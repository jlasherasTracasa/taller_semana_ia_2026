# EJ 13 · Revisión de estilo de un deck

## Objetivo
Corregir ortografía y consistencia tipográfica de una presentación sin cambiar su contenido.

## Datos de partida
- `deck_ferias.pptx` — presentación de un certamen artesano con erratas, mayúsculas inconsistentes y espacios mal puestos.

## Prompt sugerido
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Revisa deck_ferias.pptx y entrégame primero un informe_incidencias.md con cada error detectado (ortografía, mayúsculas, espacios, tildes) y después una copia corregida como deck_ferias_corregido.pptx. No toques el original."
```

## Criterio de éxito
Informe separado de cambios y copia corregida que abre sin avisos; el archivo original queda intacto.

## Tiempo estimado
≈ 20 min

## Dificultad
Media
