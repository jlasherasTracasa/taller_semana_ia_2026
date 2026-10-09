# EJ 05 · Auditoría responsive/accesible

## Objetivo
Detectar y corregir los fallos de accesibilidad y adaptabilidad de una página web real.

## Datos de partida
- `web_centro_mayores.html` — página con fallos deliberados: contraste insuficiente, letra pequeña, sin `lang`, contenido no accesible por teclado…

## Prompt sugerido
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Audita web_centro_mayores.html: contraste de color, tamaño de fuente, media queries, atributo lang y navegación por teclado. Entrega primero la lista de incidencias y después la página corregida como web_corregida.html."
```

## Criterio de éxito
Lista de incidencias con su corrección pareja a cada fallo, y un `web_corregida.html` que declara `lang="es"`, usa tamaños legibles, buen contraste y textos alternativos.

## Tiempo estimado
≈ 15 min

## Dificultad
Baja
