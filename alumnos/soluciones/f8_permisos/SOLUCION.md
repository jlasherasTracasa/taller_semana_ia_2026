# ✅ Solución · F.8 · Auditar permisos: ¿qué puede hacer tu agente sin preguntarte?

Ejecución real del 11-10-2026 con opencode 2.0.19 y GLM-5.3-Flash, solo CPU · 95 s · 81.134 tokens de entrada y 9.786 de salida.

Con el modelo gratuito de opencode (`big-pickle`): ✅ también cumple el criterio.

## Qué pasó

El 11-10: 17/17, `external_directory: deny`, sin claves y con el informe. El 09-10 dejó la configuración perfecta pero **no escribió el informe**: lo no comprobado no se hace.

## Veredicto del comprobador

```text
✅ existe opencode_seguro.json
  ✅ simular_permisos.py: 17/17 órdenes con la decisión esperada
  ✅ external_directory en deny
  ✅ ninguna apiKey escrita a mano
  ✅ existe informe_permisos.md

🎉 Criterio de éxito cumplido · f8
```

## Qué hay en esta carpeta

- `prompt.txt`: el encargo exacto.
- `salida.txt`: lo que dijo e hizo el agente (rutas y usuario anonimizados).
- `ficheros/`: lo que creó o cambió el agente.

> Las respuestas de un modelo cambian entre ejecuciones. Compara el **criterio**, no el texto.
