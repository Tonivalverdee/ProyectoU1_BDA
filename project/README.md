# 📦 Proyecto UT1 — Retail Mini (Batch Simple)

## 📘 Descripción general
Este directorio contiene el código fuente y datos del pipeline del proyecto UT1 de la asignatura Big Data & Analytics.

## 🧱 Estructura interna

```
project/
├── data/              # Datos de entrada (ventas generadas)
├── ingest/            # Scripts de ingesta y pipeline principal
├── output/            # Resultados (Parquet, SQLite, Markdown)
├── tools/             # Requisitos y utilidades
├── sql/               # Scripts SQL opcionales
└── docs/              # Documentación Quartz
```

## ⚙️ Ejecución

1️⃣ Generar los datos de ejemplo:
```bash
cd ingest
python get_data.py
```

2️⃣ Ejecutar el pipeline completo:
```bash
python run.py
```

## 🧾 Resultados esperados

| Archivo | Descripción |
|----------|--------------|
| `output/parquet/clean_ventas.parquet` | Datos limpios |
| `output/quality/ventas_invalidas.csv` | Filas con errores |
| `output/ut1.db` | Base SQLite con raw_ventas y clean_ventas |
| `output/reporte.md` | Reporte Markdown final |

---

## 📊 Capas del pipeline

| Capa | Descripción | Archivo |
|------|--------------|----------|
| Bronce | Datos crudos | raw_ventas (SQLite) |
| Plata | Datos limpios | clean_ventas.parquet |
| Oro | Reporte final | reporte.md |

---

## 📚 Dependencias
El archivo `tools/requirements.txt` contiene las librerías necesarias:
```
pandas
numpy
pyarrow
tabulate
```
Instalar con:
```bash
pip install -r tools/requirements.txt
```

---

## 🧠 Autor
**Antonio Valverde Soto — 2025**
