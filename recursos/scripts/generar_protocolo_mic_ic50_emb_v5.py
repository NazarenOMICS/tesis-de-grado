#!/usr/bin/env python3
"""
Genera el PDF v5 del protocolo MIC/IC50 de etambutol en C. glutamicum.

Diseño v5:
- 2 placas de 24 pocillos, disposición idéntica, inóculo distinto:
    Placa 1 → OD595 final = 1,0  (suspensión siembra OD595 = 2,0)
    Placa 2 → OD595 final = 0,1  (suspensión siembra OD595 = 0,2)
- Filas A, B, C: curva de 6 concentraciones en triplicado (dilución seriada por columnas)
- Fila D: 2 ctrl+  (D1-D2) | 2 ctrl-  (D3-D4, 500 µL EMB 2048 µg/mL) | 2 blancos (D5-D6)
- Dilución seriada directa en placa, por columnas (1→2→3→4→5→6)

Requisitos:
    pip install weasyprint

Uso:
    python generar_protocolo_mic_ic50_emb_v5.py

Salida:
    protocolo_mic_ic50_emb_cglutamicum_v5.pdf
"""

from __future__ import annotations

from pathlib import Path
from textwrap import dedent

try:
    from weasyprint import HTML
except ImportError as exc:
    raise SystemExit(
        "Falta instalar WeasyPrint. Instalalo con: pip install weasyprint"
    ) from exc

OUTPUT_PDF = Path("protocolo_mic_ic50_emb_cglutamicum_v5.pdf")
OUTPUT_HTML = Path("protocolo_mic_ic50_emb_cglutamicum_v5.html")

# Concentraciones finales (tras inóculo 1:1)
CONCS_FINAL = ["4", "2", "1", "0,5", "0,25", "0,125"]
# Concentraciones 2× antes del inóculo (lo que queda en el pocillo tras la dilución seriada)
CONCS_2X = ["8", "4", "2", "1", "0,5", "0,25"]


# ---------------------------------------------------------------------------
# Componentes HTML
# ---------------------------------------------------------------------------

def well(kind: str, label: str) -> str:
    return f'<td><div class="well {kind}"><div>{label}</div></div></td>'


def plate_html() -> str:
    """
    Mapa de placa 24 pocillos.
    Filas A, B, C → triplicado de 6 concentraciones (col 1-6).
    Fila D         → ctrl+, ctrl+, ctrl−, ctrl−, blanco, blanco.
    """
    dil = [f"{c}<br>µg/mL" for c in CONCS_FINAL]
    ctrl_row = ["ctrl+", "ctrl+", "ctrl−", "ctrl−", "blanco", "blanco"]

    rows_data = [dil, dil, dil, ctrl_row]
    row_names = ["A", "B", "C", "D"]

    html = [
        '<table class="plate">',
        '<tr><th></th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th></tr>',
    ]
    for row_name, row in zip(row_names, rows_data):
        html.append("<tr>")
        html.append(f'<td class="rowlab">{row_name}</td>')
        for label in row:
            if "µg/mL" in label:
                html.append(well("dilution", label))
            elif label == "ctrl+":
                html.append(well("ctrlp", label))
            elif label == "blanco":
                html.append(well("blankw", label))
            else:
                html.append(well("ctrln", label))
        html.append("</tr>")
    html.append("</table>")
    return "\n".join(html)


def vol_table_html() -> str:
    """Tabla de volúmenes totales a preparar para las 2 placas."""
    rows = [
        # (Reactivo, Descripción/uso, Vol. mínimo, Vol. recomendado)
        ("CGXII", "Serie EMB — 18 poc × 500 µL × 2 placas", "18 mL", ""),
        ("", "ctrl+ (D1-D2) — 2 poc × 500 µL × 2 placas", "2 mL", ""),
        ("", "Blancos (D5-D6) — 2 poc × 1 000 µL × 2 placas", "4 mL", ""),
        ("", "<strong>Total CGXII</strong>", "<strong>24 mL</strong>", "<strong>30 mL</strong>"),
        ("EMB 16 µg/mL<br><small>(working stock serie)</small>",
         "Col 1 (A1, B1, C1) — 3 poc × 500 µL × 2 placas", "3 mL", "5 mL"),
        ("EMB 2048 µg/mL<br><small>(ctrl−, sin diluir)</small>",
         "D3, D4 — 2 poc × 500 µL × 2 placas", "2 mL", "3 mL"),
        ("Inóculo OD595 = 2,0<br><small>(Placa 1, OD final = 1,0)</small>",
         "22 poc activos × 500 µL", "11 mL", "15 mL"),
        ("Inóculo OD595 = 0,2<br><small>(Placa 2, OD final = 0,1)</small>",
         "22 poc activos × 500 µL", "11 mL", "15 mL"),
    ]

    html = [
        '<table class="tight">',
        '<thead><tr>',
        '<th>Reactivo</th><th>Uso / detalle</th>',
        '<th style="text-align:center">Vol. mínimo</th>',
        '<th style="text-align:center">Vol. recomendado</th>',
        '</tr></thead><tbody>',
    ]
    for reactivo, uso, vmin, vrec in rows:
        html.append(
            f'<tr><td>{reactivo}</td><td>{uso}</td>'
            f'<td style="text-align:center">{vmin}</td>'
            f'<td style="text-align:center">{vrec}</td></tr>'
        )
    html.append("</tbody></table>")
    return "\n".join(html)


def dil_series_table_html() -> str:
    """Tabla de la cadena de dilución seriada: concentraciones 2× y finales."""
    html = [
        '<table class="tight">',
        '<thead><tr>',
        '<th>Columna</th>',
        '<th>Poc. (filas A-C)</th>',
        '<th>Conc. 2× antes del inóculo</th>',
        '<th>Conc. final (tras inóculo 1:1)</th>',
        '</tr></thead><tbody>',
    ]
    for i, (c2x, cf) in enumerate(zip(CONCS_2X, CONCS_FINAL), start=1):
        html.append(
            f'<tr><td style="text-align:center">{i}</td>'
            f'<td style="text-align:center">A{i}, B{i}, C{i}</td>'
            f'<td style="text-align:center">{c2x} µg/mL</td>'
            f'<td style="text-align:center">{cf} µg/mL</td></tr>'
        )
    html.append("</tbody></table>")
    return "\n".join(html)


# ---------------------------------------------------------------------------
# HTML completo
# ---------------------------------------------------------------------------

def build_html() -> str:
    plate = plate_html()
    vol_table = vol_table_html()
    dil_table = dil_series_table_html()

    return dedent(f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
    <meta charset="utf-8">
    <title>Protocolo MIC/IC50 EMB v5</title>
    <style>
      @page {{
        size: A4;
        margin: 1.8cm 2.0cm 1.8cm 2.0cm;
        @top-left {{
          content: "Protocolo MIC/IC50 - Etambutol en C. glutamicum ATCC 13032";
          font-family: Arial, Helvetica, sans-serif;
          font-size: 8pt;
          color: #516170;
        }}
        @top-right {{
          content: counter(page);
          font-family: Arial, Helvetica, sans-serif;
          font-size: 8pt;
          color: #516170;
        }}
      }}
      @page:first {{
        @top-left {{ content: none; }}
        @top-right {{ content: none; }}
      }}
      body {{
        font-family: Arial, Helvetica, sans-serif;
        color: #22303c;
        font-size: 10pt;
        line-height: 1.28;
        margin: 0;
      }}
      h1 {{
        margin: 0 0 5pt 0;
        font-size: 19pt;
        line-height: 1.14;
        color: #173a5e;
      }}
      .subtitle {{
        font-size: 11.3pt;
        color: #355977;
        font-weight: 700;
        padding-bottom: 7pt;
        border-bottom: 1.4pt solid #173a5e;
        margin-bottom: 10pt;
      }}
      .meta {{ width: 100%; border-collapse: separate; border-spacing: 0; margin: 7pt 0 12pt 0; font-size: 9.1pt; }}
      .meta td {{ padding: 5pt 7pt; border: 0.6pt solid #d8dee6; }}
      .meta tr:nth-child(odd) td {{ background: #f6f8fb; }}
      .meta .k {{ width: 20%; font-weight: 700; color: #173a5e; }}
      .band {{
        background: #173a5e;
        color: white;
        font-size: 10.6pt;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.25pt;
        padding: 6pt 8pt;
        margin: 13pt 0 7pt 0;
        border-radius: 3pt;
        page-break-after: avoid;
      }}
      h3 {{ color: #173a5e; margin: 10pt 0 4pt 0; font-size: 10pt; page-break-after: avoid; }}
      p {{ margin: 0 0 7pt 0; }}
      .grid-3 {{ display: flex; gap: 8pt; margin: 7pt 0 8pt 0; }}
      .grid-2 {{ display: flex; gap: 8pt; margin: 7pt 0 8pt 0; }}
      .card {{ flex: 1; border: 0.8pt solid #d9e0e7; border-radius: 8pt; padding: 8pt; background: #fbfcfe; }}
      .card .title {{ color: #173a5e; font-weight: 700; margin-bottom: 4pt; font-size: 9pt; }}
      .card .big {{ font-size: 13pt; font-weight: 700; color: #0e4d7a; }}
      .card .sub {{ font-size: 8.6pt; color: #5a6b7c; margin-top: 2pt; }}
      .small {{ font-size: 8.6pt; color: #5a6b7c; }}
      .flow {{ margin: 9pt 0 11pt 0; display: flex; align-items: stretch; gap: 5pt; font-size: 8.5pt; }}
      .step {{ flex: 1; border: 0.8pt solid #dce3ea; border-radius: 8pt; padding: 7pt; background: linear-gradient(180deg, #ffffff, #f6f9fc); }}
      .stepnum {{ display: inline-block; width: 17pt; height: 17pt; line-height: 17pt; text-align: center; border-radius: 50%; background: #173a5e; color: white; font-weight: 700; margin-bottom: 4pt; }}
      .arrow {{ font-size: 11pt; color: #90a2b5; padding-top: 18pt; }}
      table {{ width: 100%; border-collapse: collapse; margin: 7pt 0 10pt 0; font-size: 9pt; page-break-inside: avoid; }}
      th {{ background: #173a5e; color: white; padding: 5pt 6pt; border: 0.5pt solid #c8d0d7; text-align: left; }}
      td {{ border: 0.5pt solid #c8d0d7; padding: 5pt 6pt; vertical-align: top; }}
      tbody tr:nth-child(even) {{ background: #f7f9fb; }}
      .tight th, .tight td {{ padding: 4pt 5pt; }}
      .note, .warn {{ padding: 7pt 9pt; margin: 7pt 0 9pt 0; border-radius: 6pt; font-size: 9pt; page-break-inside: avoid; }}
      .note {{ border-left: 3pt solid #173a5e; background: #f3f6fa; }}
      .warn {{ border-left: 3pt solid #e08600; background: #fff7ed; }}
      .plate-wrap {{ border: 1pt solid #d6dde5; border-radius: 12pt; padding: 10pt 10pt 6pt 10pt; background: #f9fbfd; margin: 7pt 0 8pt 0; page-break-inside: avoid; }}
      .plate-title {{ color: #173a5e; font-weight: 700; margin-bottom: 7pt; font-size: 10pt; }}
      .legend {{ margin-bottom: 8pt; font-size: 8.5pt; }}
      .legend span {{ display: inline-block; margin-right: 9pt; margin-bottom: 3pt; }}
      .dot {{ display: inline-block; width: 10pt; height: 10pt; border-radius: 50%; margin-right: 4pt; vertical-align: middle; }}
      .dil {{ background: #dbeafe; border: 0.8pt solid #93c5fd; }}
      .pos {{ background: #dcfce7; border: 0.8pt solid #86efac; }}
      .neg {{ background: #fee2e2; border: 0.8pt solid #fca5a5; }}
      .blank {{ background: #e5e7eb; border: 0.8pt solid #cbd5e1; }}
      .plate {{ width: 100%; border-collapse: separate; border-spacing: 4pt; table-layout: fixed; margin: 0; }}
      .plate th {{ background: transparent; color: #526476; border: none; text-align: center; padding: 0 0 1pt 0; font-size: 8.3pt; }}
      .plate .rowlab {{ width: 14pt; font-weight: 700; color: #526476; text-align: center; border: none; background: transparent; padding: 0; }}
      .plate td {{ border: none; background: transparent; padding: 0; text-align: center; vertical-align: middle; }}
      .well {{ width: 68pt; height: 68pt; border-radius: 50%; border: 1pt solid #b6c4d3; display: table; margin: 0 auto; box-shadow: inset 0 0 0 4.5pt rgba(255,255,255,0.65); }}
      .well > div {{ display: table-cell; vertical-align: middle; text-align: center; padding: 3.5pt; font-size: 7.3pt; line-height: 1.12; font-weight: 700; color: #18324b; }}
      .well.dilution {{ background: radial-gradient(circle at 35% 30%, #ffffff, #dbeafe 70%); }}
      .well.ctrlp {{ background: radial-gradient(circle at 35% 30%, #ffffff, #dcfce7 70%); }}
      .well.ctrln {{ background: radial-gradient(circle at 35% 30%, #ffffff, #fee2e2 70%); }}
      .well.blankw {{ background: radial-gradient(circle at 35% 30%, #ffffff, #e5e7eb 70%); }}
      ol, ul {{ margin: 5pt 0 9pt 18pt; }}
      li {{ margin-bottom: 3pt; }}
      .footbox {{ margin-top: 10pt; padding: 8pt 9pt; border: 0.8pt solid #d8dee6; border-radius: 8pt; background: #fafcfe; font-size: 8.9pt; }}
      em {{ font-style: italic; }}
      .keep {{ page-break-inside: avoid; }}
      .plate-badge {{
        display: inline-block;
        background: #173a5e;
        color: white;
        border-radius: 4pt;
        padding: 2pt 6pt;
        font-size: 8pt;
        font-weight: 700;
        margin-right: 6pt;
        vertical-align: middle;
      }}
      small {{ font-size: 8pt; color: #5a6b7c; }}
    </style>
    </head>
    <body>
      <h1>Determinación de MIC e IC50 de etambutol en <em>Corynebacterium glutamicum</em> ATCC 13032</h1>
      <div class="subtitle">Microdilución en caldo · Placa de 24 pocillos · Dilución seriada por columnas · Triplicado · Lectura espectrofotométrica a OD595</div>

      <table class="meta">
        <tr><td class="k">Versión</td><td>5.0</td><td class="k">Fecha</td><td>27/05/2026</td></tr>
        <tr><td class="k">Organismo</td><td><em>C. glutamicum</em> ATCC 13032</td><td class="k">Fármaco</td><td>Etambutol dihidrocloruro (EMB)</td></tr>
        <tr><td class="k">Medio</td><td>CGXII-sacarosa 4% suplementado con DHB y ET</td><td class="k">Diseño</td><td>2 placas · 6 puntos · triplicado · 2 densidades de inóculo</td></tr>
      </table>

      <div class="band">Fundamento y objetivo</div>
      <p>El ensayo determina la concentración mínima inhibitoria (MIC) y la concentración inhibitoria media (IC50) del etambutol sobre <em>C. glutamicum</em> ATCC 13032 en medio mínimo CGXII. La lectura final se realiza por OD595 y se interpreta como indicador de crecimiento bacteriano.</p>
      <p>En esta versión se comparan dos densidades de inóculo (OD595 final = 1,0 y OD595 final = 0,1) para evaluar el efecto del tamaño del inóculo sobre la curva concentración-respuesta. El ctrl− (EMB 2048 µg/mL directamente, concentración final 1024 µg/mL) valida la inhibición completa y <strong>no</strong> se incluye en el ajuste de la curva IC50.</p>

      <div class="grid-3 keep">
        <div class="card">
          <div class="title">Rango ensayado</div>
          <div class="big">4 → 0,125 µg/mL</div>
          <div class="sub">6 puntos · diluciones dobles</div>
        </div>
        <div class="card">
          <div class="title">Volumen final por pocillo</div>
          <div class="big">1 000 µL</div>
          <div class="sub">500 µL EMB/medio + 500 µL inóculo</div>
        </div>
        <div class="card">
          <div class="title">Placas · Réplicas</div>
          <div class="big">2 placas</div>
          <div class="sub">Pl. 1: OD final 1,0 · Pl. 2: OD final 0,1<br>Triplicado interno (filas A, B, C)</div>
        </div>
      </div>

      <div class="flow keep">
        <div class="step"><div class="stepnum">1</div><div><strong>Preparar</strong><br>stocks de EMB, medio e inóculos (OD = 2,0 y 0,2)</div></div><div class="arrow">→</div>
        <div class="step"><div class="stepnum">2</div><div><strong>Cargar placa</strong><br>500 µL CGXII en A1-C6, controles en fila D</div></div><div class="arrow">→</div>
        <div class="step"><div class="stepnum">3</div><div><strong>Dilución seriada</strong><br>col 1 → 2 → 3 → 4 → 5 → 6 (en paralelo filas A-C)</div></div><div class="arrow">→</div>
        <div class="step"><div class="stepnum">4</div><div><strong>Inocular y leer</strong><br>T0, incubar 16 h, leer OD595 final</div></div>
      </div>

      <div class="band">Parámetros del experimento</div>
      <table class="tight"><thead><tr><th>Parámetro</th><th>Valor</th></tr></thead><tbody>
        <tr><td>Cepa</td><td><em>C. glutamicum</em> ATCC 13032</td></tr>
        <tr><td>Placa</td><td>24 pocillos, fondo plano, transparente</td></tr>
        <tr><td>Número de placas</td><td>2 (Placa 1: OD595 final = 1,0 · Placa 2: OD595 final = 0,1)</td></tr>
        <tr><td>Diseño por placa</td><td>6 concentraciones × triplicado (filas A, B, C) + 2 ctrl+ + 2 ctrl− + 2 blancos</td></tr>
        <tr><td>Pocillos activos por placa</td><td>22 (18 curva + 2 ctrl+ + 2 ctrl−); 2 blancos sin bacteria</td></tr>
        <tr><td>ctrl+ (D1, D2)</td><td>Bacteria + medio sin EMB</td></tr>
        <tr><td>Blanco (D5, D6)</td><td>Medio sin bacteria</td></tr>
        <tr><td>ctrl− (D3, D4)</td><td>Bacteria + 500 µL EMB 2048 µg/mL → EMB final 1024 µg/mL</td></tr>
        <tr><td>Lecturas</td><td>OD595 en T0 y Tf</td></tr>
        <tr><td>Agitación</td><td>Shaker orbital New Brunswick, 240 rpm, órbita 19 mm</td></tr>
        <tr><td>Temperatura</td><td>30 °C</td></tr>
        <tr><td>Tiempo de incubación</td><td>16 h (aceptable: 15-17 h)</td></tr>
      </tbody></table>

      <div class="band">Volúmenes totales a preparar (2 placas)</div>
      <p>Preparar con tiempo suficiente antes de armar las placas. Los volúmenes recomendados incluyen margen de muerto de pipeteo.</p>
      {vol_table}
      <div class="note"><strong>Nota:</strong> los inóculos de Placa 1 y Placa 2 se preparan por separado y no se mezclan. Los blancos (D5, D6) no reciben bacteria; su volumen final es 1 000 µL de CGXII solo.</div>

      <div class="band">Disposición de la placa (idéntica para ambas placas)</div>
      <div class="plate-wrap">
        <div class="plate-title">Mapa de placa 24 pocillos · concentraciones finales en el ensayo</div>
        <div class="legend">
          <span><span class="dot dil"></span>Curva EMB (triplicado)</span>
          <span><span class="dot pos"></span>ctrl+ (crecimiento sin droga)</span>
          <span><span class="dot blank"></span>Blanco (medio solo)</span>
          <span><span class="dot neg"></span>ctrl− (EMB 1024 µg/mL final)</span>
        </div>
        {plate}
      </div>
      <div class="note"><strong>Dirección de la dilución seriada:</strong> columna 1 → columna 2 → … → columna 6, realizando la transferencia simultáneamente en las tres filas (A, B, C). La disposición de la placa es idéntica para ambas placas; la única diferencia es la OD del inóculo.</div>

      <div class="band">Cadena de dilución seriada</div>
      {dil_table}
      <div class="note">El working stock para la columna 1 se prepara a <strong>16 µg/mL</strong> en CGXII. Al agregarse 500 µL de ese stock sobre los 500 µL de medio ya cargados en col 1, la concentración en el pocillo pasa a 8 µg/mL (2×). Tras el inóculo 1:1, la concentración final es 4 µg/mL.</div>

      <table class="tight"><thead><tr><th>Tipo de pocillo</th><th>Carga previa al inóculo</th><th>Agregado posterior</th><th>Resultado final</th></tr></thead><tbody>
        <tr><td>Serie EMB (A1-C6)</td><td>500 µL de CGXII en cada pocillo; col 1 recibe además 500 µL de EMB 16 µg/mL (quedan 1 000 µL a 8 µg/mL); se hace dilución seriada por columnas hasta col 6 y se descartan 500 µL de col 6</td><td>500 µL de inóculo</td><td>4 → 0,125 µg/mL (col 1 → col 6)</td></tr>
        <tr><td>ctrl+ (D1, D2)</td><td>500 µL de CGXII</td><td>500 µL de inóculo</td><td>Crecimiento sin droga</td></tr>
        <tr><td>Blanco (D5, D6)</td><td>1 000 µL de CGXII</td><td>No lleva inóculo</td><td>Control de fondo</td></tr>
        <tr><td>ctrl− (D3, D4)</td><td>500 µL de EMB 2048 µg/mL (sin diluir)</td><td>500 µL de inóculo</td><td>EMB final 1 024 µg/mL</td></tr>
      </tbody></table>

      <div class="band">Reactivos y soluciones a preparar</div>
      <h3>1. Stock primario de EMB</h3>
      <p>Disolver etambutol dihidrocloruro en agua MQ estéril hasta <strong>2048 µg/mL</strong>. Filtrar por 0,22 µm, alicuotar y conservar a −20 °C. Este stock se usa directamente para los pocillos ctrl−.</p>
      <h3>2. Working stock para la serie en placa (16 µg/mL)</h3>
      <p>Diluir el stock primario en CGXII hasta 16 µg/mL. Preparar al menos <strong>5 mL</strong> para cubrir col 1 de las 2 placas (3 poc × 500 µL × 2 = 3 mL) y el muerto de pipeteo.</p>
      <h3>3. Inóculos bacterianos</h3>
      <p>Preparar dos suspensiones de siembra independientes en CGXII:</p>
      <ul>
        <li><strong>Placa 1:</strong> OD595 = 2,0 → concentración final en pocillo OD595 = 1,0. Preparar al menos <strong>15 mL</strong>.</li>
        <li><strong>Placa 2:</strong> OD595 = 0,2 → concentración final en pocillo OD595 = 0,1. Preparar al menos <strong>15 mL</strong>.</li>
      </ul>

      <div class="band">Preparación del cultivo bacteriano</div>
      <table class="tight"><thead><tr><th>Día</th><th>Procedimiento</th></tr></thead><tbody>
        <tr><td>Día 1</td><td>Inocular desde colonia o vial congelado en BHI líquido e incubar 8 h a 30 °C y 120 rpm.</td></tr>
        <tr><td>Día 2</td><td>Centrifugar, descartar BHI, resuspender en CGXII e incubar overnight a 30 °C y 120 rpm.</td></tr>
        <tr><td>Día 3</td><td>Ajustar en CGXII fresco a OD595 = 1,0 e incubar hasta OD595 ≈ 4-5. Preparar las dos suspensiones de siembra: una a OD595 = 2,0 (para Placa 1) y otra a OD595 = 0,2 (para Placa 2). Mantener en hielo hasta usar.</td></tr>
      </tbody></table>

      <div class="band">Armado de la placa y dilución seriada directa</div>
      <h3>1. Cargar medio y controles (antes del inóculo)</h3>
      <ul>
        <li>Agregar <strong>500 µL de CGXII</strong> a todos los pocillos de la serie: A1-A6, B1-B6 y C1-C6.</li>
        <li>Agregar <strong>500 µL de EMB 16 µg/mL</strong> a A1, B1 y C1. Cada uno de esos pocillos queda con 1 000 µL a 8 µg/mL.</li>
        <li>Agregar <strong>500 µL de CGXII</strong> a D1 y D2 (ctrl+).</li>
        <li>Agregar <strong>500 µL de EMB 2048 µg/mL</strong> (stock primario, sin diluir) a D3 y D4 (ctrl−).</li>
        <li>Agregar <strong>1 000 µL de CGXII</strong> a D5 y D6 (blancos). Estos pocillos quedan completos y no recibirán inóculo.</li>
      </ul>
      <h3>2. Dilución seriada por columnas</h3>
      <ol>
        <li>Mezclar A1, B1 y C1 (cada uno por separado, pipeteando 6-8 veces).</li>
        <li>Transferir <strong>500 µL</strong> de A1 → A2, de B1 → B2 y de C1 → C2 simultáneamente. Mezclar A2, B2 y C2.</li>
        <li>Transferir <strong>500 µL</strong> de A2 → A3, B2 → B3, C2 → C3. Mezclar.</li>
        <li>Continuar de la misma forma hasta llegar a la columna 6.</li>
        <li>Mezclar A6, B6 y C6. Descartar <strong>500 µL</strong> de A6, B6 y C6 para que todos los pocillos de la serie queden con <strong>500 µL</strong>.</li>
      </ol>
      <div class="warn"><strong>Importante:</strong> realizar la transferencia de las tres filas por columna antes de pasar a la siguiente (no dilución fila por fila). Mezclar bien cada pocillo antes de transferir. Evitar burbujas; eliminarlas antes de la lectura en T0.</div>
      <h3>3. Inocular</h3>
      <ul>
        <li><strong>Placa 1:</strong> agregar <strong>500 µL</strong> de inóculo OD595 = 2,0 a todos los pocillos activos: A1-C6, D1, D2, D3 y D4.</li>
        <li><strong>Placa 2:</strong> agregar <strong>500 µL</strong> de inóculo OD595 = 0,2 a los mismos pocillos.</li>
        <li><strong>No</strong> agregar inóculo a D5 ni D6 (blancos).</li>
        <li>El volumen final en todos los pocillos queda en <strong>1 000 µL</strong>.</li>
      </ul>
      <div class="note"><strong>Lectura en T0:</strong> leer OD595 de ambas placas inmediatamente después de inocular y registrar los valores iniciales.</div>

      <div class="band">Incubación y lectura final</div>
      <table class="tight"><thead><tr><th>Parámetro</th><th>Condición</th></tr></thead><tbody>
        <tr><td>Equipo</td><td>Shaker orbital New Brunswick</td></tr>
        <tr><td>Agitación</td><td>240 rpm, órbita 19 mm</td></tr>
        <tr><td>Temperatura</td><td>30 °C</td></tr>
        <tr><td>Duración</td><td>16 h (aceptable: 15-17 h)</td></tr>
        <tr><td>Lectura final</td><td>OD595 en modo endpoint (Multiskan)</td></tr>
      </tbody></table>
      <ol>
        <li>Incubar con tapa y sellado perimetral con parafilm si es necesario.</li>
        <li>Al finalizar, retirar del shaker y dejar reposar 5 minutos.</li>
        <li>Verificar ausencia de burbujas o condensación relevante antes de la lectura.</li>
        <li>Leer OD595 de ambas placas y exportar los datos crudos.</li>
      </ol>

      <div class="band">Análisis de datos</div>
      <h3>1. Crecimiento neto</h3>
      <p>Para cada pocillo: <strong>ΔOD = OD595(Tf) − OD595(T0)</strong>.</p>
      <h3>2. Corrección de fondo y normalización</h3>
      <ul>
        <li>Calcular el ΔOD promedio de los blancos de cada placa.</li>
        <li>Restar ese valor a todos los pocillos experimentales y controles de esa placa.</li>
        <li>Tomar el promedio de los 2 ctrl+ corregidos como referencia de 100% de crecimiento.</li>
        <li>Expresar cada concentración como porcentaje de crecimiento o de inhibición respecto al ctrl+.</li>
        <li>Analizar cada placa por separado para comparar el efecto del tamaño de inóculo.</li>
      </ul>
      <h3>3. Definiciones de salida</h3>
      <ul>
        <li><strong>MIC operativo:</strong> concentración más baja con al menos 90% de inhibición.</li>
        <li><strong>IC50:</strong> concentración que reduce el crecimiento al 50%, obtenida por ajuste sigmoidal de los 6 puntos.</li>
        <li><strong>ctrl−:</strong> se usa solo como control de validez; no se incluye en el ajuste IC50.</li>
      </ul>
      <h3>4. Criterios de validez</h3>
      <table class="tight"><thead><tr><th>Criterio</th><th>Umbral</th></tr></thead><tbody>
        <tr><td>OD595 final promedio de ctrl+</td><td>≥ 0,15</td></tr>
        <tr><td>CV entre ctrl+</td><td>≤ 20%</td></tr>
        <tr><td>OD595 promedio de blancos</td><td>≤ 0,05</td></tr>
        <tr><td>ctrl−</td><td>Sin crecimiento apreciable respecto a T0</td></tr>
        <tr><td>Curva</td><td>Transición sigmoidal visible en al menos una de las dos placas</td></tr>
      </tbody></table>

      <div class="footbox">
        <strong>Resumen operativo:</strong> 2 placas de 24 pocillos, disposición idéntica. Curva de 6 concentraciones (4 → 0,125 µg/mL) en triplicado (filas A, B, C). Fila D: 2 ctrl+ (medio + inóculo), 2 ctrl− (500 µL EMB 2048 µg/mL + 500 µL inóculo = 1 024 µg/mL final), 2 blancos (1 000 µL CGXII, sin bacteria). Dilución seriada por columnas: 500 µL CGXII en todos los pocillos A1-C6; 500 µL de EMB 16 µg/mL en col 1; dilución col 1→6; descartar 500 µL de col 6. Placa 1 recibe inóculo OD595 = 2,0 (OD final = 1,0); Placa 2 recibe inóculo OD595 = 0,2 (OD final = 0,1).
      </div>
    </body>
    </html>
    """)


def main() -> None:
    html = build_html()
    OUTPUT_HTML.write_text(html, encoding="utf-8")
    HTML(string=html, base_url=str(Path.cwd())).write_pdf(OUTPUT_PDF)
    print(f"HTML generado: {OUTPUT_HTML.resolve()}")
    print(f"PDF generado:  {OUTPUT_PDF.resolve()}")


if __name__ == "__main__":
    main()
