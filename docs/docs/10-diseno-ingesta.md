# 10. Diseño de la Ingesta de Datos

## 1. Objetivo
Definir el proceso de ingesta de datos de ventas diarias en formato CSV, garantizando idempotencia, trazabilidad y registro de la fuente de origen.

## 2. Metodología
El proceso de ingesta se realiza mediante un *batch diario*, a partir de ficheros almacenados en la ruta:
```
project/data/drops/YYYY-MM-DD/ventas.csv
```

Cada fichero constituye un lote de datos con identificador único (`batch_id`), y contiene las columnas:
- `fecha`
- `id_cliente`
- `id_producto`
- `unidades`
- `precio_unitario`

El sistema registra trazabilidad mediante los campos:
- `_source_file` → nombre del archivo de origen.
- `_ingest_ts` → marca temporal de ingesta en formato ISO8601.
- `_batch_id` → identificador del lote procesado.

## 3. Idempotencia
El pipeline está diseñado de forma idempotente, lo que significa que la reingesta del mismo lote no genera duplicados. Para ello:
- Se utiliza una clave natural compuesta por (`fecha`, `id_cliente`, `id_producto`).
- La política de resolución de duplicados aplica la regla “último gana”, basada en `_ingest_ts`.

## 4. Trazabilidad
Cada registro conserva metadatos de su origen y tiempo de procesamiento. Esto permite auditar la procedencia y el momento exacto de la ingesta.

## 5. Validación inicial
Durante la ingesta, se validan aspectos básicos como:
- Existencia de todas las columnas esperadas.
- Tipos compatibles (por ejemplo, `fecha` en formato ISO, `precio_unitario` numérico).
- Número de filas no vacío.

Los ficheros que no cumplen con las condiciones mínimas son descartados y registrados en un área de cuarentena (`project/output/quality/ventas_invalidas.csv`).
