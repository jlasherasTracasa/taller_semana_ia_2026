# EJ 22 · Comparar dos versiones de un documento

## Objetivo
Entender qué cambió entre dos versiones de un documento, resumido en prosa y no en un diff crudo.

## Datos de partida
- `informe_v1.docx` e `informe_v2.docx` — dos versiones del informe anual de un centro cívico.

## Prompt sugerido
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Lee informe_v1.docx e informe_v2.docx con python-docx, compara su texto con difflib y escribe cambios.md: un resumen en prosa de lo añadido, lo eliminado y lo modificado, con las cifras viejas y nuevas."
```

## Criterio de éxito
`cambios.md` legible por una persona que no ha visto el diff: menciona todos los cambios (talleres, socios, remanente…) con las cifras exactas de ambas versiones.

## Tiempo estimado
≈ 20 min

## Dificultad
Media
