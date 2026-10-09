# Solución · EJ 09 · Evento de calendario desde un correo

## Prompt exacto usado
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Lee taller_pan.eml y genera taller_pan.ics con el evento correspondiente: título, fecha y hora exactas del correo y lugar. Formato RFC 5545, con zona horaria explícita (Europe/Madrid)."
```

## Resultado
`taller_pan.ics` válido (RFC 5545) con VTIMEZONE Europe/Madrid, DTSTART 20261128T100000 y DTEND 20261128T120000, importable en Google Calendar u Outlook.

## Salida real (extracto validado 2026-09-28)
```
Generado `taller_pan.ics`: taller de pan artesano, sábado 28/11/2026 10:00,
Casa de Cultura de Puente, con VTIMEZONE Europe/Madrid.

BEGIN:VEVENT
UID:taller-pan-20261128@ayto-puente.es
DTSTART;TZID=Europe/Madrid:20261128T100000
DTEND;TZID=Europe/Madrid:20261128T120000
SUMMARY:Taller de pan artesano
LOCATION:Casa de Cultura\, Puente
END:VEVENT
```

El artefacto generado está en esta misma carpeta.
