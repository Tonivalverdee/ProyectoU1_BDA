# 40. Reporte Markdown — Resultados y Conclusiones

## 1. Objetivo
El reporte Markdown constituye el resultado final del pipeline y presenta los indicadores del negocio de forma textual y tabular.

## 2. Contenido
Incluye los apartados:

1. **Titular** — resumen ejecutivo con los resultados globales.  
2. **KPIs principales** — ingresos, ticket medio, número de transacciones.  
3. **Top productos** — tabla de productos con mayor importe total.  
4. **Resumen diario** — tabla de ingresos por fecha.  
5. **Calidad y cobertura** — conteo de filas válidas, inválidas y métricas de consistencia.  
6. **Conclusiones** — interpretación de resultados y posibles acciones.

## 3. Ejemplo de salida

```
# Reporte UT1 · Ventas
Periodo: 2025-01-01 a 2025-01-31
Fuente: clean_ventas (Parquet)

Ingresos totales: 12 340.50 €
Ticket medio: 17.34 €
Transacciones: 712
Producto líder: P10

Top productos:
| id_producto | importe | pct |
|--------------|----------|------|
| P10 | 4 550.00 | 37% |
| P20 | 3 120.00 | 25% |
| P30 | 2 410.50 | 20% |
```
Este formato permite integrarse directamente con plataformas como Quartz o Pages, para su publicación automática.
