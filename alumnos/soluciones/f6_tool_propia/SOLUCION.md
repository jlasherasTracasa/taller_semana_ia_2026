# ✅ Solución · F.6 · Tu propia tool: plazos en días hábiles

Ejecución real del 11-10-2026 con opencode 2.0.19 y GLM-5.3-Flash, solo CPU · 37 s · 26.790 tokens de entrada y 2.792 de salida.

Con el modelo gratuito de opencode (`big-pickle`): ✅ también cumple el criterio.

## Qué pasó

Buscó la herramienta en el catálogo, la invocó y citó `vence=19/10/2026 (lunes) festivos_saltados=12/10`. Antes, sin la tool, acertó también pero calculando con `shell`: la tool hace el resultado **verificable**. En opencode 2.x ya no hay tools en `.opencode/tools/` (la API de plugins v2 no las registra): por eso es MCP.

## Veredicto del comprobador

```text
✅ vence el 19/10/2026
  ✅ cita la respuesta literal de TU tool

🎉 Criterio de éxito cumplido · f6
```

## Qué hay en esta carpeta

- `prompt.txt`: el encargo exacto.
- `salida.txt`: lo que dijo e hizo el agente (rutas y usuario anonimizados).


> Las respuestas de un modelo cambian entre ejecuciones. Compara el **criterio**, no el texto.
