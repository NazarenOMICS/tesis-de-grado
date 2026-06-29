---
tipo: resumen_operativo
fuente: legacy/transcripcion_cuaderno_laboratorio_contextualizada.md
fuente_duplicada_txt: legacy/transcripcion_cuaderno_laboratorio_contextualizada.txt
fecha_fuente: 2026-03-12/2026-06-10
fecha_resumen: 2026-06-29
OE: [OE1, OE2]
estado_dato: analizado
estado_integracion: aislado
verificacion: transcripcion_contextualizada_no_pdf_original
---

# Cuaderno de laboratorio, resumen operativo

## Alcance

HECHO VERIFICADO: el cuaderno cubre entradas entre 2026-03-12 y 2026-06-10. La fuente incorporada es una transcripcion contextualizada de un PDF manuscrito exportado desde Supernote. La transcripcion declara que reemplaza lecturas ilegibles o dudosas por reconstrucciones probables segun contexto experimental.

Uso correcto: fuente primaria operativa para reconstruir secuencia de trabajo, decisiones experimentales, preparacion de muestras, controles y cambios de protocolo. No usar como cita bibliografica ni como sustituto de resultados ya consolidados en informes metodologicos.

## Correccion principal del estado del proyecto

El estado anterior "OE2 a OE6 no iniciados" era demasiado grueso. Sigue siendo correcto que la adquisicion DIA definitiva no comenzo, pero no es correcto decir que OE2 no tuvo actividad. OE2 tuvo un inicio metodologico preliminar mediante un benchmark multiespecie evaluado primero por DDA, antes de trasladar la logica a DIA.

Formulacion correcta:

| Objetivo | Estado corregido |
|---|---|
| OE1 | Completado como desarrollo metodologico propio de MIC/IC50/IC90 operativo en CGXII-sacarosa |
| OE2 | Iniciado parcialmente como benchmark cuantitativo DDA previo a DIA; DIA definitiva no iniciada |
| OE3 | No iniciado como set biologico definitivo control vs EMB para DIA |
| OE4 | No iniciado como analisis cuantitativo final de proteinas diferenciales del TFDC |
| OE5 | No iniciado |
| OE6 | No iniciado como comparacion formal DIA vs DDA |

## OE1, desarrollo real del protocolo MIC/IC50

HECHO VERIFICADO: OE1 no fue solo aplicar o ajustar un protocolo. El cuaderno registra un desarrollo metodologico iterativo para medir respuesta de C. glutamicum a EMB en condiciones utiles para la tesis.

Secuencia operacional:

| Fecha | Hecho operativo |
|---|---|
| 2026-04-17 | Primer protocolo MIC OD600 basado en referencia, normalizacion a OD baja, preparacion EMB y lectura planeada a 16 h |
| 2026-04-20 | CGXII sin crecimiento adecuado en ventana experimental; crecimiento tardio con placa seca; se propone bajar volumen y aumentar agitacion |
| 2026-05-01 | Thermomixer genera evaporacion y desgaste de placa; no resuelve crecimiento |
| 2026-05-12/15 | Ensayo con OD final 0,01 y 0,1; no hay crecimiento observable a 16 h |
| 2026-05-21/26 | Placas de 24 pocillos, OD baja, sin crecimiento diferencial; se concluye que OD menor a 0,1 no es suficiente |
| 2026-05-27/28 | Protocolo nuevo con placas de 24 pocillos, OD 0,1 y OD 1, curva 4 a 0,125 ug/mL y controles positivos/negativos |
| 2026-06-09/10 | Preparacion de medios y MIC 6, base del cierre metodologico posterior |

DECISION CERRADA: el resultado defendible de OE1 sigue siendo IC50 cercana a 1 ug/mL e IC90 turbidimetrico operativo de 2 ug/mL, no MIC microbiologica clasica. La replica 3 se excluye por control positivo comprimido segun el informe metodologico final.

INFERENCIA OPERATIVA: no corresponde presentar OE1 como retraso. El anteproyecto ubica la determinacion de MIC y condiciones subinhibitorias en meses 4 a 5 desde inicio 03/2026, y el cierre en 06/2026 cae dentro de ese tramo.

## OE2, benchmark multiespecie previo a DIA

HECHO VERIFICADO: el cuaderno registra preparacion de extractos de E. coli, WISH/humano y S. cerevisiae, gel, FASP, StageTips, desalado, cuantificacion e inyeccion inicial.

Control de calidad de extractos individuales:

| Muestra | Proteinas max parsimony | Espectros identificados | Peptidos identificados | FDR |
|---|---:|---:|---:|---|
| E. coli | 1508 | 115436 | 13309 | <1 |
| S. cerevisiae | 1122 | 89729 | 10929 | <1 |
| WISH/humano | 2297 | 95165 | 16527 | <1 |

HECHO VERIFICADO: se preparo un benchmark con dos condiciones de mezcla y tres replicas por condicion.

| Fraccion | Condicion A | Condicion B | Fold change esperado A/B |
|---|---:|---:|---:|
| WISH/humano | 70% | 70% | 1,0 |
| E. coli | 20% | 10% | 2,0 |
| S. cerevisiae | 10% | 20% | 0,5 |

HECHO VERIFICADO: la preparacion se hizo para 1,5 ug finales por mezcla, con volumen final ajustado para permitir inyeccion. La estrategia se evaluo primero por DDA.

Interpretacion correcta: esto es avance preliminar de OE2, no optimizacion DIA cerrada. Sirve para evaluar mezcla, preparacion, cuantificacion, busqueda y comportamiento de fold changes observados antes de trasladar el enfoque a DIA.

## Extraccion proteica y muestras C. glutamicum

HECHO VERIFICADO: el cuaderno registra un cambio de buffer de lisis para C. glutamicum hacia urea 8 M Tris 100 mM pH 7,5, motivado por interferencias del buffer previo con Triton X-100, lisozima y metodos de cuantificacion. Tambien registra lisis, Qubit, FASP y StageTips de muestras C. glutamicum tratadas o control.

Limite: no formular esto como "optimizacion de extraccion proteica cerrada". La formulacion defendible es preparacion tecnica y evaluacion preliminar de un flujo de lisis/preparacion de muestras. Falta demostrar de forma cerrada recuperacion, reproducibilidad, cobertura y sesgo de proteinas de membrana.

## Implicancias para informe de avance

Frase recomendada:

No se registraron retrasos ni suspension de actividades respecto al cronograma del anteproyecto. La principal dificultad metodologica fue que no existia un protocolo operativo para determinar la respuesta de C. glutamicum al etambutol en las condiciones requeridas por la tesis, por lo que fue necesario desarrollarlo a partir de una referencia inicial mediante iteraciones experimentales. En paralelo, se avanzo de forma preliminar en la puesta a punto cuantitativa mediante un estandar multiespecie tipo Frey, evaluado inicialmente por DDA como control antes de su traslado a DIA.

## Pendientes derivados

1. Fijar concentracion subinhibitoria exacta para OE3.
2. Verificar correspondencia entre informe OE1 y archivos Prism.
3. Recalcular o auditar formalmente el analisis TripleSTD desde los Excel antes de integrarlo como resultado.
4. No presentar el flujo de extraccion como optimizado hasta tener evidencia formal.
5. No presentar adquisicion DIA como iniciada hasta que existan datos crudos DIA.
