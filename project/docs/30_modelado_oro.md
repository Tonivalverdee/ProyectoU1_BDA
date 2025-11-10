# Modelado y Almacenamiento (Oro)

## Capas de datos
| Capa | Descripción | Formato |
|------|--------------|----------|
| Bronce | Datos sin limpiar | SQLite (`raw_ventas`) |
| Plata | Datos limpios con importe | Parquet (`clean_ventas.parquet`) |
| Oro | Datos analíticos y reporte | Markdown / SQLite vistas |
