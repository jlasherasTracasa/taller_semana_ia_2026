# F.2 · Skills y comandos personalizados

## Objetivo
Convertir un encargo recurrente en un comando versionado (.opencode/command/) que cualquiera del equipo puede invocar.

## Datos de partida
- `datos/ventas_tienda.csv` y `.opencode/command/informe-semanal.md` (cópialos a tu carpeta de trabajo respetando esas rutas relativas).

## Prompt sugerido
```bash
$ opencode run --model vllm/GLM-5.3-Flash --command informe-semanal
```

## Criterio de éxito
`informe_semanal.pptx` con exactamente 3 diapositivas y totales que cuadran con el CSV (62.500 € en total). El mismo comando debe funcionar el mes que viene con datos nuevos.

## Tiempo estimado
≈ 10 min

## Dificultad
Media
