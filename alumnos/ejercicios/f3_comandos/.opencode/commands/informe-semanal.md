---
description: Genera el informe semanal de ventas (pptx) a partir de datos/ventas_tienda.csv
---
Lee `datos/ventas_tienda.csv`. Columnas: `mes,hogar,textil,bazar` (una fila por mes, importes en euros).

Crea `informe_semanal.pptx` con python-pptx y EXACTAMENTE 3 diapositivas 16:9:
1. Portada: «Informe semanal de ventas» y el último mes del CSV.
2. Total por categoría y total general, calculados con Python leyendo el CSV (nunca de memoria).
3. Tendencia: total del primer mes frente al del último y variación en porcentaje.

LÍMITES: no borres nada; no inventes cifras.
CRITERIO: abre el pptx al final con python-pptx, cuenta las diapositivas (tienen que ser 3) y comprueba que la suma de
las categorías es igual al total general. Si algo no cuadra, para y dilo.

Indicaciones extra de quien lanza el comando: $ARGUMENTS
