# 20. Limpieza y Control de Calidad

## 1. Objetivo
Definir las reglas de validación, limpieza y control de calidad sobre los datos ingeridos, garantizando consistencia y fiabilidad antes del modelado.

## 2. Procedimientos aplicados

1. **Conversión de tipos**  
   - `fecha` → conversión a tipo fecha (`datetime.date`).
   - `unidades` → conversión a entero o flotante.
   - `precio_unitario` → conversión a tipo decimal para evitar errores de redondeo.

2. **Rangos y dominios válidos**  
   - `unidades >= 0`
   - `precio_unitario >= 0`
   - `id_cliente` y `id_producto` no vacíos.

3. **Registros inválidos**  
   Todos los registros que incumplen las condiciones anteriores se trasladan a un fichero de cuarentena (`ventas_invalidas.csv`), junto con la causa de error detectada.

4. **Registros válidos (Plata)**  
   Los registros que superan la validación se almacenan en formato Parquet (`clean_ventas.parquet`), listos para el modelado posterior.

5. **Deduplicación**  
   Se aplica deduplicación por la clave natural (`fecha`, `id_cliente`, `id_producto`), conservando el registro más reciente según `_ingest_ts`.

## 3. Integridad referencial
El sistema prevé validaciones opcionales de catálogo de productos o clientes, para garantizar coherencia con un maestro de datos externo.

## 4. Mecanismos de control de calidad
- Conteo de filas válidas e inválidas por lote.
- Comparación con lotes previos.
- Registro de causas de error.
- Reporte de estadísticas de calidad (porcentaje de registros válidos).
