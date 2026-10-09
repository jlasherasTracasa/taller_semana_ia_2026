# ✅ Solución · F.0 · El bucle ReAct en 70 líneas

Ejecución real del 09-10-2026 con opencode 2.0.19 y GLM-5.3-Flash, solo CPU.

## Qué pasó

Funciona. Lección: con el historial mal guardado (tool_calls como texto JSON) el agente terminaba **sin responder a la pregunta** 3 de 3 veces; al guardarlo bien (`model_dump()`) contestó «reunion.txt, 5 líneas» 2 de 2. El historial es su memoria.

## Qué hay en esta carpeta

- Pasos: los del ENUNCIADO.
- `salida.txt`: lo que dijo e hizo el agente (rutas y usuario anonimizados).


> Las respuestas de un modelo cambian entre ejecuciones. Compara el **criterio**, no el texto.
