# 🟢 EJ 08 · Borrador de respuesta a un proveedor (sin enviar nada)

> 📬 **Correo y trámites** · 🟢 Fácil · ⏱ 10 min · 🛠️ `opencode run` · Recomendado para: 🧭 📚

## 📌 La situación

El proveedor de harina sube precios: si se confirma antes del jueves 26 se mantienen 38 € el saco. Hay que contestar, sin enviar nada.

## 🎯 Objetivo

Redactar una respuesta profesional que mantenga una cifra concreta, sin enviar nada.

## 📦 Lo que tienes en esta carpeta

- `correo/bandeja/01_proveedor_urgente.eml`.

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar ej08
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Lee correo/bandeja/01_proveedor_urgente.eml y escribe un borrador de respuesta en correo/borrador_proveedor.md confirmando el pedido mensual para mantener el precio antiguo de 38 euros el saco. Tono profesional, en castellano. No envíes nada: solo el borrador." | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- `correo/borrador_proveedor.md` menciona los 38 € y el plazo del jueves 26.
- No se ha enviado nada.

```bash
python3 taller.py comprobar ej08      # el agente no decide si está bien: lo decide el comprobador
```

## 🧪 Lo que pasó al validarlo (09-10-2026)

Borrador con los 38 €/saco y el jueves 26; no envió nada.

Prompt, salida real y ficheros: [`soluciones/ej08_borrador_respuesta/`](../../soluciones/ej08_borrador_respuesta/)

## 🔀 Siguiente paso

- **Al calendario** → [🔵 EJ 09 · De un correo a un evento de calendario](../ej09_calendario_ics/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
