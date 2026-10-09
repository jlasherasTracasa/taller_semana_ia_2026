# ✅ Solución · EJ 16 · El informe que se recalcula solo

Ejecución real del 09-10-2026 con opencode 2.0.19 y GLM-5.3-Flash, solo CPU · 37 s · 83.603 tokens de entrada y 3.951 de salida.

## Qué pasó

`informe.py` regenera el informe con 29.800 / 18.700 / 14.000, junio 12.800 y +43,8 %. El encargo antiguo apuntaba a `pptx/ventas_tienda.csv`, una ruta que no existe.

## Veredicto del comprobador

```text
✅ existe informe_semanal.txt
  ✅ total 29800 correcto
  ✅ total 18700 correcto
  ✅ total 14000 correcto
  ✅ mejor mes: junio con 12.800
  ✅ tendencia +43,8 %
  ✅ existe informe.py (el informe se puede regenerar)

🎉 Criterio de éxito cumplido · ej16
```

## Qué hay en esta carpeta

- `prompt.txt`: el encargo exacto.
- `salida.txt`: lo que dijo e hizo el agente (rutas y usuario anonimizados).
- `ficheros/`: lo que creó o cambió el agente.

> Las respuestas de un modelo cambian entre ejecuciones. Compara el **criterio**, no el texto.
