# Solución · Informe semanal desde un CSV

## Prompt exacto usado
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Lee pptx/ventas_tienda.csv y genera informe_semanal.txt \
  con el resumen de ventas: total por categoría, mes con mayores ventas y tendencia general. \
  Calcula los totales realmente leyendo el CSV, no los inventes."
```

## Resultado
`informe_semanal.txt` con hogar 29.800 / textil 18.700 / bazar 14.000, mejor mes junio (12.800) y tendencia SUBE (+43,8 %); cifras comprobadas a mano contra el CSV.

## Salida real (extracto validado 2026-09-28)
```
Extracto real de informe_semanal.txt generado por opencode run (validado 2026-09-28;
totales comprobados a mano contra el CSV):
TOTAL POR CATEGORÍA
hogar:  29.800
textil: 18.700
bazar:  14.000

MES CON MAYORES VENTAS
junio, con un total de 12.800

TENDENCIA GENERAL
SUBE. ... de 8.900 en enero a 12.800 en junio, un aumento del 43,8 %.
```

Los artefactos generados (archivos de resultado) están en esta misma carpeta.
