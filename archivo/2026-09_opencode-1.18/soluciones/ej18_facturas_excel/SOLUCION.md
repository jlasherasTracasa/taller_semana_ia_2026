# Solución · EJ 18 · Facturas PDF → Excel

## Prompt exacto usado
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Extrae de los PDF de facturas/ el emisor, la fecha, la base imponible, el IVA y el total, y genera facturas.xlsx (con openpyxl). Añade una fila final con la suma de totales y comprueba que cuadra con los originales."
```

## Resultado
`facturas.xlsx` con emisor, fecha, base, IVA y total de las dos facturas, más la fila de suma de totales verificada contra los originales.

## Salida real (extracto validado 2026-09-28)
```
Totales originales: ['454.48', '1212.90'] -> suma 1667.38
CUADRA: la suma del xlsx coincide con los originales.

Generado facturas.xlsx con los datos extraídos:
| Emisor | Fecha | Base | IVA | Total |
|---|---|---|---|---|
| Ferretería Etxeberria | 03/02/2026 | 375,60 | 78,88 | 454,48 |
| Limpiezas Ribera S.L. | 28/02/2026 | 1.002,40 | 210,50 | 1.212,90 |
| SUMA TOTALES | | | | 1.667,38 |
```

El artefacto generado está en esta misma carpeta.
