# EJ 14 · Traducir un deck conservando el formato

## Objetivo
Traducir una presentación editando el XML directamente, sin reconstruir el archivo.

## Datos de partida
- `charla_taller_es.pptx` — presentación breve en castellano.

## Prompt sugerido
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Traduce charla_taller_es.pptx al inglés editando el XML directamente (unzip → edita slideN.xml → zip). Usa defusedxml.minidom, no xml.etree. Entrega charla_taller_en.pptx. No alteres imágenes, tablas ni gráficos."
```

## Criterio de éxito
`charla_taller_en.pptx` que se abre sin avisos de reparación y conserva tablas y gráficos intactos, con el texto traducido.

## Tiempo estimado
≈ 25 min

## Dificultad
Alta
