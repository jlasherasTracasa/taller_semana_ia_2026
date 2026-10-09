# Solución · Datos CSV → pptx con gráficos

## Prompt exacto usado
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Lee ventas_tienda.csv y genera ventas.pptx: portada + \
  una diapositiva con gráfico de líneas generado con matplotlib (meses vs categorías) embebido \
  como imagen. Usa python-pptx y matplotlib ya instalados."
```

## Resultado
`ventas.pptx` con 3 diapositivas y gráfico matplotlib incrustado; totales verificados a mano: hogar 29.800, textil 18.700, bazar 14.000, total 62.500 €.

## Salida real (extracto validado 2026-09-28)
```
Extracto real de la salida de opencode run (validado 2026-09-28):
- Diapositiva 2: gráfico de líneas matplotlib (meses vs hogar, textil, bazar)
  incrustado como imagen de alta resolución.
- Diapositiva 3: totales por categoría — Hogar 29.800 € (48%), Textil 18.700 € (30%),
  Bazar 14.000 € (22%), Total general: 62.500 €

Verificado a mano contra ventas_tienda.csv: totales exactos.
```

Los artefactos generados (archivos de resultado) están en esta misma carpeta.
