# ✅ Solución · EJ 05 · Auditoría de accesibilidad de una web

Ejecución real del 11-10-2026 con opencode 2.0.19 y GLM-5.3-Flash, solo CPU · 22 s · 47.252 tokens de entrada y 2.261 de salida.

Con el modelo gratuito de opencode (`big-pickle`): ✅ también cumple el criterio.

## Qué pasó

El 11-10 falló una vez: dijo que «el mensaje se cortaba» y no creó `web_corregida.html`. Con la entrega numerada —(1) `incidencias.md`, (2) `web_corregida.html`— pasa. En la primera ronda de octubre se paró a preguntar y por eso el kit tiene `question: deny`.

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
