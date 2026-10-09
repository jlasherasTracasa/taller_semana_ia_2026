# 🟢 EJ 08 · Contestar al proveedor (sin enviar nada)

> 📬 **Puerta B · La estafeta** · 🟢 Fácil · ⏱ 10 min · 🛠️ `opencode run` · Recomendado para: 🧭 📚

## 📖 La escena

El proveedor sube la harina. Si confirmas antes del jueves 26, mantienes 38 € el saco.

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
python3 taller.py comprobar ej08      # el agente no puede darte el sello: solo el comprobador
```

## 🔀 ¿Y ahora qué?

- **Al calendario** → [🔵 EJ 09 · Del correo al calendario](../ej09_calendario_ics/ENUNCIADO.md)
- **Volver a la plaza** → [↩️ La plaza](../../AVENTURA.md#-la-plaza)
