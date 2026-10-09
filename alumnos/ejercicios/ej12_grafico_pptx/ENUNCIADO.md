# EJ 12 · Datos CSV → pptx con gráficos

## Objetivo
Generar una presentación con un gráfico de líneas calculado de verdad a partir de los datos.

## Datos de partida
- `ventas_tienda.csv` — ventas mensuales (enero-junio) por categoría: hogar, textil, bazar.

## Prompt sugerido
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Lee ventas_tienda.csv y genera ventas.pptx: portada + \
  una diapositiva con gráfico de líneas generado con matplotlib (meses vs categorías) embebido \
  como imagen. Usa python-pptx y matplotlib ya instalados."
```

## Criterio de éxito
`ventas.pptx` con el gráfico incrustado y totales EXACTOS contra el CSV (hogar 29.800 €, textil 18.700 €, bazar 14.000 €, total 62.500 €). Verifícalos a mano: si no cuadran, el encargo está mal hecho.

## Tiempo estimado
≈ 15 min

## Dificultad
Media
