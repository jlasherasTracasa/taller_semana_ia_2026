# EJ 11 · Informe Markdown → pptx

## Objetivo
Generar un deck sobrio de 5-6 diapositivas a partir de un informe en Markdown.

## Datos de partida
- `informe_cosecha.md` — informe de vendimia de una bodega con cifras y evolución.

## Prompt sugerido
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Lee informe_cosecha.md y genera presentacion.pptx: \
  5-6 diapositivas 16:9 sobrias con títulos y viñetas. Usa $HOME/.../.venv/bin/python que ya \
  tiene python-pptx instalado."
```

## Criterio de éxito
`presentacion.pptx` que abre sin errores, con portada + 4-5 diapositivas (resumen, rendimiento por variedad, evolución, conclusiones) y cifras fieles al informe.

## Tiempo estimado
≈ 15 min

## Dificultad
Media
