# ✅ Solución · EJ 05 · Una web para el centro de mayores

Ejecución real del 09-10-2026 con opencode 2.0.19 y GLM-5.3-Flash, solo CPU · 123 s · 226.139 tokens de entrada y 8.598 de salida.

## Qué pasó

Con `question: deny` y «no me hagas preguntas», escribió `incidencias.md` y la página corregida. En la ronda 1 (opencode 2 sin ese permiso) **se paró a preguntar** y, en modo `run`, falló.

## Veredicto del comprobador

```text
✅ existe web_corregida.html
  ✅ declara lang="es"
  ✅ todas las imágenes con alt (0 sin alt)
  ✅ tiene media queries
  ✅ ningún font-size por debajo de 14px
  ✅ el original sigue ahí
  ✅ existe incidencias.md con la lista de fallos

🎉 Criterio de éxito cumplido · ej05
```

## Qué hay en esta carpeta

- `prompt.txt`: el encargo exacto.
- `salida.txt`: lo que dijo e hizo el agente (rutas y usuario anonimizados).
- `ficheros/`: lo que creó o cambió el agente.

> Las respuestas de un modelo cambian entre ejecuciones. Compara el **criterio**, no el texto.
