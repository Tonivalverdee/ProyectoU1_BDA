# Proyecto UT1 · Retail Mini — Ingesta, Limpieza y Reporte en Python

**Autor:** Antonio Valverde Soto  
**Año académico:** 2025  
**Asignatura:** Big Data & Analytics — UT1  
**Repositorio base:** Proyecto_UT1_RA1_BA  
**Versión:** 1.0  

---

## Objetivo general

Construir un pipeline de datos completo que cubra todas las fases del ciclo de procesamiento:

1. **Ingesta (Bronce):** Lectura batch/micro-batch de ficheros CSV, trazabilidad e idempotencia.  
2. **Limpieza y modelado (Plata):** Validación de tipos, nulos, rangos y dominios, deduplicación con política “último gana”.  
3. **Almacenamiento (Oro):** Persistencia en formatos analíticos (Parquet y SQLite).  
4. **Reporte Markdown:** Generación automática de KPIs y tablas (sin visualización gráfica).  

---

## Ejecución

```bash
cd project/ingest
python get_data.py
python run.py
```

---

## Metodología (Bronce → Plata → Oro)

| Capa | Descripción | Formato |
|------|--------------|----------|
| **Bronce** | Datos crudos con trazabilidad | SQLite (`raw_ventas`) |
| **Plata** | Datos validados y deduplicados | Parquet (`clean_ventas.parquet`) |
| **Oro** | Datos listos para análisis y reporte | Markdown + SQLite |

---

## Documentación Quartz

El sitio Quartz se genera desde `/project/docs` y se publica con GitHub Pages.

```ts
export default {
  source: "project/docs",
  output: "site",
  theme: "default",
  title: "Proyecto UT1 · Retail Mini",
  description: "Documentación técnica — Antonio Valverde Soto",
}
```

---

## Licencia

Proyecto educativo con licencia MIT — Antonio Valverde Soto.
