# EJ 18 · Facturas PDF → Excel

## Objetivo
Extraer los datos económicos de facturas en papel digital y volcarlos en una hoja de cálculo.

## Datos de partida
- `facturas/factura_ferreteria.pdf` y `facturas/factura_limpieza.pdf` — facturas ficticias con base, IVA y total.

## Prompt sugerido
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Extrae de los PDF de facturas/ el emisor, la fecha, la base imponible, el IVA y el total, y genera facturas.xlsx (con openpyxl). Añade una fila final con la suma de totales y comprueba que cuadra con los originales."
```

## Criterio de éxito
`facturas.xlsx` legible con openpyxl; la suma de totales coincide con la suma manual de las facturas (454,48 + 1.212,90 = 1.667,38 EUR).

## Tiempo estimado
≈ 25 min

## Dificultad
Media-alta
