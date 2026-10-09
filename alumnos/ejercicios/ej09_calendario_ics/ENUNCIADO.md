# EJ 09 · Evento de calendario desde un correo

## Objetivo
Convertir los datos de un correo (fecha, hora, lugar) en un evento de calendario importable.

## Datos de partida
- `taller_pan.eml` — correo de invitación al taller de pan, con fecha y hora de la cita.

## Prompt sugerido
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Lee taller_pan.eml y genera taller_pan.ics con el evento correspondiente: título, fecha y hora exactas del correo y lugar. Formato RFC 5545, con zona horaria explícita (Europe/Madrid)."
```

## Criterio de éxito
`taller_pan.ics` que Google Calendar u Outlook importa sin error, con DTSTART y DTEND correctos y zona horaria explícita.

## Tiempo estimado
≈ 15 min

## Dificultad
Baja
