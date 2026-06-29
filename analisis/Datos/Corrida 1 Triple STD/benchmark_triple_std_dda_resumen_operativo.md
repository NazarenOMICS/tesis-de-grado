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
verificacion: no_recalculado_desde_excel
---

# Benchmark TripleSTD DDA, resumen operativo

## Estado

HECHO VERIFICADO: existen archivos de datos de la Corrida 1 Triple STD en esta carpeta: `Pairwise_comparison_TripleSTD.xlsx`, `TFold_Analysis_ConParametrosAlejandro_2026-04-17.xlsx`, `analisis_benchmark_proteomics.docx` y `analisis_benchmark_proteomics_v2.docx`.

HECHO VERIFICADO: se incorporo una interpretacion generada por IA como fuente secundaria en `legacy/analisis_ia_triple_std_dda_resultadoporGPT.txt`.

NO VERIFICADO TODAVIA: los valores cuantitativos del analisis IA no fueron recalculados desde los Excel en esta actualizacion, porque el entorno no tenia libreria de lectura Excel disponible. Usarlos como hipotesis de trabajo o resumen preliminar hasta auditoria formal.

## Diseno experimental

HECHO VERIFICADO por cuaderno de laboratorio: se preparo un benchmark three-species con WISH/humano, E. coli y S. cerevisiae, primero evaluado por DDA antes de trasladar la logica a DIA.

| Fraccion | Condicion A | Condicion B | FC esperado A/B | log2FC esperado |
|---|---:|---:|---:|---:|
| WISH/humano | 70% | 70% | 1,0 | 0 |
| E. coli | 20% | 10% | 2,0 | +1 |
| S. cerevisiae | 10% | 20% | 0,5 | -1 |

Uso correcto: control metodologico de cuantificacion, mezcla, busqueda y analisis diferencial. No es experimento biologico EMB/control y no reemplaza OE3.

## QC de extractos individuales

HECHO VERIFICADO por cuaderno:

| Muestra | Proteinas max parsimony | Espectros identificados | Peptidos identificados | FDR |
|---|---:|---:|---:|---|
| E. coli | 1508 | 115436 | 13309 | <1 |
| S. cerevisiae | 1122 | 89729 | 10929 | <1 |
| WISH/humano | 2297 | 95165 | 16527 | <1 |

Interpretacion: los extractos eran adecuados para seguir con un benchmark DDA. Esto sostiene avance preliminar de OE2, no validacion DIA.

## Resultado preliminar reportado por el analisis IA

Los siguientes valores provienen de `legacy/analisis_ia_triple_std_dda_resultadoporGPT.txt` y deben auditarse contra los Excel antes de integrarlos como resultado final.

| Metodo | Resultado reportado |
|---|---|
| Pairwise | 272 proteinas significativas: 257 E. coli, 13 S. cerevisiae, 1 H. sapiens |
| Pairwise E. coli | mediana log2FC +1,376; FC lineal ~2,60 frente a esperado 2,0 |
| Pairwise S. cerevisiae | mediana log2FC -1,145; cercano a esperado -1 |
| Pairwise Human | 1 proteina, FDR empirico reportado 0,37% sobre fraccion invariante |
| TFold total | 1921 proteinas cuantificadas |
| TFold Blue Dots | 546: 229 E. coli, 179 S. cerevisiae, 138 H. sapiens |
| TFold E. coli | mediana log2FC +1,626; FC lineal ~3,09 frente a esperado 2,0 |
| TFold S. cerevisiae | mediana log2FC -0,829; atenuado frente a esperado -1 |
| TFold Human | mediana log2FC -0,252; FDR empirico reportado 25,3% si Human se toma como invariante |
| Concordancia Pairwise/TFold Blue | 215 proteinas comunes, 79,0% segun analisis IA |

## Interpretacion preliminar

INFERENCIA del analisis IA: la direccion del cambio seria correcta para los organismos diferenciales, con E. coli aumentando y S. cerevisiae disminuyendo. Eso sugiere que el flujo DDA/PatternLab discrimina cualitativamente la direccion de cambios esperados.

INFERENCIA del analisis IA: el fold change de E. coli estaria sobreestimado de forma sistematica. La hipotesis propuesta es una concentracion real del stock de E. coli mayor que la nominal, aproximadamente 30% sobre lo esperado. Esta inferencia no debe presentarse como hecho cerrado sin recalculo.

INFERENCIA del analisis IA: TFold tendria mayor sensibilidad y menor especificidad que Pairwise en este benchmark. Pairwise seria mas conservador para presentar resultados cuantitativos; TFold seria util para exploracion de candidatos, pero con mayor riesgo de falsos positivos.

## Limites y advertencias

1. No usar este benchmark para afirmar que DIA ya fue optimizado.
2. No usar el FDR empirico de TFold como resultado cerrado hasta auditar el Excel.
3. No citar como hecho la hipotesis de stock de E. coli 30% mas concentrado sin recalculo independiente.
4. No mezclar este benchmark con el dataset biologico EMB/control del TFDC, que todavia no existe como adquisicion DIA definitiva.
5. Las afirmaciones sobre ventajas generales de DIA frente a DDA requieren respaldo bibliografico, por ejemplo Frey 2025 u otros papers, no solo este analisis.

## Proximo paso tecnico

Auditar `Pairwise_comparison_TripleSTD.xlsx` y `TFold_Analysis_ConParametrosAlejandro_2026-04-17.xlsx` con un script reproducible que genere:

1. Distribuciones log2FC por organismo.
2. Medianas y dispersion por organismo.
3. Conteos por metodo y categoria.
4. FDR empirico usando Human como fraccion invariante.
5. Comparacion Pairwise vs TFold.
6. Figuras exportables para informe, si el resultado se confirma.
