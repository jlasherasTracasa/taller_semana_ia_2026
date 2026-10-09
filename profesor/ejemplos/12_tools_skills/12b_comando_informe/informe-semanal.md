---
description: Genera el informe semanal de ventas (pptx) a partir de datos/ventas_tienda.csv
agent: build
---
Lee `datos/ventas_tienda.csv` (columnas: mes,categoria,importe).

Objetivo: crea `informe_semanal.pptx` con exactamente 3 diapositivas 16:9:
1. Portada: «Informe semanal de ventas» + mes más reciente del CSV.
2. Total por categoría (calculado realmente leyendo el CSV, no inventado).
3. Tendencia: primer vs último mes y variación porcentual.

LÍMITES: usa el intérprete `/home/jlasheras@tcsa.local/imagenes_semana_de_la_ia/.venv/bin/python`
(tiene python-pptx instalado); no borres nada; no abras el archivo.

CRITERIO: los totales deben cuadrar con el CSV; si algún cálculo no cuadra, para y dilo.
$ARGUMENTS
