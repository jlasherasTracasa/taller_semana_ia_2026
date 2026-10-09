---
name: acta-reunion
description: Redacta el acta oficial de una reunión de una asociación a partir de notas o de una transcripción. Úsala siempre que te pidan un acta, un resumen formal de reunión o los acuerdos de una junta.
---

# Skill · Acta de reunión

Sigue EXACTAMENTE este formato. Es el que exige el registro de asociaciones.

## Dónde guardarla
`actas/AAAA-MM-DD_acta.md`, con la fecha de la reunión (no la de hoy).

## Plantilla
```markdown
# Acta de la reunión de <órgano> · <dd/mm/aaaa>

**Lugar y hora:** <lugar>, de <hh:mm> a <hh:mm>
**Asistentes:** <nombre (cargo)>, …
**Ausencias excusadas:** <nombres o «ninguna»>

## Orden del día
1. <tema>

## Acuerdos
| N.º | Acuerdo | Votación | Responsable | Fecha límite |
|---|---|---|---|---|
| 1 | <qué se decide> | <a favor-en contra o «unanimidad»> | <nombre o «—»> | <dd/mm/aaaa o «—»> |

## Próxima reunión
<dd/mm/aaaa, hh:mm>

Firmado: <secretaria o secretario>, con el visto bueno de <presidenta o presidente>.
```

## Reglas
- Una fila por acuerdo; las tareas con responsable también son acuerdos.
- Las cifras (euros, votos) se copian tal cual de la transcripción. No inventes nada.
- Al terminar, ejecuta `python3 .opencode/skills/acta-reunion/validar_acta.py <ruta del acta>` y corrige lo que diga hasta que responda `ACTA VÁLIDA`.
