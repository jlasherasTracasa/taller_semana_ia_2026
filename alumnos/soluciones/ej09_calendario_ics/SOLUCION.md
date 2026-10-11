# ✅ Solución · EJ 09 · De un correo a un evento de calendario

Ejecución real del 11-10-2026 con opencode 2.0.19 y GLM-5.3-Flash, solo CPU · 69 s · 170.803 tokens de entrada y 7.230 de salida.

Con el modelo gratuito de opencode (`big-pickle`): ✅ también cumple el criterio.

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
