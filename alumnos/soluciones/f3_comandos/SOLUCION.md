# ✅ Solución · F.3 · Comandos: el encargo de todos los lunes en una palabra

Ejecución real del 09-10-2026 con opencode 2.0.19 y GLM-5.3-Flash, solo CPU · 34 s · 37.224 tokens de entrada y 2.217 de salida.

## Qué pasó

El cuerpo del comando genera las 3 diapositivas con los totales exactos. El comando original decía que el CSV tenía columnas `mes,categoria,importe` (falso): corregido. En opencode 2.x `run --command` ya no existe: los comandos se usan con `/nombre` en modo interactivo.

## Veredicto del comprobador

```text
✅ existe el comando .opencode/commands/informe-semanal.md
  ✅ informe_semanal.pptx existe y es un pptx válido
  ✅ exactamente 3 diapositivas (tiene 3)
  ✅ total 29.800 € correcto
  ✅ total 18.700 € correcto
  ✅ total 14.000 € correcto
  ✅ total 62.500 € correcto

🎉 Criterio de éxito cumplido · f3
```

## Qué hay en esta carpeta

- Pasos: los del ENUNCIADO.
- `salida.txt`: lo que dijo e hizo el agente (rutas y usuario anonimizados).
- `ficheros/`: lo que creó o cambió el agente.

> Las respuestas de un modelo cambian entre ejecuciones. Compara el **criterio**, no el texto.
