---
tipo: resumen_analisis
fecha: 2026-06-29
OE: OE2
estado_dato: analizado
estado_integracion: aislado
fuente_datos:
  - Pairwise_comparison_TripleSTD.xlsx
  - TFold_Analysis_ConParametrosAlejandro_2026-04-17.xlsx
fuente_interpretativa_no_verificada: legacy/analisis_ia_triple_std_dda_resultadoporGPT.txt
script_auditoria: auditoria_triple_std.py
verificacion: recalculado_desde_excel_2026-06-29
estado_comunicacional: interno_no_oficial_no_presentado_tutor
---

# Benchmark TripleSTD DDA, resumen operativo

## Qué es y qué no es

HECHO VERIFICADO (cuaderno de laboratorio): el benchmark TripleSTD es un estándar multiespecie tipo CQE (WISH/humano, *E. coli*, *S. cerevisiae*) mezclado en proporciones conocidas y evaluado primero por DDA. Su función es controlar el flujo de cuantificación antes de trasladar la lógica a DIA.

DECISIÓN CERRADA de encuadre: es avance metodológico preliminar de OE2, no validación DIA y no experimento biológico EMB/control. No reemplaza OE3. La adquisición DIA definitiva no comenzó.

DECISIÓN CERRADA de comunicación: este análisis está auditado como insumo interno de trabajo. No es resultado oficial del TFDC, no fue presentado al tutor como resultado y no debe redactarse como resultado oficial sin una decisión explícita posterior.

Valor metodológico que sí aporta el benchmark, dentro de su alcance DDA:

1. Control de la mezcla: verifica que las proporciones nominales A/B se traduzcan en los fold changes esperados.
2. Control de preparación: gel, FASP, StageTips, desalado y cuantificación sobre extractos de tres organismos.
3. Identificación: cobertura por organismo y FDR de identificación a nivel péptido/proteína.
4. Cuantificación: exactitud del fold change estimado frente al teórico.
5. Dirección del cambio: si el método asigna correctamente el lado del fold change (aumenta vs disminuye).
6. Evaluación de sesgos: especificidad por la fracción invariante (humano), sensibilidad por los organismos diferenciales y comparación entre dos motores de análisis (Pairwise y TFold).

## Diseño y referencia

HECHO VERIFICADO (cuaderno): dos condiciones de mezcla, tres réplicas por condición, motor PatternLab for Proteomics. Top class = Condición A, Bottom class = Condición B (parámetros del Excel TFold).

| Fracción | Condición A | Condición B | FC esperado A/B | log2FC esperado |
|---|---:|---:|---:|---:|
| WISH/humano | 70% | 70% | 1,0 | 0 |
| *E. coli* | 20% | 10% | 2,0 | +1 |
| *S. cerevisiae* | 10% | 20% | 0,5 | -1 |

El humano, invariante por diseño, es la fracción de referencia para estimar el FDR empírico: cualquier proteína humana con log2FC distinto de 0 es, por definición del benchmark, un falso positivo o variabilidad técnica.

## QC de extractos individuales

HECHO VERIFICADO (cuaderno):

| Muestra | Proteínas max parsimony | Espectros identificados | Péptidos identificados | FDR |
|---|---:|---:|---:|---|
| *E. coli* | 1508 | 115436 | 13309 | <1 |
| *S. cerevisiae* | 1122 | 89729 | 10929 | <1 |
| WISH/humano | 2297 | 95165 | 16527 | <1 |

Interpretación: los extractos eran adecuados para sostener un benchmark DDA. Sostiene avance preliminar interno de OE2, no validación DIA ni resultado oficial presentado.

## Métricas recalculadas desde los Excel

HECHO VERIFICADO (recalculado desde los Excel originales el 2026-06-29 con `auditoria_triple_std.py`): las métricas cuantitativas que reportaba el análisis IA fueron reproducidas con los datos crudos. La capa de conteos, medianas y FDR empírico deja de ser preliminar y pasa a dato verificado. Las atribuciones causales siguen siendo inferencia (ver más abajo).

Pairwise (nivel péptido, n = 272 significativas):

| Organismo | n | Mediana log2FC | FC lineal | Esperado log2FC |
|---|---:|---:|---:|---:|
| *E. coli* | 257 | +1,376 | 2,595 | +1,0 |
| *S. cerevisiae* | 13 | -1,145 | 0,452 | -1,0 |
| Humano | 1 | -1,097 | 0,467 | 0 |
| Decoy (Reverse_) | 1 | +1,283 | 2,433 | n/a |

TFold (nivel proteína, 1921 cuantificadas; Blue 546, Green 613, Red 762):

| Categoría | Organismo | n | Mediana log2FC | FC lineal |
|---|---|---:|---:|---:|
| Blue | *E. coli* | 229 | +1,626 | 3,087 |
| Blue | *S. cerevisiae* | 179 | -0,829 | 0,563 |
| Blue | Humano | 138 | -0,252 | 0,840 |
| Green | *E. coli* | 21 | +1,161 | 2,236 |
| Green | *S. cerevisiae* | 32 | -0,473 | 0,721 |
| Green | Humano | 560 | -0,280 | 0,824 |
| Red | *S. cerevisiae* | 15 | -0,069 | 0,954 |
| Red | Humano | 747 | -0,074 | 0,950 |

Totales por organismo (suma Blue+Green+Red): *E. coli* 250, *S. cerevisiae* 226, humano 1445. No hay *E. coli* en Red Dots.

Concordancia y FDR empírico (recalculados):

| Métrica | Valor verificado |
|---|---|
| Pairwise n Blue (overlap) | 215 de 272 (79,0%) |
| Pairwise n Green | 12 |
| Pairwise n Red | 0 |
| Pairwise solo (sin TFold) | 45 |
| FDR empírico Pairwise | 0,37% (1 humano sobre 271 con organismo asignado) |
| FDR empírico TFold Blue | 25,3% (138 humanos sobre 546 Blue) |

NOTA sobre el FDR de Pairwise: además de la única proteína humana, el set significativo de Pairwise contiene una entrada decoy (Reverse_), que es por definición un falso positivo. El FDR empírico de Pairwise sigue siendo bajo, pero la presencia de un decoy en el set significativo conviene reportarla, no omitirla.

## Lo que se puede afirmar sin exagerar

HECHO VERIFICADO: la dirección del cambio es correcta para los organismos diferenciales. Todas las proteínas de *E. coli* del set significativo Pairwise tienen log2FC positivo y todas las de levadura, negativo; en TFold la ausencia de *E. coli* en Red Dots es coherente con esa separación. El flujo DDA/PatternLab discrimina cualitativamente la dirección del cambio en este benchmark.

HECHO VERIFICADO: el fold change de *E. coli* excede sistemáticamente el valor teórico en los dos motores (mediana log2FC +1,376 en Pairwise, FC 2,60; +1,626 en TFold Blue, FC 3,09; esperado +1,0, FC 2,0). La levadura queda más cerca del teórico, con leve sobreestimación del efecto en Pairwise (log2FC -1,145) y atenuación en TFold Blue (log2FC -0,829).

HECHO VERIFICADO: hay un desplazamiento negativo de la fracción humana en TFold Blue (mediana log2FC -0,252), que por diseño debería ser 0. Es evidencia de variabilidad técnica residual o de efecto de la normalización por señal total, no de biología.

## Sesgo de E. coli, formulación cautelosa

INFERENCIA (no cerrada): la sobreestimación del fold change de *E. coli* es compatible con una composición real de la muestra distinta de la nominal, por ejemplo un stock de *E. coli* más concentrado que lo estimado. No debe presentarse como hecho ni con un porcentaje exacto de error de stock sin una cuantificación ortogonal independiente.

Lo que el recálculo sí sostiene, como argumento interno reproducible:

1. La hipótesis de error volumétrico con conservación de volumen total predice para la levadura una proporción del 4% en A y un log2FC de -2,31; el valor observado es -1,145. Esa predicción es incompatible con los datos, así que el error de pipeteo con volumen conservado queda descartado por aritmética del propio benchmark.
2. La consistencia del signo y del orden de magnitud entre Pairwise y TFold, que son motores con lógicas de cuantificación distintas, indica que el sesgo está en los datos y no es un artefacto de un único método.
3. El sesgo de normalización por señal total deprimiría los fold changes de la condición con más masa, no los elevaría; explica el offset humano negativo, pero no origina la sobreestimación de *E. coli*.

Conclusión defendible: el desvío de *E. coli* es real y reproducible; su causa más parsimoniosa es de preparación o cuantificación de la muestra, pero la atribución concreta (magnitud y origen del error de stock) queda PENDIENTE de verificación ortogonal y no se reporta como cifra cerrada.

## Pairwise y TFold, especificidad y sensibilidad

HECHO VERIFICADO: en este benchmark Pairwise es más específico (FDR empírico 0,37%) y TFold más sensible pero menos específico (Blue: sensibilidad 91,6% para *E. coli* y 79,2% para levadura, con FDR empírico 25,3%). La concordancia entre ambos en los hits robustos es alta (79,0%) y ningún hit de Pairwise cae en Red de TFold.

INFERENCIA razonable y alineada con la literatura: el exceso de falsos positivos de TFold sobre la fracción invariante refleja límites estructurales del modo DDA, principalmente la selección estocástica de precursores, los valores faltantes diferenciales entre réplicas y los efectos de corrida, que violan parcialmente los supuestos del control de FDR por Benjamini-Hochberg. No corresponde presentar el 25,3% como propiedad del software, sino como comportamiento esperable de DDA en cuantificación comparativa.

Uso recomendado dentro del TFDC, sin sobreinterpretar: Pairwise para presentar resultados cuantitativos con alto rigor de especificidad; TFold para explorar candidatos priorizando cobertura, asumiendo mayor tasa de falsos positivos. Toda afirmación sobre exactitud cuantitativa absoluta queda condicionada por el sesgo de preparación documentado.

## Conexión con Frey 2025 (acotada)

Frey 2025 respalda dos puntos, y solo esos: que un método de proteómica cuantitativa debe evaluarse por su cuantificación y no solo por identificación, y que las mezclas multiespecie con ratios conocidos (CQE) son el instrumento para hacerlo. Eso encuadra al TripleSTD como CQE legítimo. La expectativa de que DIA reduzca el FDR empírico y la dispersión inter-réplica frente a DDA se apoya en Frey y en los benchmarks que cita, no en este experimento. Frey es preprint no revisado por pares y usa plataformas distintas (Exploris 480, timsTOF HT) del equipo del TFDC (Exploris 240): la lógica es transferible, los parámetros finos no.

## Límites y advertencias

1. El benchmark no demuestra que DIA esté optimizado ni iniciado; es un control DDA previo.
2. Los conteos, medianas y FDR empíricos están verificados contra los Excel; las causas del sesgo de *E. coli* no.
3. No citar la hipótesis del stock de *E. coli* con un porcentaje cerrado sin cuantificación ortogonal.
4. No mezclar este benchmark con el dataset biológico EMB/control, que no existe como adquisición DIA definitiva.
5. Las ventajas de DIA frente a DDA se sostienen con bibliografía (Frey 2025 y los benchmarks que referencia), no solo con este análisis.
6. No presentarlo como resultado oficial ni como resultado comunicado al tutor salvo decisión explícita posterior.

## Pendientes derivados

1. Verificación ortogonal de la composición real de la mezcla (cuantificación absoluta del stock de *E. coli*) si se quiere cerrar la causa del desvío.
2. Trasladar la lógica del benchmark a DIA cuando la adquisición DIA esté disponible, y comparar FDR empírico y CV inter-réplica DDA vs DIA (insumo de OE6).
3. Decidir, antes de cualquier redacción oficial, si las figuras del benchmark (distribuciones log2FC por organismo, Pairwise vs TFold) se integran a la tesis; los datos ya están auditados con `auditoria_triple_std.py`, pero su estado actual es insumo interno.
