# :bar_chart: Presentación del taller

| Fichero | Qué es |
|---|---|
| `taller-agentes-ia.pptx` | La presentación: 32 diapositivas 16:9 con notas del ponente en todas. |
| `taller-agentes-ia.pdf` | La misma en PDF (renderizada con LibreOffice), para proyectar si falla PowerPoint. |
| `assets/` | Logos oficiales y la imagen de portada. |
| `fuente/` | Generador (`generar_presentacion.js`, pptxgenjs) y datos de los ejercicios (`ejercicios.json`). |

## Estructura

| # | Bloque | Contenido |
|---|---|---|
| 1–3 | Apertura | Portada, qué te llevas, plan |
| 4–15 | 01 · Qué es un agente | Del chat al agente, anatomía, **ReAct** (traza real), **tools** y function calling, permisos de opencode, **MCP**, **skills**, subagentes y memoria, tabla prompt/tool/skill/agente/MCP, opencode en 2 minutos, cómo se da un encargo |
| 16–23 | 02 · Manos a la obra | Bloques A–D y F con los 26 ejercicios, EJ 10 (inyección) en detalle, cómo verificar |
| 24–28 | 03 · Seguridad y criterio | Seis reglas, dos casos reales (proceso ajeno, «Listo»), cuándo NO usar un agente |
| 29–32 | Cierre | Reto del paper, glosario, qué hacer el lunes, gracias |

## Diseño

- **Plantilla** de la Cátedra de Ciencias de la Computación e Inteligencia Artificial (UPNA–Tracasa). Paleta tomada
  de los píxeles del logo oficial: marino `#0F2A56`, azul `#2050A0`, cian `#00A8D0`, tinta `#1D2433`. Calibri y
  Courier New para el código.
- **Logos** (`assets/`): `logo_catedra_ia.png` (logo combinado Cátedra + UPNA + Tracasa, de unavarra.es),
  `logo_upna_blanco.png` (unavarra.es) y `logo_tracasa_simbolo.png` (itracasa.es).
- **Portada**: «El primer golpe», generada con Qwen-Image-2.1 en el proyecto de este repositorio. Es una de las
  imágenes descartadas para el concurso, así que no compromete el anonimato de las obras presentadas.
- Iconos de Font Awesome (react-icons) rasterizados con sharp.

## Regenerar

```bash
cd docs/taller/presentacion/fuente
npm install                                   # pptxgenjs, react-icons, react, react-dom, sharp
python3 extraer_ejercicios.py                 # ejercicios.json desde alumnos/ejercicios y alumnos/soluciones
node generar_presentacion.js                  # → ../taller-agentes-ia.pptx
soffice --headless --convert-to pdf --outdir .. ../taller-agentes-ia.pptx
cp ../taller-agentes-ia.pptx ../../alumnos/   # la copia del kit
```

Las tarjetas de ejercicios se dibujan a partir de `ejercicios.json`. Un ejercicio aparece como «✓ validado» cuando
su `soluciones/<id>/salida.txt` contiene una ejecución real que no terminó con error.
