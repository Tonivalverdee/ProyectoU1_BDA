import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime, timedelta
import random

# === CONFIGURACIÓN DE RUTAS ===
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "drops"
DATA_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = DATA_DIR / "ventas.csv"

# === PARÁMETROS DE GENERACIÓN ===
N = 10_000  # total de registros
N_ERR = 100  # registros erróneos aprox

clientes = [f"C{str(i).zfill(3)}" for i in range(1, 501)]      # 500 clientes
productos = [f"P{str(i).zfill(2)}" for i in range(10, 51)]     # 41 productos válidos
precios = {p: round(random.uniform(5, 20), 2) for p in productos}

# === FUNCIÓN PARA CREAR REGISTROS ALEATORIOS ===
def generar_registro():
    fecha = datetime(2025, 1, 1) + timedelta(days=random.randint(0, 29))
    cliente = random.choice(clientes)
    producto = random.choice(productos)
    unidades = random.randint(1, 5)
    precio = precios[producto]
    return [fecha.date(), cliente, producto, unidades, precio]

# === GENERAR DATOS CORRECTOS ===
data = [generar_registro() for _ in range(N - N_ERR)]

# === INTRODUCIR ERRORES CONTROLADOS ===
errores = []
for i in range(N_ERR):
    r = generar_registro()
    tipo_error = random.choice(["fecha", "cliente", "producto", "unidades", "precio"])
    if tipo_error == "fecha":
        r[0] = "2025-13-40"  # fecha inválida
    elif tipo_error == "cliente":
        r[1] = ""  # cliente vacío
    elif tipo_error == "producto":
        r[2] = "P99"  # producto inexistente
    elif tipo_error == "unidades":
        r[3] = -random.randint(1, 5)  # unidades negativas
    elif tipo_error == "precio":
        r[4] = -round(random.uniform(5, 20), 2)  # precio negativo
    errores.append(r)

# === UNIR Y GUARDAR TODO ===
df = pd.DataFrame(data + errores, columns=["fecha", "id_cliente", "id_producto", "unidades", "precio_unitario"])
df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")

print(f"✅ Generado {OUTPUT_FILE} con {len(df)} filas ({N_ERR} erróneas aprox.)")
