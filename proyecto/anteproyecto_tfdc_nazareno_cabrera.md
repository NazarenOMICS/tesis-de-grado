---
titulo: "Anteproyecto TFDC: Nuevas perspectivas sobre el efecto biológico del etambutol en Mycobacteriales a partir de proteómica cuantitativa basada en DIA"
tipo: resumen_anteproyecto
fuente_pdf: legacy/anteproyecto_tfdc_nazareno_cabrera.pdf
formulario_origen: "Formulario de Anteproyecto de tesis, Versión 2025 (proyecto/legacy/Formulario de anteproyecto e Informe de avance 1.docx)"
estudiante: "Nazareno Iván Cabrera (286746)"
carrera: "Ingeniería en Biotecnología"
tutor: "Alejandro Leyva (alejandrolp@pasteur.edu.uy), no docente ORT, CV y CI enviados"
lugar: "Unidad de Proteómica y Bioquímica Analíticas (UBYPA), Institut Pasteur de Montevideo"
fecha_comienzo: "03/2026"
fecha_resumen: 2026-06-29
version: 2.0
lectura_operativa: si
nota: "Fuente primaria de hipótesis, objetivo general, los seis OE y el cronograma. Insumo directo para estado_actual_tesis.md (Fase 4)."
---

# Anteproyecto TFDC. Nazareno Cabrera

## Identificación

Título: "Nuevas perspectivas sobre el efecto biológico del etambutol en Mycobacteriales a partir de proteómica cuantitativa basada en adquisición independiente de datos." Estudiante: Nazareno Iván Cabrera (286746), Ingeniería en Biotecnología. Tutor: Alejandro Leyva (no docente ORT). Lugar: UBYPA, Institut Pasteur de Montevideo. Comienzo: 03/2026.

## Hipótesis

La exposición de Corynebacterium glutamicum a concentraciones subinhibitorias de etambutol induce una reprogramación proteómica global que trasciende los procesos asociados a la biosíntesis de la envoltura celular e involucra otros sistemas celulares no descritos previamente para este fármaco.

## Objetivo general

Explorar la existencia de efectos celulares no descritos previamente para el etambutol mediante la caracterización del impacto proteómico global en Corynebacterium glutamicum utilizando proteómica cuantitativa basada en adquisición independiente de datos (DIA).

## Objetivos específicos (literal del anteproyecto)

| OE | Enunciado |
|---|---|
| OE1 | Establecer condiciones experimentales de exposición subinhibitoria al etambutol que permitan evaluar la respuesta celular sin comprometer significativamente la viabilidad bacteriana. |
| OE2 | Implementar y validar una estrategia de adquisición proteómica en modo DIA que permita alcanzar robustez cuantitativa y adecuada cobertura del proteoma de C. glutamicum. |
| OE3 | Obtener perfiles proteómicos de células control y tratadas con etambutol mediante LC-MS/MS en modo DIA. |
| OE4 | Determinar, mediante análisis cuantitativo comparativo, las proteínas cuya abundancia se modifique significativamente tras la exposición al fármaco. |
| OE5 | Realizar un análisis funcional de las proteínas diferencialmente abundantes para determinar los procesos celulares afectados por la exposición al etambutol. |
| OE6 | Evaluar si la estrategia DIA permite una mayor profundidad de cobertura proteómica respecto al enfoque DDA previamente utilizado por el laboratorio. |

La correspondencia OE1 a OE6 coincide con las subcarpetas de `experimentos/` (OE1_MIC_IC50, OE2_validacion_DIA, OE3_adquisicion_DIA, OE4_cuantificacion, OE5_analisis_funcional, OE6_comparacion_DDA).

## Resultados esperados (literal)

1. Optimización de una estrategia de análisis cuantitativo basada en LC-MS/MS en modo DIA.
2. Conjunto de datos proteómicos cuantitativos de C. glutamicum con cobertura y reproducibilidad suficientes para sustentar comparaciones estadísticas entre condiciones control y tratadas con etambutol.
3. Lista de proteínas diferencialmente abundantes, con significancia estadística, en respuesta al etambutol.
4. Lista de procesos biológicos de C. glutamicum afectados por el etambutol en las condiciones estudiadas.
5. Evidencia que permita sustentar o refutar la hipótesis de que el etambutol ejerce efectos celulares más amplios que los clásicamente descritos.

## Cronograma de ejecución (12 meses, Ingeniería)

| Nº | Actividad | Resultado esperado | Meses |
|---|---|---|---|
| 1 | Revisión bibliográfica y diseño experimental | Marco teórico y diseño experimental definitivo | 1 a 3 |
| 2 | Determinación de MIC y condiciones subinhibitorias | Concentración y tiempos definidos | 4 a 5 |
| 3 | Optimización de extracción proteica | Protocolo de preparación de muestras | 5 a 6 |
| 4 | Puesta a punto de la estrategia de adquisición DIA | Método DIA optimizado y parámetros definidos | 6 a 8 |
| 5 | Generación de muestras biológicas | Réplicas listas para análisis | 8 a 9 |
| 6 | Adquisición LC-MS/MS en modo DIA | Datos crudos completos | 9 a 10 |
| 7 | Procesamiento y cuantificación | Matriz proteómica normalizada | 10 a 11 |
| 8 | Comparación con dataset DDA previo | Evaluación de profundidad DIA vs DDA | 11 |
| 9 | Análisis estadístico y funcional | Proteínas reguladas y análisis de enriquecimiento | 11 a 12 |
| 10 | Integración e interpretación biológica | Modelo interpretativo | 11 a 12 |
| 11 | Redacción de tesis | Documento preliminar completo | 11 a 12 |
| 12 | Correcciones finales y defensa | Versión final y defensa | 12 |

## Antecedentes y pertinencia (síntesis por bloques temáticos)

1. Problema de salud pública. Mycobacteriales incluye patógenos de lepra, difteria y tuberculosis. La tuberculosis sigue siendo la principal causa de muerte por un único agente infeccioso, con más de 30 millones de muertes en dos décadas. En Uruguay, 2024: 148 fallecidos, letalidad 10%, mortalidad 4,2 por 100.000, por encima del promedio regional (Comisión Honoraria para la Lucha Antituberculosa). El esquema de primera línea combina isoniazida, rifampicina, pirazinamida y etambutol; la duración prolongada favorece abandono y resistencia. La tuberculosis multirresistente exige esquemas más largos con drogas de segunda línea y más efectos adversos.
2. Mycobacteriales y envoltura celular. Crecimiento polar asimétrico (el polo heredado crece más rápido), con ausencia de varios componentes del elongasoma y divisoma respecto a E. coli y B. subtilis. Pared compleja e impermeable: peptidoglicano unido covalentemente a arabinogalactano esterificado con ácidos micólicos. Rol central en interacción hospedero-patógeno y virulencia, y barrera de resistencia intrínseca.
3. Etambutol: mecanismo clásico y efectos no explicados. Bacteriostático cuyo mecanismo mejor caracterizado es la inhibición de arabinosiltransferasas (síntesis de arabinogalactano). Estos blancos no explican la totalidad de sus efectos ni los mecanismos de resistencia. Estudios por electroforesis bidimensional sugieren alteración del metabolismo intermediario y la respiración. Resultados preliminares en UBYPA (IPMont) por proteómica en C. glutamicum: 192 proteínas diferencialmente expresadas frente al vehículo, ~20% del proteoma detectado, evidenciando dianas aún no identificadas.
4. C. glutamicum como modelo. No patógeno, filogenéticamente emparentado con Mycobacteriales, con la arquitectura general de la envoltura (peptidoglicano, arabinogalactano, ácidos micólicos), manipulable en bioseguridad básica.
5. Proteómica DIA frente a DDA. DDA fragmenta estocásticamente los precursores más abundantes, introduce valores faltantes y limita la reproducibilidad comparativa, subrepresentando proteínas de baja abundancia. DIA fragmenta sistemáticamente todos los precursores en ventanas de m/z predefinidas, reduce valores faltantes y mejora la reproducibilidad cuantitativa. DDA sigue siendo válido y complementario (p. ej. para librerías espectrales). El laboratorio tiene datos DDA previos que sirven de antecedente y referencia comparativa, no de resultado propio del TFDC.

## Decisiones y matices para Fase 4

El anteproyecto plantea condiciones subinhibitorias (OE1). El estado experimental real de OE1 (MIC operativo 2 µg/mL, IC50 ~1 µg/mL, descarte de colonia 3, curva por duplicado con extremos trimmed, análisis de IC50 en GraphPad) debe tomarse de los documentos experimentales y de `estado_actual_tesis.md`, no del anteproyecto, que es el plan inicial. OE2 a OE6 figuran como no iniciados; la adquisición DIA aún no comenzó.

## Ambigüedades o vacíos

1. El anteproyecto fija las condiciones subinhibitorias como objetivo a establecer; los valores concretos de MIC/IC50 son resultado posterior, no constan en el anteproyecto.
2. El cronograma es la planificación a 12 meses; los corrimientos reales respecto del plan deben reflejarse en `estado_actual_tesis.md`, no aquí.
3. Las 22 referencias del anteproyecto (formato IEEE numérico) están en el PDF; si se necesita el detalle bibliográfico exacto, abrir el PDF en `legacy/`.

## Instrucción para el agente

Fuente primaria de hipótesis, objetivo general, los seis OE y el cronograma. Usar como insumo directo de la Fase 4 (`estado_actual_tesis.md`). Si un dato del anteproyecto contradice una decisión experimental posterior, priorizar los documentos experimentales actuales y dejar constancia del cambio. Para el detalle bibliográfico, abrir el PDF en `legacy/`.
