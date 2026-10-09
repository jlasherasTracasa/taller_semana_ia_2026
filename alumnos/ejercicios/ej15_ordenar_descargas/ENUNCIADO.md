# EJ 15 · Ordenar carpeta de descargas

## Objetivo
Automatizar una tarea clásica de mantenimiento: clasificar archivos por tipo sin perder ninguno.

## Datos de partida
- `descargas/` — 11 archivos mezclados: facturas, fotos, hojas de cálculo, documentos e imágenes.

## Prompt sugerido
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Organiza descargas/: crea subcarpetas facturas/, fotos/, \
  hojas_calculo/, documentos/, imagenes/ y mueve cada archivo según su tipo sin borrar nada. \
  Luego muéstrame el árbol resultante."
```

## Criterio de éxito
Las 5 subcarpetas creadas y los 11 archivos movidos según su tipo, sin borrar ni renombrar nada (`find descargas -type f | wc -l` debe seguir dando 11).

## Tiempo estimado
≈ 10 min

## Dificultad
Baja
