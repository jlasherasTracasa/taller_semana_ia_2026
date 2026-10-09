# Solución · EJ 13 · Revisión de estilo de un deck

## Prompt exacto usado
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Revisa deck_ferias.pptx y entrégame primero un informe_incidencias.md con cada error detectado (ortografía, mayúsculas, espacios, tildes) y después una copia corregida como deck_ferias_corregido.pptx. No toques el original."
```

## Resultado
`informe_incidencias.md` con 13 incidencias documentadas (6 de tildes, 5 de mayúsculas y 3 de espaciado; la n.º 1, «artesaNIA», cuenta en dos categorías). Ojo: el resumen final del agente (extracto de abajo) dice 5 y 6: **revisa el fichero, no el resumen** y `deck_ferias_corregido.pptx`, editado solo en el texto de los runs (formato intacto). El original quedó intacto (comprobado por md5).

## Salida real (extracto validado 2026-09-28)
```
- Tildes (5): cestería, sábado, Organización, Teléfono, extensión
- Mayúsculas (6): «artesaNIA» → artesanía, «SEPTIEMBRE» → septiembre,
  «entrada gratuita» → Entrada…, «CONCIERTO» → Concierto
- Espacios (3): espacio antes de la coma en «txistu ,», doble espacio, espacios finales

$ .../validate.py deck_ferias_corregido.pptx --original deck_ferias.pptx && md5sum deck_ferias.pptx
All validations PASSED!
7f4de0820d61bf106fdd83433317a6db  deck_ferias.pptx
```

Los artefactos generados están en esta misma carpeta.

## Nota sobre la validación
El agente encontró en la máquina del docente la **skill `pptx`** (`~/.agents/skills/pptx`) y usó su `validate.py`
para comprobar que el fichero corregido es un PPTX válido. Es un buen ejemplo de skill: instrucciones y scripts
que el agente descubre y usa solo. Si tú no la tienes, pide que valide con
`python -c "import pptx; pptx.Presentation('deck_ferias_corregido.pptx')"` o abriéndolo en LibreOffice.
