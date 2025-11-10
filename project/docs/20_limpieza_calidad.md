# Limpieza y Control de Calidad (Plata)

## Validaciones aplicadas

| Regla | Condición |
|--------|-----------|
| Fecha válida | `fecha` convertible a ISO (YYYY-MM-DD) |
| Cliente no vacío | `id_cliente` ≠ "" |
| Producto válido | `id_producto` ∈ catálogo (P10–P50) |
| Unidades positivas | `unidades ≥ 0` |
| Precio positivo | `precio_unitario ≥ 0` |
