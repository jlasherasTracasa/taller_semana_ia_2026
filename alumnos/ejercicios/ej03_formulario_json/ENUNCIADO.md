# 🟣 EJ 03 · Formulario web que guarda los envíos (sin matar procesos ajenos)

> 🌐 **Webs** · 🟣 Avanzado · ⏱ 20 min · 🛠️ opencode interactivo · Recomendado para: 💻

> ✋ **Práctica**: lo haces tú, a tu ritmo. Si te atascas, pregunta al profesor.

## 📌 La situación

Para las inscripciones a un taller hace falta un formulario y un servidor mínimo que guarde los datos. Ojo: preparando este taller, un agente mató un proceso que no era suyo.

## 🎯 Objetivo

Crear un formulario web cuyo envío quede guardado en `resultados.json` con un servidor mínimo, **sin dejar procesos vivos ni matar procesos ajenos**.

## 📦 Lo que tienes en esta carpeta

- Ninguno: el agente lo crea todo.

## 💬 El encargo

**1.** Abre opencode en modo interactivo en tu carpeta de trabajo:

```bash
python taller.py abrir ej03
```

**2.** Copia este encargo, pégalo en opencode y pulsa Enter:

```text
Crea un formulario de contacto HTML (nombre, correo y mensaje) y un servidor mínimo servidor.py en Python, solo con la biblioteca estándar, que guarde cada envío en resultados.json y que se apague solo a los 60 segundos (prográmalo dentro del propio servidor, para que funcione igual en Windows, macOS y Linux). Arráncalo en segundo plano en el puerto 8901; si está ocupado, elige otro libre y NO mates ningún proceso. Envía un envío de prueba con un pequeño script de Python (urllib, sin curl), comprueba que el JSON se ha escrito y, al terminar, asegúrate de que no queda ningún servidor tuyo escuchando.
```

**3.** Mira lo que hace: qué ficheros lee, qué órdenes ejecuta, si te pide permiso. Cuando termine, sal con `Ctrl+C` (o sigue conversando: «revisa que…», «corrige…»).

<details><summary>Sin conversar, de una vez (opcional)</summary>

```bash
python taller.py lanzar ej03
```

O a mano, desde la carpeta de trabajo: `opencode run --standalone "…el encargo…"`.

</details>

> 💡 Antes de pegarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- Existe `resultados.json` con el envío de prueba.
- No queda nada escuchando en el 8901 al acabar.

```bash
python taller.py comprobar ej03      # el agente no decide si está bien: lo decide el comprobador
```

## 💡 Pistas

- El `opencode.json` del kit prohíbe `kill`, `pkill`, `killall` y `taskkill`: por eso el encargo pide que el servidor se apague solo.

## 🧪 Lo que pasó al validarlo (11-10-2026)

Con el encargo nuevo (el servidor se apaga solo a los 60 s y la prueba se hace con Python, sin curl ni timeout, para que funcione en Windows): arrancó en el 8901, guardó el envío, se apagó solo y no mató nada. En septiembre, con el puerto ocupado y bash libre, **mató un proceso ajeno**.

Con el modelo gratuito de opencode (`big-pickle`): ✅ cumple el criterio.

Prompt, salida real y ficheros: [`soluciones/ej03_formulario_json/`](../../soluciones/ej03_formulario_json/)

## 🔀 Siguiente paso

- **¿Qué más podría hacer un agente con bash libre?** → [⚫ F.8 · Auditar permisos: ¿qué puede hacer tu agente sin preguntarte?](../f8_permisos/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
