---
tipo: indice
version: 1.0
fecha: 2026-06-29
---

# Índice maestro del TFDC

## Cómo leer este índice

Este archivo es el punto de entrada único a la base operativa del proyecto.
Antes de abrir cualquier otro archivo, consultá este índice para saber qué existe y en qué estado está.

Las carpetas `legacy/` dentro de cada sección contienen PDFs originales que NO se leen
en operación normal. Solo se abren bajo pedido explícito para resolver discrepancias puntuales.

Estados posibles de un archivo de datos o análisis:
- estado_dato: crudo (generado, sin procesar) o analizado (con resultado interpretable)
- estado_integracion: aislado (existe pero no está en la tesis) o integrado (ya redactado en redaccion/)

## Mapa de carpetas

| Carpeta | Contenido | Leer en operación normal |
|---------|-----------|--------------------------|
| normativa/ | Resúmenes MD de normas ORT | Sí |
| normativa/legacy/ | PDFs regulatorios originales | NO |
| proyecto/ | Documentos operativos del anteproyecto | Sí |
| proyecto/legacy/ | Anteproyecto y formulario original | NO |
| experimentos/ | Registros de experimentos por OE | Sí |
| experimentos/legacy/ | Protocolos generales originales | NO |
| experimentos/OE1_MIC_IC50/ | Datos, análisis e imágenes de OE1 | Sí |
| experimentos/OE1_MIC_IC50/legacy/ | Protocolos originales de OE1 | NO |
| experimentos/OE2_validacion_DIA/ | Validación DIA | Sí |
| experimentos/OE2_validacion_DIA/legacy/ | Protocolos originales del pipeline proteómico | NO |
| analisis/ | Salidas analizadas | Sí |
| redaccion/ | Texto de la tesis en desarrollo | Sí |
| bibliografia/ | Resúmenes MD de papers y QA | Sí |
| bibliografia/legacy/ | PDFs de papers originales | NO |
| pasantia/ | Resumen del informe de pasantía | Sí |
| pasantia/legacy/ | Informe de pasantía PDF original | NO |
| recursos/ | Recursos de soporte técnico | Sí |
| recursos/legacy/ | PDFs de soporte técnico originales | NO |
| recursos/scripts/ | Scripts de soporte y análisis | Sí |
| recursos/presentaciones/ | Presentaciones del proyecto | Sí |

## Tabla de experimentos

| Archivo | OE | estado_dato | estado_integracion | fecha | depende_de |
|---------|-----|-------------|-------------------|-------|------------|
| (vacío) | | | | | |

## Tabla de análisis

| Archivo | OE | estado_dato | estado_integracion | fecha |
|---------|-----|-------------|-------------------|-------|
| (vacío) | | | | |

## Tabla de redacción

| Sección | Estado | Bloques cubiertos |
|---------|--------|-------------------|
| introduccion/ | no iniciado | |
| materiales_metodos/ | no iniciado | |
| resultados/ | no iniciado | |
| discusion/ | no iniciado | |
| conclusiones/ | no iniciado | |

## Pendientes derivados

- Todos los resúmenes MD de normativa ORT: pendiente (Claude, Fase 2 de su prompt).
- Resumen del informe de pasantía: pendiente (Claude, Fase 3 de su prompt).
- AGENTS.md: pendiente (Claude, Fase 7 de su prompt).
- INDEX_corpus_obsidian.md: pendiente (Claude, Fase 8 de su prompt).
- Análisis formal de IC50/MIC en GraphPad: pendiente de recuperar de otra computadora.
- Adquisición DIA: no iniciada.
