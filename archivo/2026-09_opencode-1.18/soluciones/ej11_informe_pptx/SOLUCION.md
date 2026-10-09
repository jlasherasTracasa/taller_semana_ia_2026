# Solución · Informe Markdown → pptx

## Prompt exacto usado
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Lee informe_cosecha.md y genera presentacion.pptx: \
  5-6 diapositivas 16:9 sobrias con títulos y viñetas. Usa $HOME/.../.venv/bin/python que ya \
  tiene python-pptx instalado."
```

## Resultado
`presentacion.pptx` con 5 diapositivas: portada, resumen, rendimiento por variedad, evolución de la cosecha y conclusiones; verificado con python-pptx.

## Salida real (extracto validado 2026-09-28)
```
Salida real, verificada con python-pptx tras opencode run (validado 2026-09-28):
slides: 5
1 | Informe de cosecha — Bodega Larraz · Vendimia 2025
2 | Resumen de la vendimia
3 | Rendimiento por variedad
4 | Evolución de la cosecha (kg)
5 | Conclusiones y recomendaciones
```

Los artefactos generados (archivos de resultado) están en esta misma carpeta.
