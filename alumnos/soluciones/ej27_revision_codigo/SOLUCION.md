# ✅ Solución · EJ 27 · Revisión de código de un cambio (pull request)

Ejecución real del 09-10-2026 con opencode 2.0.19 y GLM-5.3-Flash, solo CPU · 110 s · 63.303 tokens de entrada y 11.038 de salida.

## Qué pasó

Encontró los seis problemas (inyección SQL, clave en el código, regresión de la cuota a los 65, tests borrados, `except: pass` y datos personales a un tercero) y pidió cambios. **En el primer intento**, con «No modifiques nada: solo revisa», hizo la revisión en pantalla y **no creó `revision.md`**.

## Veredicto del comprobador

```text
✅ existe revision.md
  ✅ detecta la inyección SQL
  ✅ detecta la clave escrita en el código
  ✅ detecta la regresión de la cuota a los 65
  ✅ detecta los tests eliminados
  ✅ señala el except que oculta errores
  ✅ veredicto: pedir cambios
  ✅ no ha modificado el diff

🎉 Criterio de éxito cumplido · ej27
```

## Qué hay en esta carpeta

- `prompt.txt`: el encargo exacto.
- `salida.txt`: lo que dijo e hizo el agente (rutas y usuario anonimizados).
- `ficheros/`: lo que creó o cambió el agente.

> Las respuestas de un modelo cambian entre ejecuciones. Compara el **criterio**, no el texto.
