---
tipo: indice
version: 1.3
fecha: 2026-06-29
---

# Índice maestro del TFDC

## Cómo leer este índice

Este archivo es el punto de entrada único a la base operativa del proyecto.
Antes de abrir cualquier otro archivo, consultá este índice para saber qué existe y en qué estado está.

Las carpetas `legacy/` dentro de cada sección contienen PDFs originales que NO se leen
en operación normal. Solo se abren bajo pedido explícito para resolver discrepancias puntuales.

Nota de versión (Fase 2, 2026-06-29): los seis resúmenes MD de `normativa/` fueron reescritos
en versión densa y accionable (alcance, reglas accionables numeradas, números y formatos exactos,
ambigüedades) verificando contra los PDFs de `normativa/legacy/`. Reemplazan a los resúmenes
comprimidos de Codex. Precedencia normativa: el Documento 302-BI prevalece en conflicto,
en particular frente al Documento 303-BI.

Nota de versión (Fase 3, 2026-06-29): ampliados a versión densa los resúmenes de pasantía
(`pasantia/informe_pasantia_perfil_termico_proteoma.md`), anteproyecto
(`proyecto/anteproyecto_tfdc_nazareno_cabrera.md`) y bibliografía (`bibliografia/*.md`).
El anteproyecto ahora contiene hipótesis, objetivo general, los seis OE y el cronograma,
como insumo directo de la Fase 4. La pasantía distingue qué quedó validado, qué fue exploratorio
y qué no se retoma, y deja explícito que la adquisición DIA no fue parte validada de la pasantía.
Los MD de papers incorporan `bloque_tematico` en YAML. El PDF de Frey 2025 y su copia
`copia_setup` son idénticos (mismo md5); el resumen principal es `frey2025_dia_cqe_lfq.md`.

Nota de versión (Fase 4, 2026-06-29): completado `estado_actual_tesis.md` (v1.0) con estado real
por objetivo. OE1 COMPLETADO como resultado exploratorio (n=2): IC50 ~1 µg/mL e IC90 turbidimétrico
operativo 2 µg/mL en CGXII-sacarosa (no MIC clásica); réplica 3 excluida por control de calidad.
OE2 a OE6 NO INICIADOS; la adquisición DIA no comenzó. Introducción NO INICIADA en `redaccion/`.

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

## Resúmenes PDF operativos

| Resumen MD | PDF original |
|------------|--------------|
| normativa/documento_302_bi_normas_presentacion_tfdc.md | normativa/legacy/documento_302_bi_normas_presentacion_tfdc.pdf |
| normativa/documento_303_bi_hoja_verificacion.md | normativa/legacy/documento_303_bi_hoja_verificacion.pdf |
| normativa/documento_304_desarrollo_tfdc.md | normativa/legacy/documento_304_desarrollo_tfdc.pdf |
| normativa/documento_305_guia_tutores.md | normativa/legacy/documento_305_guia_tutores.pdf |
| normativa/documento_306_titulos_abstracts_correccion.md | normativa/legacy/documento_306_titulos_abstracts_correccion.pdf |
| normativa/guia_tesis_biotecnologia_2023.md | normativa/legacy/guia_tesis_biotecnologia_2023.pdf |
| proyecto/anteproyecto_tfdc_nazareno_cabrera.md | proyecto/legacy/anteproyecto_tfdc_nazareno_cabrera.pdf |
| pasantia/informe_pasantia_perfil_termico_proteoma.md | pasantia/legacy/informe_pasantia_perfil_termico_proteoma.pdf |
| bibliografia/stuart_beyond_inhibition_rifampicin_mycobacteria.md | bibliografia/legacy/stuart_beyond_inhibition_rifampicin_mycobacteria.pdf |
| bibliografia/frey2025_dia_cqe_lfq.md | bibliografia/legacy/frey2025_dia_cqe_lfq.pdf |
| bibliografia/frey2025_dia_cqe_lfq_copia_setup.md | bibliografia/legacy/frey2025_dia_cqe_lfq_copia_setup.pdf |
| experimentos/protocolo_azalea_soluciones_cultivo_proteinas.md | experimentos/legacy/protocolo_azalea_soluciones_cultivo_proteinas.pdf |
| experimentos/manual_amersham_lmw_sds.md | experimentos/legacy/manual_amersham_lmw_sds.pdf |
| experimentos/protocolo_crecimiento_corynebacterium.md | experimentos/legacy/protocolo_crecimiento_corynebacterium.pdf |
| experimentos/OE1_MIC_IC50/protocolo_mic_ic50_emb_v6.md | experimentos/OE1_MIC_IC50/legacy/protocolo_mic_ic50_emb_v6.pdf |
| experimentos/OE1_MIC_IC50/protocolo_od600_emb_2026_04_22.md | experimentos/OE1_MIC_IC50/legacy/protocolo_od600_emb_2026_04_22.pdf |
| experimentos/OE1_MIC_IC50/protocolo_od600_emb_v4_2026_05_13.md | experimentos/OE1_MIC_IC50/legacy/protocolo_od600_emb_v4_2026_05_13.pdf |
| experimentos/OE1_MIC_IC50/MIC/MIC Final Analisis/informe_metodologico_mic_emb_final.md | experimentos/OE1_MIC_IC50/MIC/MIC Final Analisis/informe_metodologico_mic_emb_final.pdf |
| experimentos/OE2_validacion_DIA/protocolo_fasp_stagetips_ubypa.md | experimentos/OE2_validacion_DIA/legacy/protocolo_fasp_stagetips_ubypa.pdf |
| experimentos/OE2_validacion_DIA/protocolo_extraccion_proteinas_celulares.md | experimentos/OE2_validacion_DIA/legacy/protocolo_extraccion_proteinas_celulares.pdf |
| experimentos/OE2_validacion_DIA/protocolo_fasp_stagetips_copia.md | experimentos/OE2_validacion_DIA/legacy/protocolo_fasp_stagetips_copia.pdf |
| recursos/tutorial_patternlab_v.md | recursos/legacy/tutorial_patternlab_v.pdf |
| recursos/obligatorio_bioinformatica_1.md | recursos/legacy/obligatorio_bioinformatica_1.pdf |
| analisis/Analisis Rstudio/figura_2b_replica_norm_mediana.md | analisis/Analisis Rstudio/figura_2b_replica_norm_mediana.pdf |
| analisis/Analisis Rstudio/figura_2b_pairwise_estilo.md | analisis/Analisis Rstudio/figura_2b_pairwise_estilo.pdf |

## Pendientes derivados

- estado_actual_tesis.md: COMPLETADO (Fase 4, v1.0, 2026-06-29).
- AGENTS.md: pendiente (Claude, Fase 7 de su prompt).
- INDEX_corpus_obsidian.md: pendiente (Claude, Fase 8 de su prompt).
- Tablas de experimentos y análisis del INDEX: pendientes de poblar con metadata YAML (Fase 5).
- Concentración subinhibitoria de tratamiento para OE3: pendiente de fijar a partir de IC50 ~1 µg/mL e IC90 ~2 µg/mL.
- Análisis formal de IC50/IC90 en GraphPad: pendiente de consolidar contra los archivos Prism de la carpeta.
- Adquisición DIA: no iniciada (OE2 a OE6).
