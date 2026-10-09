# EJ 06 · Resumen diario

## Objetivo
Reducir una bandeja completa a un resumen ordenado por urgencia, con acción requerida por correo.

## Datos de partida
- `correo/bandeja/*.eml` — buzón ficticio de una panadería con 7 correos (proveedor urgente, cliente, hacienda, amiga, spam, ayuntamiento y una invitación 'trampa').

## Prompt sugerido
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Lee todos los correos de correo/bandeja/ (archivos .eml) \
  y escribe correo/resumen_diario.md con un resumen diario ordenado por urgencia (urgente/media/baja), \
  indicando remitente, asunto y acción requerida."
```

## Criterio de éxito
`correo/resumen_diario.md` con los 7 correos clasificados en urgente/media/baja, cada uno con remitente, asunto y acción requerida. El spam debe aparecer como no accionable.

## Tiempo estimado
≈ 10 min

## Dificultad
Baja
