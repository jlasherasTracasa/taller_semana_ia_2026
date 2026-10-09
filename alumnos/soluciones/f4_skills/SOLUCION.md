# ✅ Solución · F.4 · Skills: recetas que el agente carga cuando las necesita

Ejecución real del 09-10-2026 con opencode 2.0.19 y GLM-5.3-Flash, solo CPU · 37 s · 58.027 tokens de entrada y 1.955 de salida.

## Qué pasó

El agente **descubrió y cargó la skill** `acta-reunion` sin que el encargo la nombrara, escribió `actas/2026-10-15_acta.md` y el validador de la skill dijo `ACTA VÁLIDA` a la primera.

## Veredicto del comprobador

```text
✅ existe actas/2026-10-15_acta.md (nombre que exige la skill)
  ✅ validar_acta.py dice ACTA VÁLIDA
  ✅ copia las cifras (1.800 €, 15 € de cuota)
  ✅ el agente cargó la skill

🎉 Criterio de éxito cumplido · f4
```

## Qué hay en esta carpeta

- `prompt.txt`: el encargo exacto.
- `salida.txt`: lo que dijo e hizo el agente (rutas y usuario anonimizados).
- `ficheros/`: lo que creó o cambió el agente.

> Las respuestas de un modelo cambian entre ejecuciones. Compara el **criterio**, no el texto.
