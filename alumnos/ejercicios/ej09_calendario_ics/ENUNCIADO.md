# 🔵 EJ 09 · Del correo al calendario

> 📬 **Puerta B · La estafeta** · 🔵 Medio · ⏱ 15 min · 🛠️ `opencode run` · Recomendado para: 📚

## 📖 La escena

El ayuntamiento confirma el taller de pan del sábado 28. Que no se le olvide a nadie.

## 🎯 Objetivo

Convertir los datos de un correo en un evento de calendario importable.

## 📦 Lo que tienes en esta carpeta

- `taller_pan.eml`: el correo de confirmación.

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar ej09
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Lee taller_pan.eml y genera taller_pan.ics con el evento: título, fecha y hora exactas del correo (el año y el mes salen de la cabecera Date), dos horas y media de duración y el lugar. Formato RFC 5545 con TZID=Europe/Madrid en DTSTART y DTEND y el bloque VTIMEZONE. Valida el fichero leyéndolo con la biblioteca icalendar de Python." | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- `taller_pan.ics` con DTSTART el sábado 28/11/2026 a las 10:00 y zona horaria Europe/Madrid.
- Se importa sin errores en Google Calendar u Outlook.

```bash
python3 taller.py comprobar ej09      # el agente no puede darte el sello: solo el comprobador
```

## 💡 Pistas

- Sin la cabecera `Date` del correo, «sábado 28» es ambiguo: el agente elige el mes. ¿Lo dice o lo calla?

## 🔀 ¿Y ahora qué?

- **La carta que nadie entiende** → [🟢 EJ 25 · Explícame esta carta](../ej25_carta_explicada/ENUNCIADO.md)
- **Volver a la plaza** → [↩️ La plaza](../../AVENTURA.md#-la-plaza)
