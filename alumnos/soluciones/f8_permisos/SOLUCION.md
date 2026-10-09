# 🟡 Solución · F.8 · Auditar permisos: ¿qué puede hacer tu agente sin preguntarte?

Ejecución real del 09-10-2026 con opencode 2.0.19 y GLM-5.3-Flash, solo CPU · 50 s · 70.021 tokens de entrada y 4.583 de salida.

## Qué pasó

Dejó `opencode_seguro.json` perfecto (17/17, `external_directory: deny`, sin claves) pero **no escribió `informe_permisos.md`** y terminó preguntando si quería que lo escribiera: hizo la parte que tenía comprobación y se saltó la que no.

## Veredicto del comprobador

```text
✅ existe opencode_seguro.json
  ✅ simular_permisos.py: 17/17 órdenes con la decisión esperada
  ✅ external_directory en deny
  ✅ ninguna apiKey escrita a mano
  ❌ existe informe_permisos.md

⚠️  1 comprobación(es) sin cumplir · f8
```

## Qué hay en esta carpeta

- `prompt.txt`: el encargo exacto.
- `salida.txt`: lo que dijo e hizo el agente (rutas y usuario anonimizados).
- `ficheros/`: lo que creó o cambió el agente.

> Las respuestas de un modelo cambian entre ejecuciones. Compara el **criterio**, no el texto.
