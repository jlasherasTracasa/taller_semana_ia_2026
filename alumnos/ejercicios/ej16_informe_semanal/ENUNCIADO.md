# EJ 16 · Informe semanal desde un CSV

## Objetivo
Un informe de texto que se recalcula solo cuando cambian los datos.

## Datos de partida
- `ventas_tienda.csv` — las mismas ventas por categoría y mes.

## Prompt sugerido
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Lee pptx/ventas_tienda.csv y genera informe_semanal.txt \
  con el resumen de ventas: total por categoría, mes con mayores ventas y tendencia general. \
  Calcula los totales realmente leyendo el CSV, no los inventes."
```

## Criterio de éxito
`informe_semanal.txt` con total por categoría, mejor mes (junio, 12.800) y tendencia (+43,8 % de enero a junio), calculados leyendo el CSV — verificados a mano.

## Tiempo estimado
≈ 10 min

## Dificultad
Baja
