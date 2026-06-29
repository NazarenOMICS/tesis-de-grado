---
tipo: indice_corpus_obsidian
version: 1.0
fecha: 2026-06-29
estado_integracion: ruta_auditada_no_correspondiente
ruta_vault_auditada: "C:/Users/Naza/Documents/Obsidian Vault/OBL alimentos"
---

# INDEX corpus Obsidian

## Estado de Fase 8

La ruta auditada fue `C:/Users/Naza/Documents/Obsidian Vault/OBL alimentos`.

Resultado: NO se identifico ahi el corpus bibliografico del TFDC sobre etambutol, Mycobacteriales, Corynebacterium glutamicum, proteomica DIA o introduccion de tesis. Por lo tanto, este indice no habilita todavia la regla de prioridad cientifica del vault para el TFDC.

HECHO VERIFICADO: el vault auditado contiene principalmente material de un obligatorio de alimentos sobre MenoPAUSA, formulacion, inocuidad, HACCP, rotulado, mercado, proceso industrial y fuentes regulatorias alimentarias.

DECISION CERRADA de esta fase: no se copia ni se integra contenido del vault auditado a la bibliografia cientifica del TFDC, porque no corresponde al corpus de investigacion de esta tesis.

PENDIENTE: recibir o localizar la ruta correcta del vault Obsidian del TFDC. Cuando exista, este archivo debe reemplazarse o ampliarse con el mapa real por bloques 1.1 a 1.8.

## Inventario de la ruta auditada

Conteo de archivos:

| Extension | Cantidad |
|---|---:|
| `.md` | 102 |
| `.pdf` | 13 |
| `.docx` | 6 |
| `.png` | 2 |
| `.svg` | 2 |

Carpetas principales detectadas:

| Ruta relativa | Lectura operativa |
|---|---|
| `Alimentos material/` | PDFs regulatorios y materiales de inocuidad alimentaria |
| `citas obl alimentos/` | Citas y auditorias de un trabajo de alimentos |
| `OBL nuevo/` | Desarrollo operativo del obligatorio de alimentos |
| `OBL nuevo/fuentes/` | Resumenes de fuentes regulatorias alimentarias |
| `Old y fuentes/` | Versiones anteriores y fuentes del proyecto MenoPAUSA |

Archivos representativos detectados:

| Archivo | Motivo de descarte para TFDC |
|---|---|
| `PROMPT MAESTRO.md` | Prompt de proyecto alimentario, no del TFDC |
| `Informe DOCS final v1.md` | Informe largo de MenoPAUSA, no tesis EMB/DIA |
| `01 Fase 1 - justificacion inicial fuerte.md` | Justificacion comercial y nutricional de un alfajor funcional |
| `10 Especificacion tecnica del producto.md` | Especificacion de producto alimentario |
| `Seccion 5 - Plan HACCP y prerrequisitos.md` | Inocuidad y HACCP |
| `Alimentos material/` | Reglamentos y manuales de alimentos |

## Busqueda de senales del TFDC

Se busco en archivos de texto del vault auditado con terminos del proyecto: etambutol, ethambutol, Corynebacterium, glutamicum, Mycobacter, tuberculosis, arabinogalactano, arabinosiltransferasa, acidos micolicos, proteomica, proteomica DIA, LC-MS, Orbitrap, DDA, DIA-NN, FASP, StageTips y PatternLab.

Resultado interpretado:

| Categoria | Resultado |
|---|---|
| Etambutol / ethambutol | No se detecto corpus de tesis |
| Corynebacterium glutamicum | No se detecto corpus de tesis |
| Mycobacteriales / tuberculosis / envoltura | No se detecto corpus de tesis |
| Proteomica DIA / LC-MS / Orbitrap | No se detecto corpus de tesis |
| Coincidencias aparentes | Falsos positivos por palabras como "dia" en textos de alimentos o por reglas de escritura generales |

Una coincidencia aislada en `Rules_Of_Writing.md` no constituye corpus cientifico del TFDC. Ese archivo funciona como guia de estilo, no como bibliografia o autoresearch.

## Mapa por bloques de introduccion

Como no se encontro el corpus del TFDC en la ruta auditada, todos los bloques quedan incompletos.

| Bloque | Tema esperado | Estado en la ruta auditada | Accion necesaria |
|---|---|---|---|
| 1.1 | Tuberculosis como problema sanitario | INCOMPLETO | Localizar vault correcto |
| 1.2 | Mycobacteriales y envoltura celular | INCOMPLETO | Localizar vault correcto |
| 1.3 | Etambutol y mecanismo canonico | INCOMPLETO | Localizar vault correcto |
| 1.4 | C. glutamicum como modelo | INCOMPLETO | Localizar vault correcto |
| 1.5 | Proteomica cuantitativa, DDA y DIA | INCOMPLETO | Localizar vault correcto |
| 1.6 | Efectos subletales y respuesta proteomica | INCOMPLETO | Localizar vault correcto |
| 1.7 | Antecedentes del laboratorio y brecha | INCOMPLETO | Localizar vault correcto |
| 1.8 | Justificacion del enfoque experimental | INCOMPLETO | Localizar vault correcto |

## Regla operativa hasta localizar el vault correcto

Para preguntas cientificas, interpretacion de resultados, introduccion o discusion:

1. No usar `C:/Users/Naza/Documents/Obsidian Vault/OBL alimentos` como fuente del TFDC.
2. Usar los MD ya versionados en `bibliografia/`, `proyecto/`, `pasantia/`, `experimentos/` y `estado_actual_tesis.md`.
3. Si se usa conocimiento general del agente, declararlo como complemento no respaldado por el corpus Obsidian del TFDC.
4. Cuando Nazareno indique la ruta correcta, rehacer Fase 8 sobre esa ruta sin modificar el vault.
