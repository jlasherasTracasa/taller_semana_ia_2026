# EJ 02 · Agenda de evento desde un CSV

## Objetivo
Convertir el programa de unas fiestas (CSV) en una página de agenda agrupada por franjas horarias.

## Datos de partida
- `programa.csv` — 6 eventos con hora, título y tipo de actividad.

## Prompt sugerido
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Lee programa.csv y crea agenda.html: página de una \
  sola columna, diseño festivo, responsive y sin dependencias externas."
```

## Criterio de éxito
`agenda.html` con los 6 eventos presentes y agrupados por franja (mañana/tarde), una sola columna, responsive y sin dependencias externas. Comprueba que ninguna fila del CSV se haya quedado fuera.

## Tiempo estimado
≈ 10 min

## Dificultad
Baja
