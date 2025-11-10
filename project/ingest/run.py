from pathlib import Path
from datetime import datetime, timezone
import pandas as pd
import sqlite3

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "drops"
OUT = ROOT / "output"
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "parquet").mkdir(parents=True, exist_ok=True)
(OUT / "quality").mkdir(parents=True, exist_ok=True)

# Ingesta (Bronce)
files = sorted(DATA.glob("*.csv"))
raw_parts = []
for f in files:
    df = pd.read_csv(f, dtype=str)
    df["_source_file"] = f.name
    df["_ingest_ts"] = datetime.now(timezone.utc).isoformat()
    df["_batch_id"] = df["_ingest_ts"].replace(":", "-")
    raw_parts.append(df)
raw_df = pd.concat(raw_parts, ignore_index=True) if raw_parts else pd.DataFrame()

# Validación y limpieza (Plata)
def to_float_money(x):
    try:
        return float(str(x).replace(",", "."))
    except:
        return None

df = raw_df.copy()
df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce").dt.date
df["unidades"] = pd.to_numeric(df["unidades"], errors="coerce")
df["precio_unitario"] = df["precio_unitario"].apply(to_float_money)
valid = (
    df["fecha"].notna()
    & df["unidades"].notna() & (df["unidades"] >= 0)
    & df["precio_unitario"].notna() & (df["precio_unitario"] >= 0)
    & df["id_cliente"].notna() & (df["id_cliente"] != "")
    & df["id_producto"].notna() & (df["id_producto"] != "")
)
quarantine = df.loc[~valid].copy()
clean = df.loc[valid].copy()

if not clean.empty:
    clean["_ingest_ts_parsed"] = pd.to_datetime(clean["_ingest_ts"], errors="coerce")
    clean = (
        clean.sort_values(["fecha", "id_cliente", "id_producto", "_ingest_ts_parsed"])
             .drop_duplicates(subset=["fecha", "id_cliente", "id_producto"], keep="last")
    )
    clean["importe"] = clean["unidades"] * clean["precio_unitario"]

# Persistencia (Oro)
quarantine.to_csv(OUT / "quality" / "ventas_invalidas.csv", index=False)
PARQUET_FILE = OUT / "parquet" / "clean_ventas.parquet"
if not clean.empty:
    clean.to_parquet(PARQUET_FILE, index=False)

DB = OUT / "ut1.db"
con = sqlite3.connect(DB)
if not df.empty:
    df.to_sql("raw_ventas", con, if_exists="replace", index=False)
if not clean.empty:
    clean.to_sql("clean_ventas", con, if_exists="replace", index=False)
    con.execute("CREATE VIEW IF NOT EXISTS ventas_diarias AS SELECT fecha, COUNT(*) AS transacciones, SUM(importe) AS ingresos FROM clean_ventas GROUP BY fecha ORDER BY fecha;")
con.close()

# Reporte Markdown
# === 5️⃣ REPORTE MARKDOWN (KPIs + TABLAS BONITAS) ===
print("📊 Generando reporte Markdown...")

if PARQUET_FILE.exists():
    clean_rep = pd.read_parquet(PARQUET_FILE)
else:
    clean_rep = pd.DataFrame(columns=["fecha","id_cliente","id_producto","unidades","precio_unitario","importe"])

if not clean_rep.empty:
    ingresos = float(clean_rep["importe"].sum())
    trans = int(len(clean_rep))
    ticket = float(ingresos / trans) if trans > 0 else 0.0

    top = (
        clean_rep.groupby("id_producto", as_index=False)
        .agg(importe=("importe", "sum"))
        .sort_values("importe", ascending=False)
    )
    total_imp = top["importe"].sum() or 1.0
    top["pct"] = (100 * top["importe"] / total_imp).round(0).astype(int).astype(str) + "%"

    by_day = (
        clean_rep.groupby("fecha", as_index=False)
        .agg(importe_total=("importe", "sum"), transacciones=("importe", "count"))
        .sort_values("fecha")
    )

    periodo_ini = str(clean_rep["fecha"].min())
    periodo_fin = str(clean_rep["fecha"].max())
    producto_lider = top.iloc[0]["id_producto"] if not top.empty else "—"
else:
    ingresos = ticket = 0.0
    trans = 0
    top = pd.DataFrame(columns=["id_producto","importe","pct"])
    by_day = pd.DataFrame(columns=["fecha","importe_total","transacciones"])
    periodo_ini = periodo_fin = producto_lider = "—"

# === Crear el contenido del reporte ===
report = (
    "# Reporte UT1 · Ventas\n"
    f"**Periodo:** {periodo_ini} a {periodo_fin} · **Fuente:** clean_ventas (Parquet) · **Generado:** {datetime.now(timezone.utc).isoformat()}\n\n"
    "## 1. Titular\n"
    f"Ingresos totales {ingresos:.2f} €; producto líder: {producto_lider}.\n\n"
    "## 2. KPIs\n"
    f"- **Ingresos netos:** {ingresos:.2f} €\n"
    f"- **Ticket medio:** {ticket:.2f} €\n"
    f"- **Transacciones:** {trans}\n\n"
    "## 3. Top productos\n"
    f"{(top.to_markdown(index=False) if not top.empty else '_(sin datos)_')}\n\n"
    "## 4. Resumen por día\n"
    f"{(by_day.to_markdown(index=False) if not by_day.empty else '_(sin datos)_')}\n\n"
    "## 5. Calidad y cobertura\n"
    f"- Filas bronce: {len(df)} · Plata: {len(clean)} · Cuarentena: {len(quarantine)}\n\n"
    "## 6. Persistencia\n"
    f"- Parquet: {PARQUET_FILE}\n"
    f"- SQLite : {DB} (tablas: raw_ventas, clean_ventas; vista: ventas_diarias)\n\n"
    "## 7. Conclusiones\n"
    "- Reponer producto líder según demanda.\n"
    "- Revisar filas en cuarentena (rangos/tipos).\n"
    "- Valorar particionado por fecha para crecer.\n"
)

# === Guardar el reporte ===
(OUT / "reporte.md").write_text(report, encoding="utf-8")
print("✅ Pipeline ejecutado correctamente. Reporte generado en:", OUT / "reporte.md")

