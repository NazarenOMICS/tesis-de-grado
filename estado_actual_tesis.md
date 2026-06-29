---
tipo: estado_actual
version: 1.0
fecha: 2026-06-29
---

# Estado actual del TFDC

## Identificación

Título: "Nuevas perspectivas sobre el efecto biológico del etambutol en Mycobacteriales a partir de proteómica cuantitativa basada en adquisición independiente de datos."

Estudiante: Nazareno Iván Cabrera (286746), Ingeniería en Biotecnología, Universidad ORT Uruguay. Tutor: Alejandro Leyva (no docente de ORT; CV y CI ya enviados). Lugar de realización: Unidad de Bioquímica y Proteómica Analíticas (UBYPA), Institut Pasteur de Montevideo. Comienzo de tesis: 03/2026. Fecha de este estado: 2026-06-29.

Organismo modelo: Corynebacterium glutamicum ATCC 13032 (proxy no patógeno de Mycobacteriales). Fármaco: etambutol (EMB). Tecnología central: proteómica cuantitativa DIA en Orbitrap Exploris 240 acoplado a nano-HPLC UltiMate 3000.

## Antecedentes de pasantía

La pasantía previa en UBYPA dejó operativo un flujo proteómico completo basado en péptidos sobre C. glutamicum: preparación de muestras por FASP-StageTips C18, adquisición en nanoHPLC-Orbitrap Exploris 240 y procesamiento en PatternLab V. Quedó validado además el encadenamiento crecimiento-lisis-preparación-adquisición con lisados propios de C. glutamicum, con SDS-PAGE reproducible entre cultivos.

Fueron exploratorios y no concluyentes el trabajo inicial con DIA (familiarización formativa, sin análisis cuantitativo) y la primera implementación del experimento de perfil térmico del proteoma (TPP), que no mostró precipitación diferencial, con hipótesis principal de interferencia del Triton X-100 del buffer de lisis.

No se retoman en la tesis el experimento de perfil térmico (TPP), el pipeline DDA ni los organismos auxiliares de la pasantía (E. coli, células WISH, S. cerevisiae). La adquisición DIA no fue parte validada de la pasantía: el TFDC la desarrolla de cero (OE2 y OE3). Detalle completo en `pasantia/informe_pasantia_perfil_termico_proteoma.md`.

## Hipótesis, objetivo general y objetivos específicos

Hipótesis: la exposición de C. glutamicum a concentraciones subinhibitorias de etambutol induce una reprogramación proteómica global que trasciende los procesos asociados a la biosíntesis de la envoltura celular e involucra otros sistemas celulares no descritos previamente para este fármaco.

Objetivo general: explorar la existencia de efectos celulares no descritos previamente para el etambutol mediante la caracterización del impacto proteómico global en C. glutamicum utilizando proteómica cuantitativa basada en DIA.

| OE | Enunciado | Estado |
|---|---|---|
| OE1 | Establecer condiciones experimentales de exposición subinhibitoria al etambutol sin comprometer significativamente la viabilidad bacteriana. | COMPLETADO (resultado exploratorio, n=2; ver matices) |
| OE2 | Implementar y validar una estrategia de adquisición proteómica en modo DIA con robustez cuantitativa y cobertura adecuada del proteoma de C. glutamicum. | NO INICIADO |
| OE3 | Obtener perfiles proteómicos de células control y tratadas con EMB mediante LC-MS/MS en modo DIA. | NO INICIADO |
| OE4 | Determinar, por análisis cuantitativo comparativo, las proteínas con abundancia significativamente modificada tras la exposición al fármaco. | NO INICIADO |
| OE5 | Realizar análisis funcional de las proteínas diferencialmente abundantes para determinar los procesos celulares afectados. | NO INICIADO |
| OE6 | Evaluar si la estrategia DIA permite mayor profundidad de cobertura proteómica respecto al enfoque DDA previo del laboratorio. | NO INICIADO |

## Estado por objetivo

### OE1, MIC/IC50: COMPLETADO (con matices)

Qué está cerrado: se caracterizó la respuesta dosis-respuesta de EMB en C. glutamicum ATCC 13032 en medio mínimo CGXII-sacarosa 4% suplementado con DHB y elementos traza (ET), a 30 °C, lectura endpoint por OD595 a las 16 h, según el protocolo v6.0 (10/06/2026). Diseño: microdilución en caldo en placas de 24 pocillos, una placa por colonia como réplica biológica, curva de 14 puntos por diluciones dobles de 64 a 0,0078 µg/mL, dilución seriada directa en placa.

Resultado final (fuente: `experimentos/OE1_MIC_IC50/MIC/MIC Final Analisis/informe_metodologico_mic_emb_final.md` y su PDF):

1. IC50 cercana a 1 µg/mL. Lectura directa: media geométrica R1-R2 = 1,08 µg/mL (R1 0,98; R2 1,18); 4PL de la media = 1,09 µg/mL. Lectura diluida 1:5: media geométrica = 0,98 µg/mL (R1 0,87; R2 1,11); 4PL = 1,01 µg/mL. La diferencia directa vs diluida (~0,1 µg/mL) cae dentro de la resolución del ensayo (grilla 2-fold, n=2). Conclusión defendible: IC50 ~1 µg/mL.
2. Umbral operativo de inhibición >=90% = 2 µg/mL en ambas réplicas conservadas y ambas lecturas. Se reporta como IC90 turbidimétrico operativo, no como MIC microbiológica clásica. La transición de crecimiento a inhibición se ubica en el intervalo (1, 2] µg/mL.

Decisiones de análisis cerradas: el análisis final se restringió al rango informativo 0,125-16 µg/mL y a las réplicas 1 y 2. La réplica 3 (colonia 3) se excluyó por un control positivo comprimido (rango dinámico ~la mitad de R1 y R2) que generó inhibiciones físicamente imposibles en baja concentración (hasta -127% directa, -156% diluida), reproducidas en lectura directa y diluida 1:5; los datos se conservan en la trazabilidad. La exclusión no altera la conclusión (la propia R3 da IC50 1,06-1,11 µg/mL e IC90 2 µg/mL). IC50 estimada por interpolación logarítmica (estimador primario) con 4PL como verificación gráfica.

Qué queda pendiente en OE1:
1. La concentración subinhibitoria concreta a usar como tratamiento en OE3 no está fijada explícitamente en las fuentes cargadas (pendiente de verificar/decidir a partir de IC50 ~1 µg/mL e IC90 ~2 µg/mL).
2. Consolidar el análisis frente a los archivos GraphPad Prism presentes en la carpeta (`MIC analisis graphpad.prism`, `MIC OD 600 BHI.prism`): verificar consistencia entre el informe (interpolación + 4PL) y el Prism. Nota: el prompt maestro indicaba que el archivo de IC50 en GraphPad no estaba en la carpeta; hoy hay archivos .prism, cuya correspondencia exacta con el resultado final está pendiente de verificar.
3. El resultado es exploratorio con n=2 réplicas biológicas; aceptable si se explicita, limitado para incertidumbre formal. No se hizo calibración OD595 vs UFC/mL o peso seco (OD usada como proxy relativo de biomasa).

### OE2 a OE6: NO INICIADO

La adquisición DIA aún no comenzó. No hay datos crudos DIA, ni matriz cuantitativa, ni listas de proteínas diferenciales, ni análisis funcional, ni comparación formal DIA vs DDA. El antecedente DDA del laboratorio (~192 proteínas diferenciales, ~20% del proteoma detectado) es referencia comparativa para OE6, no resultado del TFDC.

## Decisiones experimentales cerradas

Estas decisiones están tomadas y registradas; no se reabren salvo inconsistencia concreta o pedido del estudiante.

1. Formato de placa: placas de 24 pocillos no tratadas, 1 mL por pocillo. Las de 96 pocillos fallan por aireación insuficiente a las velocidades de agitación disponibles; las tratadas causan adhesión celular. (Fuente: decisiones registradas en el prompt maestro; pendiente de cruzar con protocolo v6 para la cita literal.)
2. Inóculo de trabajo a OD 0,1. OD 0,001 y 0,01 no inician crecimiento detectable en CGXII. (Fuente: decisiones registradas en el prompt maestro.)
3. Medio CGXII con elementos traza y DHB como componentes necesarios para crecimiento confiable; ensayo final en CGXII-sacarosa 4%.
4. Control negativo del ensayo con EMB a alta concentración (1024 µg/mL) en lugar de Triton X-100, porque EMB es bacteriostático y no lítico: el control negativo debe aproximar la OD de la biomasa residual del inóculo, no un cero óptico. El control negativo blanco-restado fue ~0,16 en directa, compatible con biomasa residual.
5. Exclusión de la réplica 3 (colonia 3) por control positivo comprimido, decisión de control de calidad documentada por encima del plan del protocolo v6 de combinar las tres réplicas.
6. Análisis con curva por duplicado (R1, R2) y extremos recortados (rango 0,125-16 µg/mL).
7. Terminología: el valor de 2 µg/mL se reporta como IC90 turbidimétrico operativo, no como MIC clásica, por tratarse de inhibición de señal turbidimétrica normalizada con controles propios y no de ausencia de viabilidad.

## Estado de la introducción por bloques

La introducción tiene un borrador preliminar integrado en `redaccion/introduccion/introduccion_borrador_tb_emb_dia.md`. Estado: BORRADOR PRELIMINAR, no texto final. Cubre 1.1 y 1.2 de forma parcial y requiere limpieza, citas y verificación contra el corpus correcto.

Los bloques temáticos identificables a partir de los antecedentes del anteproyecto son:

1. Tuberculosis como problema de salud pública y rol del etambutol en el esquema de primera línea. Material de base disponible (anteproyecto, paper Stuart 2026).
2. Orden Mycobacteriales y particularidad de la envoltura celular (peptidoglicano, arabinogalactano, ácidos micólicos), crecimiento polar asimétrico. Material de base disponible (anteproyecto).
3. Mecanismo clásico del etambutol (inhibición de arabinosiltransferasas) y evidencia de efectos proteoma-globales que lo exceden. Material de base disponible (anteproyecto, informe MIC, antecedente DDA del laboratorio).
4. C. glutamicum como modelo no patógeno emparentado con Mycobacteriales. Material de base disponible (anteproyecto).
5. Proteómica DIA frente a DDA y justificación metodológica. Material de base disponible (anteproyecto, paper Frey 2025).

El mapeo completo de la introducción a la estructura de bloques 1.1 a 1.8 y su corpus de respaldo esta indexado en `bibliografia/INDEX_corpus_obsidian.md`. En Fase 8 se identifico el corpus TFDC dentro de `C:/Users/Naza/Documents/Obsidian Vault`, principalmente en `Notes/NotebookLM/`. Los bloques 1.1 a 1.5 tienen carpetas NotebookLM completas; los bloques 1.6 a 1.8 quedan parciales y deben completarse o verificarse con reviews auxiliares, bibliografia versionada y papers fuente.

## Pendientes globales abiertos

1. OE1: fijar la concentración subinhibitoria de tratamiento para OE3; consolidar IC50/IC90 contra los archivos Prism presentes en la carpeta.
2. OE2 a OE6: no iniciados; la adquisición DIA no ha comenzado.
3. Redacción: introducción en borrador preliminar; materiales y métodos, resultados, discusión y conclusiones no iniciados en `redaccion/`.
4. `AGENTS.md`: completado en Fase 7 y revisado a v2.0 como contrato operativo agente-agente.
5. `bibliografia/INDEX_corpus_obsidian.md`: completado en Fase 8 como indice del corpus Obsidian del TFDC; queda pendiente reforzar bloques 1.6 a 1.8.
6. Verificación de correspondencia entre el informe metodológico de OE1 y los archivos GraphPad Prism.

## Fuentes

Anteproyecto (`proyecto/anteproyecto_tfdc_nazareno_cabrera.md`), informe de pasantía (`pasantia/informe_pasantia_perfil_termico_proteoma.md`), informe metodológico final de OE1 (`experimentos/OE1_MIC_IC50/MIC/MIC Final Analisis/informe_metodologico_mic_emb_final.md` y su PDF), protocolo MIC/IC50 v6 (`experimentos/OE1_MIC_IC50/protocolo_mic_ic50_emb_v6.md`), `INDEX.md` y el prompt maestro (`MEGAPROMPT_cowork_base_tesis.md`).
