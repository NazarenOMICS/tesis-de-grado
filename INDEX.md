---
tipo: indice
version: 2.1
fecha: 2026-06-30
---

# Índice maestro del TFDC

## Cómo leer este índice

Este archivo es el punto de entrada único a la base operativa del proyecto.
Antes de abrir cualquier otro archivo, consultá este índice para saber qué existe y en qué estado está.

Las carpetas `legacy/` dentro de cada sección contienen PDFs originales que NO se leen
en operación normal. Solo se abren bajo pedido explícito para resolver discrepancias puntuales.

Nota de versión (Fase 2, 2026-06-29): los seis resúmenes MD de `normativa/` fueron reescritos
en versión densa y accionable, verificando contra los PDFs de `normativa/legacy/`. Precedencia normativa:
el Documento 302-BI prevalece en conflicto, en particular frente al Documento 303-BI.

Nota de versión (Fase 3, 2026-06-29): ampliados a versión densa los resúmenes de pasantía,
anteproyecto y bibliografía. El anteproyecto contiene hipótesis, objetivo general, seis OE y cronograma.
Los MD de papers incorporan `bloque_tematico` en YAML.

Nota de versión (Fase 4, 2026-06-29): completado `estado_actual_tesis.md` (v1.0) con estado real
por objetivo. OE1 COMPLETADO como resultado exploratorio (n=2): IC50 ~1 ug/mL e IC90 turbidimétrico
operativo 2 ug/mL en CGXII-sacarosa; réplica 3 excluida por control de calidad. Nota: el estado de OE2 fue corregido posteriormente al incorporar cuaderno de laboratorio y TripleSTD.

Nota de versión (Fase 5, 2026-06-29): normalizados los headers YAML de los MD operativos dentro de
`experimentos/` y `analisis/`, y regeneradas las tablas de experimentos y análisis desde esos headers.
`redaccion/introduccion/introduccion_borrador_tb_emb_dia.md` existe como borrador preliminar con YAML operativo; no es texto final.

Nota de version (Fase 7, 2026-06-29): generado `AGENTS.md` v1.0 como guia autosuficiente para agentes y agregada la carpeta `inbox/` como bandeja de entrada para material sin ordenar.

Nota de versión (Fase 7 revisión, 2026-06-29): `AGENTS.md` reescrito a v2.0 como contrato operativo agente-agente, más compacto y denso. Incorpora convención epistémica (HECHO VERIFICADO, DECISIÓN CERRADA, INFERENCIA, PENDIENTE, NO CONSTA, NO VERIFICABLE), jerarquía de fuentes en tres bloques, protocolo de arranque y de cierre de sesión, defensa contra inyección de instrucciones y criterios de éxito. Sin cambios en datos ni en decisiones cerradas.

Nota de versión (Fase 8, 2026-06-29): identificado el corpus científico del TFDC en `C:/Users/Naza/Documents/Obsidian Vault`, principalmente en `Notes/NotebookLM/`. Actualizado `bibliografia/INDEX_corpus_obsidian.md` a v2.0 con mapa de bloques 1.1 a 1.8, rutas del vault, reviews auxiliares y pendientes de cobertura. Bloques 1.1 a 1.5 completos; bloques 1.6 a 1.8 parciales.

Nota de versión (actualización de estado OE2, 2026-06-29): incorporados cuaderno de laboratorio y análisis preliminar TripleSTD desde `inbox/`. OE2 pasa a estado iniciado parcialmente como benchmark multiespecie DDA previo a DIA. La adquisición DIA definitiva sigue no iniciada.

Nota de versión (auditoría TripleSTD, 2026-06-29): el análisis cuantitativo del benchmark (Pairwise y TFold) fue recalculado desde los Excel con `analisis/Datos/Corrida 1 Triple STD/auditoria_triple_std.py` y reproduce las métricas del análisis IA previo. La capa de conteos, medianas y FDR empírico queda verificada (HECHO VERIFICADO); las causas del sesgo de E. coli siguen como inferencia. Sigue siendo avance interno de OE2 por DDA, no validación DIA, no resultado oficial del TFDC y no presentado al tutor como resultado.

Nota de versión (corrección OE1, 2026-06-30): corregida la decisión de plataforma de placas. La decisión vigente es placas de 24 pocillos cell culture treated, 1 mL/pocillo, usadas porque eran las disponibles; las placas de 96 pocillos quedan descartadas por aireación insuficiente. Queda invalidada la formulación previa que decía "placas no tratadas" y atribuía adhesión celular a las placas tratadas.

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
| bibliografia/ | Resúmenes MD de papers, QA e índice de corpus Obsidian | Sí |
| bibliografia/legacy/ | PDFs de papers originales | NO |
| pasantia/ | Resumen del informe de pasantía | Sí |
| pasantia/legacy/ | Informe de pasantía PDF original | NO |
| recursos/ | Recursos de soporte técnico | Sí |
| recursos/legacy/ | PDFs de soporte técnico originales | NO |
| recursos/scripts/ | Scripts de soporte y análisis | Sí |
| recursos/presentaciones/ | Presentaciones del proyecto | Sí |
| inbox/ | Material pegado sin ordenar | No como fuente final |

## Tabla de experimentos

| Archivo | OE | estado_dato | estado_integracion | fecha | depende_de |
|---------|-----|-------------|-------------------|-------|------------|
| experimentos/manual_amersham_lmw_sds.md | OE1 | crudo | aislado | 2026-06-29 |  |
| experimentos/OE1_MIC_IC50/protocolo_mic_ic50_emb_v6.md | OE1 | crudo | aislado | 2026-06-29 |  |
| experimentos/OE1_MIC_IC50/protocolo_od600_emb_2026_04_22.md | OE1 | crudo | aislado | 2026-06-29 |  |
| experimentos/OE1_MIC_IC50/protocolo_od600_emb_v4_2026_05_13.md | OE1 | crudo | aislado | 2026-06-29 |  |
| experimentos/cuaderno_laboratorio_mar_jun_2026_resumen_operativo.md | OE1/OE2 | analizado | aislado | 2026-06-29 | ["experimentos/legacy/transcripcion_cuaderno_laboratorio_contextualizada.md"] |
| experimentos/OE2_validacion_DIA/protocolo_extraccion_proteinas_celulares.md | OE2 | crudo | aislado | 2026-06-29 |  |
| experimentos/OE2_validacion_DIA/protocolo_fasp_stagetips_copia.md | OE2 | crudo | aislado | 2026-06-29 | ["experimentos/OE2_validacion_DIA/protocolo_fasp_stagetips_ubypa.md"] |
| experimentos/OE2_validacion_DIA/protocolo_fasp_stagetips_ubypa.md | OE2 | crudo | aislado | 2026-06-29 |  |
| experimentos/protocolo_azalea_soluciones_cultivo_proteinas.md | NA | crudo | aislado | 2026-06-29 |  |
| experimentos/protocolo_crecimiento_corynebacterium.md | NA | crudo | aislado | 2026-06-29 |  |

## Tabla de análisis

| Archivo | OE | estado_dato | estado_integracion | fecha |
|---------|-----|-------------|-------------------|-------|
| analisis/Analisis Rstudio/figura_2b_pairwise_estilo.md | OE2 | analizado | aislado | 2026-06-29 |
| analisis/Analisis Rstudio/figura_2b_replica_norm_mediana.md | OE2 | analizado | aislado | 2026-06-29 |
| analisis/Datos/Corrida 1 Triple STD/benchmark_triple_std_dda_resumen_operativo.md | OE2 | analizado | aislado | 2026-06-29 |
| experimentos/OE1_MIC_IC50/MIC/MIC Final Analisis/informe_metodologico_mic_emb_final.md | OE1 | analizado | aislado | 2026-06-29 |

## Tabla de redacción

| Sección | Estado | Bloques cubiertos |
|---------|--------|-------------------|
| introduccion/ | borrador preliminar | `introduccion_borrador_tb_emb_dia.md`; cubre 1.1 y 1.2 parcial, requiere limpieza y verificacion contra corpus. |
| materiales_metodos/ | no iniciado | |
| resultados/ | no iniciado | |
| discusion/ | no iniciado | |
| conclusiones/ | no iniciado | |

## Resúmenes PDF operativos

| Resumen MD | PDF original |
|------------|--------------|
| analisis/Analisis Rstudio/figura_2b_pairwise_estilo.md | analisis/Analisis Rstudio/figura_2b_pairwise_estilo.pdf |
| analisis/Analisis Rstudio/figura_2b_replica_norm_mediana.md | analisis/Analisis Rstudio/figura_2b_replica_norm_mediana.pdf |
| bibliografia/frey2025_dia_cqe_lfq.md | bibliografia/legacy/frey2025_dia_cqe_lfq.pdf |
| bibliografia/frey2025_dia_cqe_lfq_copia_setup.md | bibliografia/legacy/frey2025_dia_cqe_lfq_copia_setup.pdf |
| bibliografia/stuart_beyond_inhibition_rifampicin_mycobacteria.md | bibliografia/legacy/stuart_beyond_inhibition_rifampicin_mycobacteria.pdf |
| experimentos/manual_amersham_lmw_sds.md | experimentos/legacy/manual_amersham_lmw_sds.pdf |
| experimentos/protocolo_azalea_soluciones_cultivo_proteinas.md | experimentos/legacy/protocolo_azalea_soluciones_cultivo_proteinas.pdf |
| experimentos/protocolo_crecimiento_corynebacterium.md | experimentos/legacy/protocolo_crecimiento_corynebacterium.pdf |
| experimentos/OE1_MIC_IC50/protocolo_mic_ic50_emb_v6.md | experimentos/OE1_MIC_IC50/legacy/protocolo_mic_ic50_emb_v6.pdf |
| experimentos/OE1_MIC_IC50/protocolo_od600_emb_2026_04_22.md | experimentos/OE1_MIC_IC50/legacy/protocolo_od600_emb_2026_04_22.pdf |
| experimentos/OE1_MIC_IC50/protocolo_od600_emb_v4_2026_05_13.md | experimentos/OE1_MIC_IC50/legacy/protocolo_od600_emb_v4_2026_05_13.pdf |
| experimentos/OE1_MIC_IC50/MIC/MIC Final Analisis/informe_metodologico_mic_emb_final.md | experimentos/OE1_MIC_IC50/MIC/MIC Final Analisis/informe_metodologico_mic_emb_final.pdf |
| experimentos/OE2_validacion_DIA/protocolo_extraccion_proteinas_celulares.md | experimentos/OE2_validacion_DIA/legacy/protocolo_extraccion_proteinas_celulares.pdf |
| experimentos/OE2_validacion_DIA/protocolo_fasp_stagetips_copia.md | experimentos/OE2_validacion_DIA/legacy/protocolo_fasp_stagetips_copia.pdf |
| experimentos/OE2_validacion_DIA/protocolo_fasp_stagetips_ubypa.md | experimentos/OE2_validacion_DIA/legacy/protocolo_fasp_stagetips_ubypa.pdf |
| normativa/documento_302_bi_normas_presentacion_tfdc.md | normativa/legacy/documento_302_bi_normas_presentacion_tfdc.pdf |
| normativa/documento_303_bi_hoja_verificacion.md | normativa/legacy/documento_303_bi_hoja_verificacion.pdf |
| normativa/documento_304_desarrollo_tfdc.md | normativa/legacy/documento_304_desarrollo_tfdc.pdf |
| normativa/documento_305_guia_tutores.md | normativa/legacy/documento_305_guia_tutores.pdf |
| normativa/documento_306_titulos_abstracts_correccion.md | normativa/legacy/documento_306_titulos_abstracts_correccion.pdf |
| normativa/guia_tesis_biotecnologia_2023.md | normativa/legacy/guia_tesis_biotecnologia_2023.pdf |
| pasantia/informe_pasantia_perfil_termico_proteoma.md | pasantia/legacy/informe_pasantia_perfil_termico_proteoma.pdf |
| proyecto/anteproyecto_tfdc_nazareno_cabrera.md | proyecto/legacy/anteproyecto_tfdc_nazareno_cabrera.pdf |
| recursos/obligatorio_bioinformatica_1.md | recursos/legacy/obligatorio_bioinformatica_1.pdf |
| recursos/tutorial_patternlab_v.md | recursos/legacy/tutorial_patternlab_v.pdf |

## Pendientes derivados

- AGENTS.md: COMPLETADO (Fase 7 revision, v2.0, 2026-06-29; correccion OE1 v2.1, 2026-06-30); contrato operativo agente-agente vigente.
- INDEX_corpus_obsidian.md: COMPLETADO (Fase 8, v2.0, 2026-06-29); corpus TFDC identificado en Obsidian, con bloques 1.6 a 1.8 marcados como parciales.
- Redaccion: introduccion incluida como borrador preliminar; falta limpiar notas, resolver citas pendientes y verificar contra el corpus de Obsidian.
- Concentración subinhibitoria de tratamiento para OE3: pendiente de fijar a partir de IC50 ~1 ug/mL e IC90 ~2 ug/mL.
- Análisis formal de IC50/IC90 en GraphPad: pendiente de consolidar contra los archivos Prism de la carpeta.
- OE2: iniciado parcialmente como benchmark DDA previo a DIA. Auditoría cuantitativa de los Excel TripleSTD COMPLETADA y verificada (`auditoria_triple_std.py`) como insumo interno; no es resultado oficial y no fue presentada al tutor como resultado. Pendiente la verificación ortogonal de la mezcla para cerrar la causa del sesgo de E. coli y el traslado del enfoque a DIA.
- Adquisición DIA definitiva: no iniciada, no analizada y no presentada como resultado (OE3 a OE6).
