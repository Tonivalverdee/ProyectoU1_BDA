# 30. Modelado de Datos y KPIs (Capa Oro)

## 1. Objetivo
Desarrollar el modelo de datos de la capa oro, orientado a la generación de indicadores clave (KPIs) del negocio minorista.

## 2. Cálculo del importe
Se define una nueva variable derivada:
```
importe = unidades * precio_unitario
```

## 3. Almacenamiento
Los datos limpios se almacenan en:
- `clean_ventas.parquet` (formato analítico).
- `ut1.db` (base SQLite con tablas `raw_ventas` y `clean_ventas`).

## 4. KPIs principales
- **Ingresos totales:** suma de todos los importes.
- **Ticket medio:** ingresos totales / número de transacciones.
- **Transacciones:** total de registros válidos.
- **Producto líder:** aquel con mayor importe total acumulado.
- **Cobertura temporal:** rango de fechas disponible en los datos.

## 5. Vistas SQL
Se implementan vistas en SQLite para análisis agregados:
```sql
CREATE VIEW ventas_diarias AS
SELECT fecha,
       SUM(importe) AS ingresos_diarios,
       COUNT(*) AS transacciones
FROM clean_ventas
GROUP BY fecha;
```

## 6. Supuestos
- Los precios unitarios no varían durante el día para un mismo producto.
- La moneda base es euro (EUR).
- Los valores nulos se interpretan como 0 en los cálculos de ingresos.
