# ✅ Solución · EJ 25 · Entender una carta de la Administración

Ejecución real del 11-10-2026 con opencode 2.0.19 y GLM-5.3-Flash, solo CPU · 29 s · 21.845 tokens de entrada y 3.077 de salida.

Con el modelo gratuito de opencode (`big-pickle`): ✅ también cumple el criterio.

## Qué pasó

GLM se saltó dos veces el apartado del teléfono (aunque decía bien que la carta no lo da). Con los seis apartados numerados: 127,40 €, recargo hasta 152,88 €, plazo lunes 19/10 (salta el 12) y «la carta no lo dice».

## Veredicto del comprobador

```text
✅ existe explicacion.md
  ✅ importe: 127,40 €
  ✅ recargo del 20 %
  ✅ lo que pagaría con recargo: 152,88 €
  ✅ plazo: 19 de octubre (el 12 es festivo)
  ✅ tiene el apartado «¿A qué teléfono llamo?»
  ✅ admite que la carta no da teléfono
  ✅ no se inventa ningún número de teléfono

🎉 Criterio de éxito cumplido · ej25
```

## Qué hay en esta carpeta

- `prompt.txt`: el encargo exacto.
- `salida.txt`: lo que dijo e hizo el agente (rutas y usuario anonimizados).
- `ficheros/`: lo que creó o cambió el agente.

> Las respuestas de un modelo cambian entre ejecuciones. Compara el **criterio**, no el texto.
