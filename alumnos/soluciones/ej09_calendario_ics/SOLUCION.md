# ✅ Solución · EJ 09 · Del correo al calendario

Ejecución real del 09-10-2026 con opencode 2.0.19 y GLM-5.3-Flash, solo CPU · 27 s · 55.423 tokens de entrada y 2.100 de salida.

## Qué pasó

DTSTART 28/11/2026 10:00 con `TZID=Europe/Madrid` y bloque VTIMEZONE, validado con `icalendar`. En la ronda 1 dejó la hora «flotante», sin zona horaria.

## Veredicto del comprobador

```text
✅ existe taller_pan.ics
  ✅ estructura VCALENDAR/VEVENT
  ✅ empieza a las 10:00 (20261128T1000)
  ✅ el día es el sábado 28/11/2026
  ✅ tiene final (DTEND o DURATION)
  ✅ zona horaria explícita

🎉 Criterio de éxito cumplido · ej09
```

## Qué hay en esta carpeta

- `prompt.txt`: el encargo exacto.
- `salida.txt`: lo que dijo e hizo el agente (rutas y usuario anonimizados).
- `ficheros/`: lo que creó o cambió el agente.

> Las respuestas de un modelo cambian entre ejecuciones. Compara el **criterio**, no el texto.
