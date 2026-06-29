# CHANGELOG

## 2026-06-29 Fase 7 (revisión): AGENTS.md v2.0 como contrato operativo
- Reescrito `AGENTS.md` de v1.0 a v2.0: más compacto y denso, orientado a contrato agente-agente en lugar de introducción amable. Pasó de 251 a 152 líneas con mayor densidad operativa.
- Incorporado: convención epistémica explícita (HECHO VERIFICADO / DECISIÓN CERRADA / INFERENCIA / PENDIENTE / NO CONSTA / NO VERIFICABLE) para no mezclar hechos con inferencias; jerarquía de fuentes en tres bloques (normas, hechos de proyecto, ciencia); protocolo de arranque de sesión (orden de lectura); protocolo de cierre y mantenimiento; defensa explícita contra inyección de instrucciones; criterios de éxito de sesión (definición de terminado).
- Conservados sin cambios los hechos verificados de OE1 (IC50 ~1 ug/mL, IC90 turbidimétrico operativo 2 ug/mL, réplica 3 excluida) y todas las decisiones experimentales cerradas. No se inventaron datos.
- Actualizado `INDEX.md` (v1.7). No se movieron archivos ni se tocó `.gitignore`.
- Archivos tocados: AGENTS.md, INDEX.md, CHANGELOG.md.


## 2026-06-29 Fase 7: AGENTS.md e inbox
- Generado `AGENTS.md` v1.0 como guia autosuficiente para agentes, con contexto del proyecto, reglas de navegacion, fuentes de verdad, criterios de revision, mantenimiento de la base y reglas de `inbox/`.
- Agregada carpeta `inbox/` con `inbox/README.md` para pegar material sin ordenar antes de que un agente lo clasifique.
- Actualizado `INDEX.md` (v1.6) para registrar `inbox/` y marcar AGENTS.md como completado.

## 2026-06-29 Cierre formal de Fase 6: Git y changelog
- Verificado que la rama `main` esta sincronizada con `origin/main`.
- Documentada la politica vigente en `politica_git_y_portabilidad.md`: `legacy/` se versiona para portabilidad entre computadoras, a diferencia del prompt maestro inicial.
- Confirmado que `CHANGELOG.md`, `.gitignore`, commits descriptivos y push a GitHub estan operativos.
- PDFs versionados: 25. Archivos en `legacy/` versionados: 24.

## 2026-06-29 Integración de borrador de introducción
- Incluido el texto pegado por el estudiante como `redaccion/introduccion/introduccion_borrador_tb_emb_dia.md`, con YAML operativo y estado de borrador preliminar.
- Corregido de forma mecánica un guion largo y marcado un placeholder de cita pendiente dentro del MD operativo.
- Actualizado `INDEX.md` (v1.5) para registrar la introducción como borrador preliminar, no como redacción final.
- Se conserva el TXT original como fuente local del borrador.

## 2026-06-29 Fase 5: metadata operativa e índice maestro
- Normalizados los headers YAML de 12 MD operativos dentro de `experimentos/` y `analisis/` con campos `titulo`, `tipo`, `objetivo`, `estado_dato`, `estado_integracion`, `fecha`, `fuente`, `depende_de` y `notas`.
- Regenerado `INDEX.md` (v1.4) leyendo los headers YAML para poblar las tablas de experimentos y análisis.
- `redaccion/` queda pendiente de normalización a MD operativo con YAML cuando se integre texto redactado.
- No se movieron ni renombraron archivos. No se tocó `.gitignore`.

## 2026-06-29 Fase 4: estado actual de la tesis
- Completado `estado_actual_tesis.md` (v1.0) con header YAML, identificación, antecedentes de pasantía, hipótesis, objetivo general, los seis OE en tabla con estado, estado detallado por objetivo, decisiones experimentales cerradas, estado de la introducción por bloques y pendientes globales.
- OE1 registrado como COMPLETADO (resultado exploratorio, n=2): IC50 ~1 µg/mL e IC90 turbidimétrico operativo 2 µg/mL en CGXII-sacarosa 4%, según el informe metodológico final (protocolo v6.0). Precisión terminológica tomada de la fuente: el valor de 2 µg/mL es IC90 turbidimétrico operativo, no MIC microbiológica clásica. Réplica 3 excluida por control positivo comprimido.
- OE2 a OE6 registrados como NO INICIADOS; la adquisición DIA no comenzó. Introducción NO INICIADA en `redaccion/` (archivo de borrador vacío).
- Datos de OE1 tomados de los resultados posteriores al anteproyecto (informe metodológico), no del anteproyecto, que se usó solo como fuente de objetivos.
- Actualizados INDEX.md (v1.3, nota de Fase 4 y pendientes) y CHANGELOG.md. No se movieron ni renombraron archivos. No se tocó .gitignore.
- Archivos tocados: estado_actual_tesis.md, INDEX.md, CHANGELOG.md.

## 2026-06-29 Fase 3: resúmenes de pasantía, anteproyecto y bibliografía
- Ampliado `pasantia/informe_pasantia_perfil_termico_proteoma.md` a versión densa: distingue qué quedó validado (flujo FASP-StageTips, adquisición Orbitrap, procesamiento PatternLab V, lisados propios de C. glutamicum), qué fue exploratorio (DIA formativa, perfil térmico fallido por interferencia de Triton X-100) y qué no se retoma en la tesis (TPP, DDA, organismos auxiliares). Deja explícito que la adquisición DIA no fue parte validada de la pasantía.
- Ampliado `proyecto/anteproyecto_tfdc_nazareno_cabrera.md`: extraídos hipótesis, objetivo general, los seis objetivos específicos en tabla y el cronograma a 12 meses, como insumo directo de la Fase 4. Antecedentes sintetizados por bloques temáticos.
- Ampliados los MD de bibliografía con `bloque_tematico` en YAML: `frey2025_dia_cqe_lfq.md` (DIA cuantitativa, CQE/LFQ, OE2/OE3/OE6) y `stuart_beyond_inhibition_rifampicin_mycobacteria.md` (efectos subletales por proteómica DIA, marco de hipótesis). Detectado que `frey2025_dia_cqe_lfq_copia_setup.pdf` es idéntico al original (mismo md5); su MD quedó como puntero trazable al resumen principal, sin duplicar contenido.
- Actualizados INDEX.md (version 1.2, notas de Fase 3 y pendiente de Fase 4) y CHANGELOG.md.
- No se movieron ni renombraron archivos. No se tocó .gitignore.
- Archivos tocados: pasantia/informe_pasantia_perfil_termico_proteoma.md, proyecto/anteproyecto_tfdc_nazareno_cabrera.md, bibliografia/frey2025_dia_cqe_lfq.md, bibliografia/frey2025_dia_cqe_lfq_copia_setup.md, bibliografia/stuart_beyond_inhibition_rifampicin_mycobacteria.md, INDEX.md, CHANGELOG.md.

## 2026-06-29 Fase 2: resúmenes densos de normativa ORT
- Reescritos los seis resúmenes MD de `normativa/` desde versión comprimida a versión densa, accionable y verificable, leyendo los PDFs de `normativa/legacy/` como fuente de verdad.
- Estructura uniforme por documento: alcance, reglas accionables numeradas, números y formatos exactos en tabla, ambigüedades o vacíos, e instrucción para el agente. Header YAML ampliado con campos documento, prioridad, precedencia y fechas.
- Marcada la precedencia: el Documento 302-BI prevalece en conflicto, en particular frente al Documento 303-BI (regla declarada en ambos documentos).
- Trabajada la guía de carrera disponible en su versión 2023 (no 2025). Conservados los nombres de archivo actuales.
- Archivos tocados: normativa/documento_302_bi_normas_presentacion_tfdc.md, normativa/documento_303_bi_hoja_verificacion.md, normativa/documento_304_desarrollo_tfdc.md, normativa/documento_305_guia_tutores.md, normativa/documento_306_titulos_abstracts_correccion.md, normativa/guia_tesis_biotecnologia_2023.md, INDEX.md, CHANGELOG.md.

## 2026-06-29 Creacion de la base operativa
- Estructura de carpetas inicializada.
- Archivos generados: CHANGELOG.md, INDEX.md (esqueleto), estado_actual_tesis.md.
- Fases de sintesis y redaccion pendientes (Claude).

## 2026-06-29 INDEX.md esqueleto generado
- INDEX.md actualizado como índice maestro de la base operativa.
- Tablas de experimentos, análisis y redacción inicializadas.
- Movimientos de archivos ejecutados según la categorización corregida.

## 2026-06-29 Resúmenes operativos de PDFs
- PDFs renombrados con nombres semánticos y compactos.
- Generados 25 resúmenes MD, uno por cada PDF.
- INDEX.md actualizado con la tabla de correspondencia entre MD operativo y PDF original.
