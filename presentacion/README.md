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

## Estructura (50 diapositivas)

| # | Bloque |
|---|---|
| 1-8 | Portada · cómo funciona (con QR) · **demos en directo y prácticas** · **el plan de hoy** (qué demo va en cada momento) · perfiles · preparar el ordenador (Windows primero, sin clave) · **modo interactivo** · **plan B** |
| 9-14 | **01 · Cómo hemos llegado aquí**: de las reglas al aprendizaje (1950-2016), de los transformers a los agentes (2017-2026), qué es un modelo de lenguaje, cómo aprende, el contexto |
| 15-28 | **02 · Qué es un agente**: chat frente a agente, anatomía y **una diapositiva por pieza con su ejercicio** (ReAct F.0, tools F.1, AGENTS.md F.2, comandos F.3, skills F.4, MCP F.5-F.6, subagentes F.7, permisos F.8), resumen y buen encargo |
| 29-36 | **03 · Ejercicios por áreas**: reparto, una diapositiva por área (con las demos marcadas) y la prueba de seguridad |
| 37-45 | **04 · Lo que aprendimos**: cinco casos reales (qué pasó, por qué, qué hacemos ahora), verificar y medir, cuándo no usar un agente, coste |
| 46-51 | **05 · Cierre**: niveles, reto avanzado, glosario, qué hacer el lunes, gracias |

Cada diapositiva de una pieza lleva arriba a la derecha su ejercicio: **DEMO EN DIRECTO** (lo hace el profesor) o
**PRÁCTICA** (lo hacen los alumnos). Las demos salen de `demo=True` en `herramientas/aventura.py`.

## Regenerar

```bash
cd presentacion/fuente
npm install                                # pptxgenjs, react-icons, sharp, qrcode
python3 ../../herramientas/construir_kit.py
node generar_presentacion.js               # → ../taller-agentes-ia.pptx y ../taller-agentes-ia-con-notas.pptx
soffice --headless --convert-to pdf --outdir .. ../taller-agentes-ia.pptx   # o con Docker: ver más abajo
```

Las tarjetas de ejercicios, los resultados de validación y los costes se leen de `alumnos/ejercicios/indice.json` y
`herramientas/validacion.json`: si cambias un ejercicio, la presentación se actualiza sola.

### PDF sin LibreOffice instalado (con Docker)

```bash
cd presentacion
docker run --rm -v "$PWD":/r debian:bookworm-slim bash -c "apt-get update -qq && apt-get install -y -qq libreoffice-impress fonts-crosextra-carlito >/dev/null && \
  mkdir -p /usr/share/fonts/truetype/barlow && cp /r/assets/fuentes/*.ttf /usr/share/fonts/truetype/barlow/ && fc-cache -f && \
  cd /r && soffice --headless --convert-to pdf taller-agentes-ia.pptx"
```
