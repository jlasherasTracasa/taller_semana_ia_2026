# ✅ Solución · F.7 · Subagentes: un redactor y un revisor que no puede tocar nada

Ejecución real del 09-10-2026 con opencode 2.0.19 y GLM-5.3-Flash, solo CPU · 86 s · 279.249 tokens de entrada y 6.197 de salida.

## Qué pasó

Delegó en dos subagentes **en paralelo** (redactor y revisor). El revisor leyó una versión anterior del fichero y marcó un error ya corregido: una condición de carrera de manual. Con `edit: deny`, el revisor no pudo editar (`Edit … failed`).

## Veredicto del comprobador

```text
✅ existe nota_prensa.md
  ✅ fecha correcta (28 de noviembre)
  ✅ 12 plazas e inscripción hasta el 26
  ✅ máximo 200 palabras
  ✅ el agente delegó en el subagente revisor

🎉 Criterio de éxito cumplido · f7
```

## Qué hay en esta carpeta

- `prompt.txt`: el encargo exacto.
- `salida.txt`: lo que dijo e hizo el agente (rutas y usuario anonimizados).
- `ficheros/`: lo que creó o cambió el agente.

> Las respuestas de un modelo cambian entre ejecuciones. Compara el **criterio**, no el texto.
