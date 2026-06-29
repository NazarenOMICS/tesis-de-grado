---
titulo: "Recommendations for Quantitative DIA Proteomics using Controlled Quantitative Experiments (CQEs)"
autores: "Frey A, Sidgwick F, Porter A, Palmowski P, Trost M"
anio: 2025
fuente: "bioRxiv preprint, doi:10.1101/2025.09.22.677725 (no revisado por pares al momento del resumen)"
tipo: resumen_paper
bloque_tematico: "Proteómica cuantitativa DIA: validación, control de calidad y métricas (alimenta intro DIA vs DDA y metodología OE2/OE3/OE6)"
objetivo_relacionado: "OE2, OE3, OE6"
fuente_pdf: legacy/frey2025_dia_cqe_lfq.pdf
fecha_resumen: 2026-06-29
version: 2.0
lectura_operativa: si
---

# Frey 2025. Recomendaciones para proteómica DIA cuantitativa con CQEs

## Bloque temático

Metodología de proteómica DIA cuantitativa: cómo evaluar y validar la cuantificación, no solo la identificación. Alimenta el bloque de introducción sobre DIA frente a DDA y, sobre todo, la metodología de los OE2 (implementar y validar DIA), OE3 (adquisición DIA) y OE6 (comparación de profundidad DIA vs DDA).

## Aporte central

Propone usar experimentos cuantitativos controlados (CQE): mezclas definidas de proteomas de humano, levadura y bacteria en proporciones conocidas, para medir el desempeño cuantitativo real de un método DIA contra un objetivo esperado. El punto del paper es que la mayoría de los métodos DIA nuevos se evalúan por tasa de identificación, pero rara vez se testea la eficacia de la cuantificación; los CQE llenan ese vacío.

## Diseño y hallazgos

Se corrieron CQE en dos plataformas (Orbitrap Exploris 480 y timsTOF HT) con mezclas multi-especie. La identificación y cuantificación inicial se hizo con DIA-NN, comparando opciones de post-procesamiento. Resultados: más de 10.000 proteínas únicas y más de 160.000 precursores con buena exactitud y precisión. El post-procesamiento tiene impacto fuerte sobre tasa de IDs, precisión y exactitud cuantitativa, y sobre la tasa de cuantificación falsa (FQR), especialmente con bajo input de muestra. En condiciones óptimas de carga, el procesamiento de datos redujo la FQR de ~0,1% a 0% con pérdida mínima de IDs.

## Métricas y conceptos útiles para el TFDC

FQR (false quantitation rate) y BS-FQR (biologically significant false quantitation rate) como medidas de error cuantitativo; CV (coeficiente de variación) para precisión; control de FDR por target-decoy competition (TDC) a nivel PSM. Concepto de compromiso entre gradientes LC cortos (mayor throughput, picos más angostos, exige analizador rápido) y largos (mayor cobertura). Preferencia por LFQ (label-free) por costo y ausencia de límite de número de muestras.

## Relevancia para la justificación metodológica

Da base para justificar, en OE2, los controles, la normalización, la linealidad, la reproducibilidad entre réplicas y los criterios de aceptación del pipeline DIA. El esquema de mezclas multi-especie con ratios conocidos conecta directamente con el trabajo exploratorio de DIA descrito en la pasantía (donde el set multi-especie quedó incompleto por el lisado de levadura). Para OE6, aporta el marco para comparar profundidad y calidad cuantitativa DIA frente a DDA.

## Ambigüedades o límites de uso

1. Es un preprint no revisado por pares; citarlo señalando ese estatus.
2. Las plataformas del paper (Exploris 480 y timsTOF HT) no son idénticas al equipo del TFDC (Orbitrap Exploris 240); las recomendaciones son transferibles en lógica, no necesariamente en parámetros exactos.
3. El paper se centra en la evaluación cuantitativa del método, no en biología del etambutol ni de Mycobacteriales.

## Instrucción para el agente

Usar para OE2, OE3 y OE6 y para la metodología DIA. Priorizarlo al discutir validación cuantitativa, CQE, LFQ, FQR, reproducibilidad y criterios de aceptación del pipeline. Para parámetros finos, abrir el PDF en `legacy/`. El archivo `frey2025_dia_cqe_lfq_copia_setup.md` refiere al mismo paper (PDF idéntico); este es el resumen principal.
