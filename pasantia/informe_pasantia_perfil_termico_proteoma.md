---
titulo: "Informe de pasantía: implementación y estandarización de un flujo proteómico y primera aproximación al perfil térmico del proteoma en C. glutamicum"
tipo: resumen_informe_pasantia
fuente_pdf: legacy/informe_pasantia_perfil_termico_proteoma.pdf
estudiante: "Nazareno Iván Cabrera (286746)"
tutor: "Alejandro Leyva"
lugar: "Unidad de Bioquímica y Proteómica Analíticas (UBYPA), Institut Pasteur de Montevideo"
fecha_resumen: 2026-06-29
version: 2.0
lectura_operativa: si
relacion_tfdc: "antecedente metodológico del TFDC, no categoría separada"
---

# Informe de pasantía. Perfil térmico del proteoma en C. glutamicum

## Relación con el TFDC

La pasantía es antecedente metodológico del TFDC activo, no un proyecto externo ni una categoría separada. Aporta la experiencia previa en el flujo proteómico que el TFDC retoma y profundiza. El TFDC cambia el objeto de estudio (efecto del etambutol vía DIA cuantitativa), no continúa el experimento de perfil térmico.

## Contexto y objetivo de la pasantía

Se desarrolló en UBYPA (IPMont), en el marco del proyecto "Identificación de blancos moleculares y mecanismos de acción de compuestos antimicobacterianos mediante el análisis del perfil térmico del proteoma en células intactas". La implementación inicial se centró en estandarizar el flujo proteómico y en una primera aproximación al experimento térmico sobre lisados, como paso previo a una futura implementación en células intactas. Organismo de trabajo: Corynebacterium glutamicum (modelo no patógeno emparentado con Mycobacteriales). Instrumentación: Orbitrap Exploris 240 acoplado a nano-HPLC UltiMate 3000 (ambos Thermo Sc.).

## Qué se hizo y quedó validado

1. Montaje y validación de un flujo proteómico completo basado en péptidos: preparación de muestras por FASP seguido de desalado y concentración en StageTips C18, adquisición en nanoHPLC–Orbitrap y procesamiento bioinformático en PatternLab V. Quedó operativo y reproducible.
2. Prueba de concepto con lisados de C. glutamicum preparados por el laboratorio (réplicas WT3, WT4, WT5, seleccionadas por concentración y patrón SDS-PAGE). Carga objetivo de 25 µg de proteína total por réplica en FASP; pasivación de tubos y filtros con Tween 20 al 5%; digestión con tripsina en relación enzima:sustrato 1:50.
3. Control de desempeño instrumental con estándar BSA (tres corridas) antes de las muestras biológicas. Verificación del pipeline con métricas de identificación coherentes (coberturas de 0,786 y 0,797; 10 y 11 péptidos únicos; 131 y 237 espectros únicos; NSAF ~0,97 en las inyecciones de BSA).
4. Establecimiento de una estrategia reproducible para crecer C. glutamicum y obtener lisados propios: cultivo en BHI, transición a medio mínimo CGXII (con biotina, CaCl2, MgSO4, sacarosa, elementos traza y DHB), lisis mecánica con beads de zirconio en Bullet Blender, cuantificación por Qubit. La caracterización por SDS-PAGE mostró perfiles comparables entre los cuatro cultivos.
5. Verificación de que los lisados propios de C. glutamicum, procesados y adquiridos con el mismo flujo, dieron desempeño consistente con la etapa inicial. Esto valida el encadenamiento completo crecimiento–lisis–preparación–adquisición–procesamiento.

## Qué fue exploratorio (no validado, no concluyente)

1. Trabajo inicial con adquisición independiente de datos (DIA): carácter declarado como exploratorio y formativo. Se trabajó la lógica del método y sus requerimientos operativos, y se adquirieron corridas de E. coli y de células WISH, pero no se realizó análisis cuantitativo formal ni comparaciones biológicas. La puesta a punto de DIA requiere un set completo de mezclas multi-especie en proporciones definidas (incluyendo S. cerevisiae); como el lisado de levadura no resultó adecuado (sin bandas detectables en SDS-PAGE), no se avanzó con la optimización DIA. El cuello de botella identificado fue la preparación de muestra en levadura, no la adquisición instrumental.
2. Primera implementación del experimento de perfil térmico del proteoma sobre lisados, rango 37 a 82 °C en pasos de 5 °C, incubación 3 min a temperatura, 3 min a temperatura ambiente y enfriamiento en hielo, centrifugación a 17.000 g por 45 min a 4 °C, por duplicado. Cuantificación de la fracción soluble por Qubit en diluciones 1/20. El ensayo no mostró precipitación diferencial clara ni tendencia coherente; no fue posible ajustar curva de fusión ni estimar Tm. Hipótesis principal del fallo: interferencia del Triton X-100 del buffer de lisis con la desnaturalización y coagregación térmica. Hipótesis secundaria, de menor peso: centrifugación a 17.000 g frente a ultracentrifugación (~100.000 g) habitual en la literatura, aunque el IPMont obtuvo resultados adecuados con esquemas comparables. No se repitió por limitaciones de tiempo y de muestra.

## Qué NO se retoma en la tesis

1. El experimento de perfil térmico del proteoma (TPP) no forma parte del TFDC. Fue el cierre metodológico de la pasantía y queda como línea a futuro de ese otro proyecto, no del TFDC.
2. El pipeline DDA y las métricas de identificación de la pasantía son antecedente; no son resultados del TFDC.
3. Los organismos E. coli, células WISH y S. cerevisiae se usaron en la pasantía para el contexto de mezclas multi-especie; no son parte del TFDC, centrado en C. glutamicum.

## La adquisición DIA no fue parte de la pasantía (validada)

La adquisición DIA no fue desarrollada ni validada en la pasantía. Lo único que ocurrió con DIA fue una familiarización exploratoria y formativa que no alcanzó la optimización ni produjo datos cuantitativos. El TFDC desarrolla la estrategia DIA de cero como objetivo propio (OE2 implementación y validación de la estrategia DIA, OE3 adquisición LC-MS/MS en modo DIA). Toda referencia a DIA en la pasantía debe leerse como antecedente formativo, no como resultado retomable.

## Datos numéricos y técnicos de referencia

Parámetros de adquisición usados en la pasantía (modo DDA top-20, provistos por A. Leyva): columna analítica PepMap RSLC C18 75 µm x 50 cm a 40 °C; gradiente 1 a 35% B en 150 min y 35 a 99% B en 15 min a 200 nL/min; voltaje de espray 2,0 kV; capilar 250 °C; MS full scan 200 a 2000 m/z, resolución 90000 a 200 m/z; MS/MS resolución 22500 a 200 m/z; HCD con NCE escalonada 25, 30, 35; exclusión dinámica 10 s. Estos parámetros son del flujo DDA de la pasantía y no prejuzgan los del método DIA del TFDC.

## Antecedente conceptual aportado al TFDC

Manejo práctico del instrumento (Orbitrap Exploris 240 + nano-HPLC UltiMate 3000), preparación FASP-StageTips, control de pérdidas por adsorción, criterios de cuantificación peptídica (NanoDrop 215/280 nm y Qubit, con la limitación conocida del Qubit Protein Kit para mezclas peptídicas), definición de carga de inyección (1 µg por corrida), organización trazable de archivos RAW y bases de datos FASTA (UniProt), y procesamiento en PatternLab V (módulo Peptide Spectrum Matching and Filtering, control por FDR).

## Ambigüedades o vacíos

1. El informe describe la cuantificación peptídica con Qubit Protein Kit como operativa, reconociendo que no es exacta para mezclas post-digestión; un método validado (BCA u otro) sería preferible. Queda como nota técnica, no como dato a citar como cuantificación precisa.
2. Los anexos del informe (protocolo FASP-StageTips y guía PatternLab V) están referidos pero su contenido detallado vive en los protocolos de `experimentos/` y `recursos/`, no en este resumen.

## Instrucción para el agente

Usar para reconstruir la experiencia previa y la continuidad técnica hacia el TFDC. Antes de describir la experiencia de laboratorio, consultar este resumen y no inventar tareas, equipos ni resultados. Si un dato no figura, responder "NO CONSTA EN INFORME DE PASANTÍA". Recordar que TPP y DDA son antecedentes, no resultados del TFDC, y que la adquisición DIA no fue parte validada de la pasantía. Para verificación fina, abrir el PDF en `legacy/`.
