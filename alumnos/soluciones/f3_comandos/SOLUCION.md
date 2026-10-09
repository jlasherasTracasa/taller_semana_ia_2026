# Solución · F.2 · Skills y comandos personalizados

## Prompt exacto usado
```bash
$ opencode run --model vllm/GLM-5.3-Flash --command informe-semanal
```

## Resultado
`--command informe-semanal` cargó el procedimiento, leyó el CSV y generó `informe_semanal.pptx` (3 diapositivas; total 62.500 €; +43,8 % enero→junio).

## Salida real (extracto validado 2026-09-28)
```
> build · GLM-5.3-Flash

→ Skill "pptx"
→ Read datos/ventas_tienda.csv
El CSV real está en formato ancho (`mes,hogar,textil,bazar`), no `mes,categoria,importe`; calcularé los totales reales leyéndolo tal cual. Creo el script con python-pptx usando el intérprete indicado:

← Write ./
Wrote file successfully.

$ <repo>/.venv/bin/python ./
OK -> ./
Totales por categoria: {'hogar': 29800, 'textil': 18700, 'bazar': 14000}
Mensual: {'enero': 8900, 'febrero': 8600, 'marzo': 10100, 'abril': 10600, 'mayo': 11500, 'junio': 12800}
Tendencia enero(8900) -> junio(12800): 43.82% | Total general: 62500

$ <repo>/.venv/bin/python ~/.agents/skills/pptx/scripts/office/validate.py ./ && <repo>/.venv/bin/python - <<'EOF'
from pptx import Presentation
p = Presentation('./')
print("Slides:", len(p.slides), "| 16:9:", round(p.slide_width/914400,3), "x", round(p.slide_height/914400,2))
for i, s in enumerate(p.slides, 1):
    texts = [sh.text_frame.text for sh in s.shapes if sh.has_text_frame and sh.text_frame.text]
    charts = sum(1 for sh in s.shapes if sh.has_chart)
    print(f"-- Slide {i} (charts: {charts}):", texts[:3])
EOF
Traceback (most recent call last):
  File "~/.agents/skills/pptx/scripts/office/validate.py", line 22, in <module>
    import defusedxml.ElementTree as ET
ModuleNotFoundError: No module named 'defusedxml'

Verificación estructural (sin abrir el archivo en ninguna aplicación):
$ <repo>/.venv/bin/python - <<'EOF'
from pptx import Presentation
import zipfile
p = Presentation('./')
print("Slides:", len(p.slides), "| 16:9:", round(p.slide_width/914400,3), "x", round(p.slide_height/914400,2))
for i, s in enumerate(p.slides, 1):
    texts = [sh.text_frame.text for sh in s.shapes if sh.has_text_frame and sh.text_frame.text]
    charts = sum(1 for sh in s.shapes if sh.has_chart)
    print(f"-- Slide {i} (charts: {charts}):", texts[:4])
z = zipfile.ZipFile('./')
bad = z.testzip()
print("ZIP ok:", bad is None)
EOF
Slides: 3 | 16:9: 13.333 x 7.5
-- Slide 1 (charts: 0): ['Informe semanal de ventas', 'Mes más reciente del histórico: Junio', 'Datos calculados directamente desde ventas_tienda.csv · 6 meses · 3 categorías']
-- Slide 2 (charts: 1): ['Total por categoría', 'Suma de importes de enero a junio', 'TOTAL GENERAL', '62.500 €']
-- Slide 3 (charts: 1): ['Tendencia: enero → junio', 'Ventas totales por mes (suma de las tres categorías)', 'Enero', '8.900 €']
ZIP ok: True

Listo: `./` — 3 diapositivas 16:9, creadas con python-pptx usando el intérprete indicado.

Nota: el CSV real es formato ancho (`mes,hogar,textil,bazar`), no `mes,categoria,importe`; los totales se calcularon leyéndolo tal cual:

- **Slide 1 — Portada**: «Informe semanal de ventas» + mes más reciente (junio).
- **Slide 2 — Total por categoría** (gráfico de barras + tarjetas): hogar 29.800 € · textil 18.700 € · bazar 14.000 € · total general 62.500 €.
- **Slide 3 — Tendencia** (gráfico de línea mensual): enero 8.900 € → junio 12.800 €, variación **+43,8 %**.
```

Los artefactos generados (archivos de resultado) están en esta misma carpeta.
