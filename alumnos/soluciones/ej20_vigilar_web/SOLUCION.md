# ✅ Solución · EJ 20 · Avisar cuando cambia una web

Ejecución real del 11-10-2026 con opencode 2.0.19 y GLM-5.3-Flash, solo CPU · 25 s · 21.511 tokens de entrada y 2.657 de salida.

Con el modelo gratuito de opencode (`big-pickle`): ✅ también cumple el criterio.

## Qué pasó

Ahora en Python (antes era bash + curl, que no funciona en Windows): rutas relativas al propio script, log de dos líneas y funciona lanzado desde la raíz del disco. En septiembre, con 30 tools extra de un MCP global, dijo «Listo» con un script vacío.

## Veredicto del comprobador

```text
✅ existe vigila/vigila_cambios.py
  ✅ sin rutas absolutas escritas a mano
  ✅ el log tiene al menos 2 líneas (tiene 4)
  ✅ lanzado desde / añade exactamente una línea

🎉 Criterio de éxito cumplido · ej20
```

## Qué hay en esta carpeta

- `prompt.txt`: el encargo exacto.
- `salida.txt`: lo que dijo e hizo el agente (rutas y usuario anonimizados).
- `ficheros/`: lo que creó o cambió el agente.

> Las respuestas de un modelo cambian entre ejecuciones. Compara el **criterio**, no el texto.
