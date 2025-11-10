# 99. Lecciones Aprendidas

## 1. Aspectos positivos
- La estructura modular del proyecto permitió mantener independencia entre ingesta, limpieza, modelado y reporte.
- El uso de Parquet mejoró la eficiencia de lectura y almacenamiento.
- La implementación de SQLite permitió consultas rápidas y reutilizables.
- La idempotencia y trazabilidad garantizan reproducibilidad total del proceso.

## 2. Dificultades encontradas
- Gestión inicial del submódulo de Quartz y conflictos con GitHub Pages.
- Necesidad de ajustar versiones de Node y dependencias para la generación de reportes.
- Validación de tipos numéricos y conversión de datos en CSV con formatos mixtos.

## 3. Mejoras propuestas
- Automatizar el control de calidad con métricas de error acumuladas.
- Desarrollar una interfaz de usuario para selección de lotes.
- Integrar notificaciones o alertas automáticas ante errores de ingesta.

## 4. Conclusión
El proyecto cumple los objetivos establecidos en la UT1: ingesta controlada, limpieza de datos, modelado analítico y generación de reportes reproducibles.  
Se considera una base sólida para proyectos ETL de mayor complejidad en el ámbito de analítica empresarial.
