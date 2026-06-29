# Formato de protocolo PDF — referencia de estilo

Herramienta: Python + WeasyPrint. El script genera un HTML intermedio y lo convierte a PDF A4.
Ejemplo funcional: `generar_protocolo_mic_ic50_emb_v5.py` (en esta misma carpeta).

---

## Paleta de colores

| Rol | Hex |
|-----|-----|
| Azul oscuro principal | `#173a5e` |
| Azul medio (subtítulo) | `#355977` |
| Texto general | `#22303c` |
| Texto secundario / small | `#5a6b7c` |
| Bordes de tabla | `#c8d0d7` / `#d8dee6` |
| Fondo de tabla par | `#f7f9fb` |
| Fondo card | `#fbfcfe` |
| Fondo plate-wrap | `#f9fbfd` |

---

## Objetos de layout

### Banda de sección `.band`

Barra azul oscura con texto blanco en mayúsculas. Actúa como separador de secciones.

```css
background: #173a5e;
color: white;
font-size: 10.6pt;
font-weight: 700;
text-transform: uppercase;
letter-spacing: 0.25pt;
padding: 6pt 8pt;
border-radius: 3pt;
page-break-after: avoid;
```

### Cards de resumen `.grid-3` / `.grid-2`

Flex row de 2 o 3 tarjetas con borde suave y número grande destacado. Ideales para mostrar parámetros clave de un vistazo.

```html
<div class="grid-3 keep">
  <div class="card">
    <div class="title">Rango ensayado</div>
    <div class="big">4 → 0,125 µg/mL</div>
    <div class="sub">6 puntos · diluciones dobles</div>
  </div>
  ...
</div>
```

### Diagrama de flujo `.flow`

Pasos numerados en flex row con flechas entre ellos. Usa `.stepnum` (círculo azul) + texto descriptivo.

```html
<div class="flow keep">
  <div class="step">
    <div class="stepnum">1</div>
    <div><strong>Preparar</strong><br>descripción corta</div>
  </div>
  <div class="arrow">→</div>
  ...
</div>
```

### Tablas `.tight`

Header azul oscuro, filas alternas en gris claro, padding compacto. `page-break-inside: avoid`.

```html
<table class="tight">
  <thead><tr><th>Col A</th><th>Col B</th></tr></thead>
  <tbody>
    <tr><td>dato</td><td>valor</td></tr>
  </tbody>
</table>
```

### Cajas de nota y advertencia `.note` / `.warn`

- `.note`: borde izquierdo azul, fondo celeste muy claro → información relevante.
- `.warn`: borde izquierdo naranja, fondo amarillo claro → advertencias de procedimiento.

```html
<div class="note"><strong>Nota:</strong> texto informativo.</div>
<div class="warn"><strong>Importante:</strong> advertencia operativa.</div>
```

### Mapa de placa `.plate-wrap`

Contenedor con borde redondeado y fondo claro. Dentro: título `.plate-title`, leyenda `.legend` con puntos `.dot`, y la tabla de pocillos `.plate`.

Los pocillos se renderizan como círculos con gradiente radial según su tipo:

| Clase CSS | Color de fondo | Uso |
|-----------|---------------|-----|
| `.well.dilution` | Azul claro (`#dbeafe`) | Pocillos de la curva EMB |
| `.well.ctrlp` | Verde claro (`#dcfce7`) | Control positivo (ctrl+) |
| `.well.ctrln` | Rojo claro (`#fee2e2`) | Control de inhibición (ctrl−) |
| `.well.blankw` | Gris claro (`#e5e7eb`) | Blanco de medio |

```python
def well(kind: str, label: str) -> str:
    return f'<td><div class="well {kind}"><div>{label}</div></div></td>'

# Tipos: "dilution", "ctrlp", "ctrln", "blankw"
```

### Tabla de metadatos `.meta`

Tabla de 4 columnas (clave–valor × 2), filas alternas, celdas clave en azul. Sirve para el encabezado con versión, organismo, fecha, etc.

```html
<table class="meta">
  <tr>
    <td class="k">Versión</td><td>5.0</td>
    <td class="k">Fecha</td><td>27/05/2026</td>
  </tr>
</table>
```

### Caja de resumen final `.footbox`

Box con borde gris y fondo casi blanco al pie del documento. Resume el protocolo en prosa densa.

### Encabezado de página `@page`

Header automático con WeasyPrint: título a la izquierda, número de página a la derecha. La primera página no lo muestra.

```css
@page {
  size: A4;
  margin: 1.8cm 2.0cm 1.8cm 2.0cm;
  @top-left { content: "Título del protocolo"; font-size: 8pt; color: #516170; }
  @top-right { content: counter(page); font-size: 8pt; color: #516170; }
}
@page:first {
  @top-left { content: none; }
  @top-right { content: none; }
}
```

---

## Dependencias

```bash
pip install weasyprint
```

El script escribe primero el `.html` intermedio y luego lo convierte a `.pdf` con:

```python
from weasyprint import HTML
HTML(string=html, base_url=str(Path.cwd())).write_pdf(OUTPUT_PDF)
```

---

## Convenciones de uso

- Fuente: Arial/Helvetica, 10pt base, 9pt en tablas.
- Español: separador decimal con coma (`0,5`), unidades con espacio fino (`µg/mL`, no `µg/mL`).
- Clase `.keep` en cualquier bloque que no debe partirse entre páginas.
- Nombres de output: `generar_protocolo_<experimento>_v<N>.py` → genera `protocolo_<experimento>_v<N>.pdf`.
