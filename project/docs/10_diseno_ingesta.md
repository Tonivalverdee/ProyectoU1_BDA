# Diseño de Ingesta (Bronce)

## Estrategia de ingesta
La ingesta se realiza en modo **batch diario**, leyendo automáticamente todos los archivos del directorio `project/data/drops/`.
Cada lote genera un identificador único con `_ingest_ts`, `_source_file` y `_batch_id`.
