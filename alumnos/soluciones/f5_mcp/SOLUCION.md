# ✅ Solución · F.5 · MCP: enchufar un servidor de herramientas

Ejecución real del 09-10-2026 con opencode 2.0.19 y GLM-5.3-Flash, solo CPU · 9 s · 30.132 tokens de entrada y 903 de salida.

## Qué pasó

Cita literalmente `filas=6 suma=29800 media=4966.67`. En opencode 2.x la tool MCP no aparece suelta: el modelo la **busca en un catálogo** y la llama escribiendo código (tool `execute`), y el catálogo puede tardar unos segundos en cargarse.

## Veredicto del comprobador

```text
✅ el agente cita suma=29800
  ✅ y media=4966.67 (el valor EXACTO de la tool)

🎉 Criterio de éxito cumplido · f5
```

## Qué hay en esta carpeta

- `prompt.txt`: el encargo exacto.
- `salida.txt`: lo que dijo e hizo el agente (rutas y usuario anonimizados).


> Las respuestas de un modelo cambian entre ejecuciones. Compara el **criterio**, no el texto.
