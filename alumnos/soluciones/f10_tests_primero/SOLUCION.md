# ✅ Solución · F.10 · Tests primero: el agente no puede hacer trampa

Ejecución real del 09-10-2026 con opencode 2.0.19 y GLM-5.3-Flash, solo CPU · 30 s · 50.158 tokens de entrada y 2.052 de salida.

## Qué pasó

9/9 tests en verde sin tocar `tests/`. Arregló los cuatro fallos, incluido el cambio en céntimos enteros para evitar el error de coma flotante.

## Veredicto del comprobador

```text
✅ tests/test_precios.py intacto
  ✅ python3 -m unittest: OK con 9 tests

🎉 Criterio de éxito cumplido · f10
```

## Qué hay en esta carpeta

- `prompt.txt`: el encargo exacto.
- `salida.txt`: lo que dijo e hizo el agente (rutas y usuario anonimizados).
- `ficheros/`: lo que creó o cambió el agente.

> Las respuestas de un modelo cambian entre ejecuciones. Compara el **criterio**, no el texto.
