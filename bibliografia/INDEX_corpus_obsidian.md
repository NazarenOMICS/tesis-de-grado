---
tipo: indice_corpus_obsidian
version: 2.0
fecha: 2026-06-29
estado_integracion: corpus_tfdc_identificado
ruta_vault: "C:/Users/Naza/Documents/Obsidian Vault"
ruta_corpus_principal: "C:/Users/Naza/Documents/Obsidian Vault/Notes/NotebookLM"
---

# INDEX corpus Obsidian

## Estado de Fase 8

La ruta correcta auditada fue `C:/Users/Naza/Documents/Obsidian Vault`.

Resultado: se identifico corpus cientifico del TFDC dentro de `Notes/NotebookLM`, con carpetas especificas para bloques 1.1 a 1.5 de la introduccion, reviews auxiliares sobre etambutol y C. glutamicum, material de presentacion de tesis y PDFs fuente en `Research/Papers`.

HECHO VERIFICADO: el vault contiene carpetas NotebookLM `tb-intro-bloque-1-1`, `tb-bloque-1-2`, `tb-bloque-1-3`, `tb-bloque-1-4` y `tb-bloque-1-5`. No se detectaron carpetas equivalentes para `tb-bloque-1-6`, `tb-bloque-1-7` o `tb-bloque-1-8`.

DECISION CERRADA de esta fase: este indice habilita la regla de prioridad cientifica del vault para los bloques y temas cubiertos por el corpus identificado. Para bloques parciales o sin carpeta propia, el agente debe declarar el limite y usar tambien los MD versionados del repo.

## Regla de prioridad cientifica

Ante preguntas cientificas, interpretacion de resultados, redaccion de introduccion o discusion:

1. Consultar primero este indice.
2. Abrir bajo demanda la nota especifica del vault que corresponda al bloque o pregunta.
3. Priorizar el corpus del vault sobre conocimiento general del agente cuando exista una nota relevante.
4. Usar los MD versionados del repo para hechos del proyecto, resultados propios, normativa, estado actual y trazabilidad.
5. Si una afirmacion cientifica no esta respaldada por el corpus, declararlo y separar el aporte del agente como conocimiento general.

El vault es de solo lectura para esta base. No se copia su contenido completo al repo.

## Rutas relevantes

| Uso | Ruta |
|---|---|
| Vault completo | `C:/Users/Naza/Documents/Obsidian Vault` |
| Corpus NotebookLM principal | `Notes/NotebookLM/` |
| Papers fuente | `Research/Papers/` |
| Reviews auxiliares sobre etambutol | `Notes/Reviews/ethambutol-proteomics-treatment-pipeline/` |
| Papers clave EMB en BHI | `Notes/Reviews/ethambutol-bhi-papers/` |
| Material historico MIC/EMB | `old/eth-mic-review/` |
| Presentaciones de tesis | `Tesis/Presentaciones/` |
| Dashboards de introduccion | `Notes/Dashboards/` |
| Carpeta auditada y descartada previamente | `OBL alimentos/` |

## Inventario del vault completo

Conteo general de archivos detectado:

| Extension | Cantidad |
|---|---:|
| `.md` | 855 |
| `.pdf` | 269 |
| `.json` | 25 |
| `.js` | 13 |
| `.css` | 11 |
| `.docx` | 9 |
| `.zip` | 5 |
| `.svg` | 3 |
| `.canvas` | 2 |
| `.png` | 2 |
| otros | 3 |

Este conteo es solo orientativo. No implica que todos esos archivos pertenezcan al TFDC.

## Mapa por bloque de introduccion

| Bloque | Tema | Estado | Carpeta o archivo guia | Alimenta |
|---|---|---|---|---|
| 1.1 | Tuberculosis como problema de salud publica global y local | COMPLETO | `Notes/NotebookLM/tb-intro-bloque-1-1/` | Introduccion, justificacion sanitaria |
| 1.2 | Resistencia a farmacos, MDR-TB, XDR-TB y necesidad de nuevos blancos | COMPLETO | `Notes/NotebookLM/tb-bloque-1-2/` | Introduccion, brecha terapeutica |
| 1.3 | Biologia de Mycobacteriales, crecimiento polar y envoltura | COMPLETO | `Notes/NotebookLM/tb-bloque-1-3/` | Introduccion, marco biologico |
| 1.4 | C. glutamicum como organismo modelo | COMPLETO | `Notes/NotebookLM/tb-bloque-1-4/` | Introduccion, justificacion del modelo |
| 1.5 | Mecanismo de accion del etambutol | COMPLETO | `Notes/NotebookLM/tb-bloque-1-5/` | Introduccion, hipotesis, OE1 |
| 1.6 | Vacios en el mecanismo de EMB y efectos proteomicos mas amplios | PARCIAL | `Notes/Dashboards/` y `Notes/Reviews/ethambutol-proteomics-treatment-pipeline/` | Introduccion, hipotesis, discusion futura |
| 1.7 | Proteomica como herramienta global | PARCIAL | `Notes/Reviews/ethambutol-proteomics-treatment-pipeline/`, `bibliografia/frey2025_dia_cqe_lfq.md` | OE2, OE3, introduccion metodologica |
| 1.8 | DDA frente a DIA y justificacion metodologica | PARCIAL | `bibliografia/frey2025_dia_cqe_lfq.md`, `Notes/Reviews/ethambutol-proteomics-treatment-pipeline/` | OE2, OE6, metodologia |

Advertencia: el dashboard de esqueleto completo de introduccion lista formalmente los bloques 1.1 a 1.8 y advierte que los bloques 1.4 y 1.6 contienen referencias a datos preliminares del laboratorio sin cita bibliografica formal. Si esos datos se usan como evidencia motivadora, deben citarse como comunicacion interna, dato no publicado o resultado preliminar, segun defina el tutor.

## Bloque 1.1, tuberculosis como problema sanitario

Carpeta: `Notes/NotebookLM/tb-intro-bloque-1-1/`

| Tipo | Cantidad | Archivo guia |
|---|---:|---|
| Resumenes | 3 | `QA/summaries/2026-04-04 Bloque 1.1 - Resumen para introducción.md` |
| Preguntas respondidas | 8 | `QA/answers/` |
| Fuentes anotadas | 23 | `Sources/` |

Preguntas existentes:

| Pregunta | Ruta |
|---|---|
| Carga global actual | `Notes/NotebookLM/tb-intro-bloque-1-1/QA/answers/2026-04-04 Q01 - cuál-es-la-carga-global-actual.md` |
| Mortalidad | `Notes/NotebookLM/tb-intro-bloque-1-1/QA/answers/2026-04-04 Q02 - cuáles-son-las-tasas-de-mortalidad.md` |
| Regimen de tratamiento | `Notes/NotebookLM/tb-intro-bloque-1-1/QA/answers/2026-04-04 Q03 - cuál-es-el-régimen-de-tratamiento.md` |
| Abandono | `Notes/NotebookLM/tb-intro-bloque-1-1/QA/answers/2026-04-04 Q04 - cuáles-son-las-tasas-de-abandono.md` |
| Factores sociales y epidemiologicos | `Notes/NotebookLM/tb-intro-bloque-1-1/QA/answers/2026-04-04 Q05 - qué-factores-sociales-y-epidemiológicos-específicos.md` |
| Incidencia y prevalencia | `Notes/NotebookLM/tb-intro-bloque-1-1/QA/answers/2026-04-04 Q06 - qué-datos-recientes-de-incidencia-prevalencia.md` |
| Tendencias globales | `Notes/NotebookLM/tb-intro-bloque-1-1/QA/answers/2026-04-04 Q07 - cuáles-son-las-tendencias-globales-recientes.md` |
| Vacio de cobertura asistencial | `Notes/NotebookLM/tb-intro-bloque-1-1/QA/answers/2026-04-04 Q08 - qué-vacíos-de-cobertura-asistencial-o.md` |

Fuentes destacadas: GBD 2021 EndTB milestones, Global y regional TB, determinantes sociales, adherencia, abandono, poblaciones vulnerables, resistencia y resultados de tratamiento.

## Bloque 1.2, resistencia y nuevos blancos

Carpeta: `Notes/NotebookLM/tb-bloque-1-2/`

| Tipo | Cantidad | Archivo guia |
|---|---:|---|
| Resumenes | 3 | `QA/summaries/2026-04-06 Resistencia a farmacos antituberculosos - Bloque 1.2.md` |
| Preguntas respondidas | 7 | `QA/answers/` |
| Fuentes anotadas | 25 | `Sources/` |

Preguntas existentes:

| Pregunta | Ruta |
|---|---|
| Prevalencia MDR-TB | `Notes/NotebookLM/tb-bloque-1-2/QA/answers/2026-04-06 QQ01 - es-prevalencia-global-actual-mdr-tb.md` |
| Mecanismos moleculares de resistencia | `Notes/NotebookLM/tb-bloque-1-2/QA/answers/2026-04-06 QQ02 - mecanismos-moleculares-resistencia-mycobacterium-tuberculosis-para.md` |
| Segunda y tercera linea | `Notes/NotebookLM/tb-bloque-1-2/QA/answers/2026-04-06 QQ03 - caracteristicas-definen-esquemas-terapeuticos-segunda-tercera.md` |
| Nuevos farmacos | `Notes/NotebookLM/tb-bloque-1-2/QA/answers/2026-04-06 QQ04 - nuevos-farmacos-han-sido-aprobados-bedaquilina.md` |
| Caracterizacion de blancos | `Notes/NotebookLM/tb-bloque-1-2/QA/answers/2026-04-06 QQ05 - evidencia-experimental-bibliografica-existe-caracterizacion-profundidad.md` |
| Envoltura como blanco | `Notes/NotebookLM/tb-bloque-1-2/QA/answers/2026-04-06 QQ06 - argumentos-presenta-literatura-para-considerar-envoltura.md` |
| Pipeline global | `Notes/NotebookLM/tb-bloque-1-2/QA/answers/2026-04-06 QQ07 - es-estado-actual-del-pipeline-global.md` |

Fuentes destacadas: revisiones y estudios sobre resistencia, BPaL/BPaLM, nuevos farmacos, mecanismos geneticomoleculares y pared celular como blanco.

## Bloque 1.3, Mycobacteriales y envoltura

Carpeta: `Notes/NotebookLM/tb-bloque-1-3/`

| Tipo | Cantidad | Archivo guia |
|---|---:|---|
| Resumenes | 3 | `QA/summaries/2026-04-06 Biologia de Mycobacteriales - crecimiento polar y envoltura celular.md` |
| Preguntas respondidas | 8 | `QA/answers/` |
| Fuentes anotadas | 29 | `Sources/` |

Preguntas existentes:

| Pregunta | Ruta |
|---|---|
| Crecimiento polar | `Notes/NotebookLM/tb-bloque-1-3/QA/answers/2026-04-06 Q01 - se-describe-sobre-patron-crecimiento-polar.md` |
| Elongasoma y divisoma | `Notes/NotebookLM/tb-bloque-1-3/QA/answers/2026-04-06 Q02 - componentes-del-elongasoma-divisoma-estan-presentes.md` |
| Maquinaria molecular de crecimiento polar | `Notes/NotebookLM/tb-bloque-1-3/QA/answers/2026-04-06 Q03 - maquinaria-molecular-dirige-crecimiento-polar-mycobacteriales.md` |
| Composicion de la envoltura | `Notes/NotebookLM/tb-bloque-1-3/QA/answers/2026-04-06 Q04 - es-composicion-quimica-detallada-envoltura-celular.md` |
| Contribucion de cada capa | `Notes/NotebookLM/tb-bloque-1-3/QA/answers/2026-04-06 Q05 - contribuye-cada-capa-estructural-envoltura-celular.md` |
| Rol de la envoltura en M. tuberculosis | `Notes/NotebookLM/tb-bloque-1-3/QA/answers/2026-04-06 Q06 - rol-cumple-envoltura-celular-m-tuberculosis.md` |
| Proteinas y complejos de biosintesis | `Notes/NotebookLM/tb-bloque-1-3/QA/answers/2026-04-06 Q07 - proteinas-complejos-enzimaticos-biosintesis-envoltura-celular.md` |
| Integracion biologica | `Notes/NotebookLM/tb-bloque-1-3/QA/answers/2026-04-06 Q08 - informacion-sobre-biologia-mycobacteriales-crecimiento-polar.md` |

Fuentes destacadas: crecimiento polar, DivIVA, FtsEX/RipC, peptidoglicano, arabinogalactano, acidos micolicos, micomembrana y complejos de biosintesis.

## Bloque 1.4, C. glutamicum como modelo

Carpeta: `Notes/NotebookLM/tb-bloque-1-4/`

| Tipo | Cantidad | Archivo guia |
|---|---:|---|
| Resumenes | 3 | `QA/summaries/2026-04-06 C. glutamicum como modelo de Mycobacteriales - Bloque 1.4.md` |
| Preguntas respondidas | 7 | `QA/answers/` |
| Fuentes anotadas | 20 | `Sources/` |

Preguntas existentes:

| Pregunta | Ruta |
|---|---|
| Posicion filogenetica | `Notes/NotebookLM/tb-bloque-1-4/QA/answers/2026-04-06 Q01 - es-posicion-filogenetica-corynebacterium-glutamicum-dentro.md` |
| Similitudes y diferencias de envoltura | `Notes/NotebookLM/tb-bloque-1-4/QA/answers/2026-04-06 Q02 - similitudes-diferencias-concretas-existen-arquitectura-composicion.md` |
| Vias conservadas | `Notes/NotebookLM/tb-bloque-1-4/QA/answers/2026-04-06 Q03 - vias-biosintesis-envoltura-celular-estan-conservadas.md` |
| Usos previos de C. glutamicum | `Notes/NotebookLM/tb-bloque-1-4/QA/answers/2026-04-06 Q04 - trabajos-previos-han-utilizado-c-glutamicum.md` |
| Evidencia sobre efecto de EMB | `Notes/NotebookLM/tb-bloque-1-4/QA/answers/2026-04-06 Q05 - evidencia-experimental-especifica-existe-sobre-efecto.md` |
| Ventajas operativas | `Notes/NotebookLM/tb-bloque-1-4/QA/answers/2026-04-06 Q06 - ventajas-operativas-bioseguridad-experimentales-ofrece-c.md` |
| Limitaciones del modelo | `Notes/NotebookLM/tb-bloque-1-4/QA/answers/2026-04-06 Q07 - limitaciones-concretas-presenta-c-glutamicum-modelo.md` |

Fuentes destacadas: trabajos sobre arquitectura de envoltura, genes esenciales, crecimiento polar, fenotipos por EMB y comparabilidad del modelo.

## Bloque 1.5, mecanismo de accion del etambutol

Carpeta: `Notes/NotebookLM/tb-bloque-1-5/`

| Tipo | Cantidad | Archivo guia |
|---|---:|---|
| Resumenes | 3 | `QA/summaries/2026-04-07 Mecanismo de accion del etambutol - Bloque 1.5.md` |
| Preguntas respondidas | 7 | `QA/answers/` |
| Fuentes anotadas | 27 | `Sources/` |

Preguntas existentes:

| Pregunta | Ruta |
|---|---|
| Mecanismo molecular de inhibicion | `Notes/NotebookLM/tb-bloque-1-5/QA/answers/2026-04-07 Q01 - es-mecanismo-molecular-por-etambutol-inhibe.md` |
| Datos estructurales | `Notes/NotebookLM/tb-bloque-1-5/QA/answers/2026-04-07 Q02 - datos-estructurales-alta-resolucion-existen-sobre.md` |
| Via DPA | `Notes/NotebookLM/tb-bloque-1-5/QA/answers/2026-04-07 Q03 - es-via-biosintetica-del-decaprenilfosfato-arabinosa.md` |
| Mutaciones de resistencia | `Notes/NotebookLM/tb-bloque-1-5/QA/answers/2026-04-07 Q04 - mutaciones-resistencia-al-etambutol-mas-frecuentes.md` |
| Vacios del mecanismo | `Notes/NotebookLM/tb-bloque-1-5/QA/answers/2026-04-07 Q05 - aspectos-del-mecanismo-accion-del-etambutol.md` |
| Estudios omicos globales | `Notes/NotebookLM/tb-bloque-1-5/QA/answers/2026-04-07 Q06 - estudios-proteomicos-transcriptomicos-metabolomicos-globales-han.md` |
| Complejo Emb | `Notes/NotebookLM/tb-bloque-1-5/QA/answers/2026-04-07 Q07 - se-conoce-sobre-rol-del-complejo.md` |

Fuentes destacadas: EmbB/EmbC, arabinosiltransferasas, DPA, arabinogalactano, resistencia a EMB, estructura cryo-EM, efectos sobre envoltura y estudios globales.

## Bloques 1.6 a 1.8, cobertura parcial

No se detectaron carpetas NotebookLM propias para 1.6, 1.7 y 1.8. La base disponible es parcial:

| Tema | Ruta util | Uso |
|---|---|---|
| Esqueleto de bloques 1.1 a 1.8 | `Notes/Dashboards/` | Define estructura completa de la introduccion; buscar el archivo cuyo nombre empieza con `Esqueleto completo de la Introducción` |
| Tratamientos con EMB y corpus proteomico adyacente | `Notes/Reviews/ethambutol-proteomics-treatment-pipeline/00-index.md` | Condiciones de tratamiento, medios, dosis y tiempos comparables |
| Resumen del review EMB/proteomica | `Notes/Reviews/ethambutol-proteomics-treatment-pipeline/03-summary.md` | Lectura rapida para interpretar concentraciones y limites |
| QA del review EMB/proteomica | `Notes/Reviews/ethambutol-proteomics-treatment-pipeline/02-qa.md` | Preguntas operativas sobre BHI, CGXII y proteomica directa |
| Frey 2025 | `bibliografia/frey2025_dia_cqe_lfq.md` | Base versionada para DIA, CQE, LFQ y validacion cuantitativa |
| Stuart 2026 | `bibliografia/stuart_beyond_inhibition_rifampicin_mycobacteria.md` | Antecedente conceptual sobre efectos subletales y tolerancia fenotipica, sin extrapolar rifampicina a EMB |

Nota operacional: para 1.6 no alcanza con afirmar que EMB genera reprogramacion proteomica global si solo se citan antecedentes indirectos. Diferenciar datos propios del laboratorio, antecedentes no publicados, literatura omica relacionada y resultados futuros del TFDC.

## Reviews auxiliares sobre etambutol

| Review | Ruta | Uso |
|---|---|---|
| Pipeline proteomico y condiciones de tratamiento | `Notes/Reviews/ethambutol-proteomics-treatment-pipeline/` | Separar medio, organismo, dosis, tiempo, endpoint y comparabilidad |
| Papers EMB en C. glutamicum/BHI | `Notes/Reviews/ethambutol-bhi-papers/00-index.md` | Orden de lectura: Schubert 2017, Meyer 2023, Radmacher 2005 |
| Material historico MIC/EMB | `old/eth-mic-review/` | Fuentes y QA antiguas; usar con menor prioridad que NotebookLM actual |

Puntos utiles del review de tratamiento:

| HECHO VERIFICADO EN VAULT | Implicancia |
|---|---|
| No se encontro en el corpus local un estudio proteomico directo con EMB en C. glutamicum o M. smegmatis con tabla clara de concentracion/tiempo. | No inventar un benchmark proteomico directo. |
| Schubert 2017 y Meyer 2023 muestran fenotipos en BHI en rango de 1 a 10 ug/mL. | Utiles como contexto, no como sustituto del OE1 en CGXII. |
| Radmacher 2005 usa concentraciones mayores y endpoints distintos. | No usar como contradiccion directa de IC50/IC90 del TFDC. |
| Meyer 2023 usa 10 ug/mL durante 4 h en BHI para integridad de envoltura. | Referencia contextual para tratamiento, no decision automatica para OE3. |

## Research/Papers

`Research/Papers/` contiene PDFs fuente asociados al corpus. Se detectaron al menos 62 archivos con nombres compatibles con TB, Mycobacteriales, EMB, C. glutamicum, proteomica o DIA.

Archivos clave detectados por nombre:

| Archivo | Uso probable |
|---|---|
| `Research/Papers/Frey2025_DIA evaluation with CQEs or LFQ.pdf` | Validacion DIA, CQE/LFQ |
| `Research/Papers/radmacher_2005_ethambutol_cglutamicum.pdf` | EMB en C. glutamicum, fisiologia/pared, no benchmark directo de MIC |
| `Research/Papers/schubert_2017_the_antituberculosis_drug_ethambutol_selectively_blocks_apical_growth.pdf` | EMB y crecimiento apical |
| `Research/Papers/meyer_2023_effects_of_benzothiazinone_and_ethambutol_on_the_integrity.pdf` | Integridad de envoltura y EMB |
| `Research/Papers/liang_2025_proteomic_characterization_mycobacterium_tuberculosis_drug_treatment.pdf` | Proteomica y tratamiento en M. tuberculosis |
| `Research/Papers/Global Tuberculosis Report 2025.md` o fuentes GBD/EndTB equivalentes | Contexto epidemiologico, verificar archivo exacto antes de citar |

Regla: para citar en la tesis, abrir la nota del bloque y la fuente concreta. Este indice no reemplaza la verificacion de la cita.

## Presentaciones y dashboards

| Zona | Ruta | Uso |
|---|---|---|
| Guiones de presentacion TFDC | `Tesis/Presentaciones/` | Antecedente discursivo del proyecto; no usar como fuente bibliografica primaria |
| Presentacion 24-04 | `Notes/Presentación 24-04/` | Guion y prompt de slides; util para detectar narrativa, no como dato final |
| Dashboards TB | `Notes/Dashboards/TB Intro 1.2.md`, `Notes/Dashboards/TB Intro 1.3.md` | Estructura y referencias por bloque |
| Esqueleto completo | `Notes/Dashboards/` | Buscar archivo cuyo nombre empieza con `Esqueleto completo de la Introducción` |

## Carpetas descartadas o de baja prioridad

| Ruta | Decision |
|---|---|
| `OBL alimentos/` | Descartada para TFDC; pertenece a proyecto de alimentos/MenoPAUSA |
| `Notes/NotebookLM/menopausa-*` | Descartada para TFDC |
| `Notes/NotebookLM/smoke-*` | Descartada para TFDC |
| `Archive/OBL alimentos*` | Descartada para TFDC |
| `.obsidian/` | Infraestructura del vault, no contenido cientifico |

## Pendientes

1. Completar o localizar corpus especifico para bloques 1.6, 1.7 y 1.8.
2. Verificar si `Research/Papers/liang_2025_proteomic_characterization_mycobacterium_tuberculosis_drug_treatment.pdf` u otras fuentes proteomicas deben convertirse en MD operativo dentro de `bibliografia/`.
3. Decidir como citar datos preliminares del laboratorio usados como motivacion, en especial los 192 cambios proteicos y el 20% del proteoma detectado.
4. Revisar el borrador de introduccion contra este indice antes de seguir redactando.
