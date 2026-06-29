---
tipo: politica_operativa
version: 1.0
fecha: 2026-06-29
---

# Politica Git y portabilidad

Este repositorio usa Git como trazabilidad fina y GitHub como mecanismo de portabilidad entre computadoras.

## Politica vigente

- La rama operativa es `main`.
- El remoto principal es `origin`, apuntando a `https://github.com/NazarenOMICS/tesis-de-grado.git`.
- Los PDFs y fuentes originales en carpetas `legacy/` se versionan en Git para que el repositorio sea completo al clonar en otra computadora.
- Esta decision difiere del prompt maestro inicial, que proponia excluir `legacy/`. La decision vigente prioriza portabilidad y reproducibilidad local.
- El Obsidian vault no se copia ni se versiona dentro de este repositorio. Solo se versionara `bibliografia/INDEX_corpus_obsidian.md` cuando se ejecute la Fase 8.
- Cada avance real debe actualizar el archivo correspondiente, regenerar `INDEX.md` cuando cambie metadata o estructura, actualizar `CHANGELOG.md`, hacer commit descriptivo y hacer push a GitHub.

## Estado al cierre formal de Fase 6

- Git inicializado y sincronizado con GitHub.
- `CHANGELOG.md` activo y en orden cronologico inverso.
- `.gitignore` conserva exclusiones de temporales, Obsidian y datos crudos grandes, pero no excluye `legacy/`.
- PDFs versionados: 25.
- Archivos en `legacy/` versionados: 24.
