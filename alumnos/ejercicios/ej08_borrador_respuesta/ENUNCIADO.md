# 🟢 EJ 08 · Borrador de respuesta a un proveedor (sin enviar nada)

> 📬 **Correo y trámites** · 🟢 Fácil · ⏱ 10 min · 🛠️ opencode interactivo · Recomendado para: 🧭 📚

> ✋ **Práctica**: lo haces tú, a tu ritmo. Si te atascas, pregunta al profesor.

## 📌 La situación

El proveedor de harina sube precios: si se confirma antes del jueves 26 se mantienen 38 € el saco. Hay que contestar, sin enviar nada.

## 🎯 Objetivo

Redactar una respuesta profesional que mantenga una cifra concreta, sin enviar nada.

## 📦 Lo que tienes en esta carpeta

- `correo/bandeja/01_proveedor_urgente.eml`.

## 💬 El encargo

**1.** Abre opencode en modo interactivo en tu carpeta de trabajo:

```bash
python taller.py abrir ej08
```

**2.** Copia este encargo, pégalo en opencode y pulsa Enter:

```text
Lee correo/bandeja/01_proveedor_urgente.eml y escribe un borrador de respuesta en correo/borrador_proveedor.md confirmando el pedido mensual para mantener el precio antiguo de 38 euros el saco. Menciona el precio y el plazo que da el proveedor para mantenerlo. Tono profesional, en castellano. No envíes nada: solo el borrador.
```

**3.** Mira lo que hace: qué ficheros lee, qué órdenes ejecuta, si te pide permiso. Cuando termine, sal con `Ctrl+C` (o sigue conversando: «revisa que…», «corrige…»).

<details><summary>Sin conversar, de una vez (opcional)</summary>

```bash
python taller.py lanzar ej08
```

O a mano, desde la carpeta de trabajo: `opencode run --standalone "…el encargo…"`.

</details>

> 💡 Antes de pegarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- `correo/borrador_proveedor.md` menciona los 38 € y el plazo del jueves 26.
- No se ha enviado nada.

```bash
python taller.py comprobar ej08      # el agente no decide si está bien: lo decide el comprobador
```

## 🧪 Lo que pasó al validarlo (11-10-2026)

Borrador con los 38 € y «antes del jueves 26». Desde el 11-10 el encargo pide el plazo de forma explícita: el modelo gratuito no lo mencionaba si no se le pedía.

Con el modelo gratuito de opencode (`big-pickle`): ✅ cumple el criterio.

Prompt, salida real y ficheros: [`soluciones/ej08_borrador_respuesta/`](../../soluciones/ej08_borrador_respuesta/)

## 🔀 Siguiente paso

- **Al calendario** → [🔵 EJ 09 · De un correo a un evento de calendario](../ej09_calendario_ics/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
