# Proyecto UT1 — Retail Mini (Batch Simple)

**Autor:** Antonio Valverde Soto  
**Año:** 2025  
**Repositorio base:** Proyecto_UT1_RA1_BA  

---

## Objetivo general

Construir un pipeline mínimo que cubra:
1. **Ingesta** (batch o micro-batch) con trazabilidad e idempotencia  
2. **Limpieza / modelado** (tipos, nulos, rangos, dominios, dedupe)  
3. **Almacenamiento** (Parquet y/o SQLite)  
4. **Reporte Markdown** con KPIs y tablas  

---

## Esquema general del pipeline

```mermaid
flowchart LR
A[Ingesta (Bronce)] --> B[Limpieza / Modelado (Plata)]
B --> C[Almacenamiento (Oro)]
C --> D[Reporte Markdown]
```
