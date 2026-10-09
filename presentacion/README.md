# 🖥️ Presentación

| Fichero | Qué es |
|---|---|
| [`taller-agentes-ia.pdf`](taller-agentes-ia.pdf) | Las diapositivas en PDF (con las fuentes incrustadas): para proyectar o descargar |
| [`taller-agentes-ia.pptx`](taller-agentes-ia.pptx) | Las mismas en PowerPoint, **sin notas del ponente** |
| `taller-agentes-ia-con-notas.pptx` | Versión del docente con notas. **No está en el repositorio**: se genera en local o se descifra de `profesor/taller-con-notas.pptx.enc` |
| `assets/` | Logos, imagen del cartel, adornos de circuitos y la fuente Barlow Condensed |
| `fuente/` | Generador (`generar_presentacion.js`, pptxgenjs) y adornos (`circuitos.js`) |

## Diseño

Minimalista, tipo Material Design, con la identidad de la **Semana de la IA 2026**:

- Diapositivas de contenido claras (`#F6F5F1`), tarjetas blancas con sombra suave y mucho aire.
- Portada, separadores y cierre en el **azul noche** del cartel (`#0F1C26`) con sus **circuitos** cian y ámbar.
- Acento **dorado** (`#E4B858` sobre oscuro, `#B8862B` sobre claro), como el «DE LA» del logotipo.
- Títulos en **Barlow Condensed** (como el cartel; licencia OFL) y texto en Calibri. Instala las fuentes de
  `assets/fuentes/` en el portátil desde el que proyectes; si no, PowerPoint las sustituye (el PDF ya las lleva).
- Logotipo de la Semana de la IA recreado en vectorial (`assets/logo_semana_ia_2026*.svg`) a partir del cartel
  oficial (`assets/banner_semana_ia_2026_oficial.jpg`, de unavarra.es).
- Código QR a la web del taller en la diapositiva 2 y en la de cierre.

## Estructura (34 diapositivas)

| # | Bloque |
|---|---|
| 1-4 | Portada · cómo funciona el taller (con QR) · perfiles · preparar el portátil |
| 5-12 | **01 · Qué es un agente**: chat vs agente, anatomía, ReAct, tools, piezas de opencode, permisos, buen encargo |
| 13-20 | **02 · Ejercicios por áreas**: reparto, una diapositiva por área y la prueba de seguridad |
| 21-28 | **03 · Lo que aprendimos**: cuatro casos reales, verificar y medir, cuándo no usar un agente, coste |
| 29-34 | **04 · Cierre**: niveles, reto avanzado, glosario, qué hacer el lunes, gracias |

## Regenerar

```bash
cd presentacion/fuente
npm install                                # pptxgenjs, react-icons, sharp, qrcode
python3 ../../herramientas/construir_kit.py
node generar_presentacion.js               # → ../taller-agentes-ia.pptx y ../taller-agentes-ia-con-notas.pptx
soffice --headless --convert-to pdf --outdir .. ../taller-agentes-ia.pptx
```

Las tarjetas de ejercicios, los resultados de validación y los costes se leen de `alumnos/ejercicios/indice.json` y
`herramientas/validacion.json`: si cambias un ejercicio, la presentación se actualiza sola.
