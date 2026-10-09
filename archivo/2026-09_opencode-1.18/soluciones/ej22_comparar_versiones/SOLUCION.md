# Solución · EJ 22 · Comparar dos versiones de un documento

## Prompt exacto usado
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Lee informe_v1.docx e informe_v2.docx con python-docx, compara su texto con difflib y escribe cambios.md: un resumen en prosa de lo añadido, lo eliminado y lo modificado, con las cifras viejas y nuevas."
```

## Resultado
`cambios.md`: resumen en prosa de añadidos, eliminaciones y modificaciones con las cifras exactas de ambas versiones.

## Salida real (extracto validado 2026-09-28)
```
Hecho. Comparé ambos docx con difflib y escribí cambios.md:
- Modificado: cifras actualizadas (14 → 17 talleres, 210 → 238 socios)
  y reformuladas las frases del taller más frecuentado y del saldo.
- Añadido: el taller de memoria digital y el remanente de 3.150 euros
  destinado a audiovisuales.
- Eliminado: nada; v2 solo actualiza y amplía el texto de v1.
```

El artefacto generado está en esta misma carpeta.
