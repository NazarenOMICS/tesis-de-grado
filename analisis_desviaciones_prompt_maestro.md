---
tipo: analisis_operativo
version: 1.0
fecha: 2026-06-29
destinatario: Claude
---

# Desviaciones del prompt maestro operativo

Este archivo registra diferencias entre el prompt maestro inicial y la ejecucion real realizada en Codex. La base quedo funcional, pero conviene que Claude conozca estos ajustes antes de continuar.

## Desviaciones principales

- Se aplico una correccion posterior de categorizacion enviada por Nazareno, por encima de las reglas iniciales del prompt maestro.
- Se crearon carpetas adicionales no listadas en la estructura original: `proyecto/`, `experimentos/legacy/`, `experimentos/OE1_MIC_IC50/legacy/`, `experimentos/OE1_MIC_IC50/geles/`, `experimentos/OE2_validacion_DIA/legacy/`, `recursos/legacy/`, `recursos/scripts/` y `recursos/presentaciones/`.
- El archivo `INDEX.md` no quedo como copia exacta del esqueleto original. Fue adaptado a la estructura real y se le agrego una tabla de correspondencia entre resúmenes MD y PDFs originales.
- Se generaron resúmenes MD para cada PDF, aunque el prompt maestro inicial reservaba parte de la sintesis para Claude. Estos resúmenes son operativos y comprimidos, no deben tomarse como sintesis academica final.
- Los PDFs fueron renombrados con nombres semanticos para mejorar trazabilidad.
- Los PDFs en `legacy/` primero quedaron ignorados por Git, pero luego se cambio la decision para versionarlos y poder mover la base completa entre computadoras por GitHub.
- Se modifico `.gitignore`: ya no excluye `**/legacy/`.
- Se agregaron archivos `.gitkeep` para conservar carpetas vacias en Git.
- Se incorporo `Obligatorio bioinformatica 1.pdf` desde una copia ubicada fuera de la carpeta inicial, porque habia aparecido en el inventario original y luego no estaba dentro del arbol reorganizado.
- Se subio todo el repositorio a GitHub en `NazarenOMICS/tesis-de-grado`, rama `main`.

## Criterio para Claude

Claude deberia tratar los MD generados como capa de lectura rapida y no como resumen definitivo. Para redaccion, sintesis o citas metodologicas finas, conviene usar estos MD como mapa inicial y abrir el PDF original solo cuando sea necesario resolver una discrepancia, confirmar un dato puntual o extraer una formulacion normativa.

La estructura actual del repositorio debe considerarse la base operativa vigente.
