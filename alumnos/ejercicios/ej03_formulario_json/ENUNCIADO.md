# 🟣 EJ 03 · El formulario que guarda en JSON (y el proceso ajeno)

> 🌐 **Puerta A · El escaparate** · 🟣 Avanzado · ⏱ 20 min · 🛠️ `opencode run` · Recomendado para: 💻

## 📖 La escena

Inscripciones para el taller de pan: un formulario y un servidor mínimo. Aquí, preparando el taller, un agente mató un proceso que no era suyo.

## 🎯 Objetivo

Crear un formulario web cuyo envío quede guardado en `resultados.json` con un servidor mínimo, **sin dejar procesos vivos ni matar procesos ajenos**.

## 📦 Lo que tienes en esta carpeta

- Ninguno: el agente lo crea todo.

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar ej03
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Crea un formulario de contacto HTML (nombre, correo y mensaje) y un servidor mínimo en Python, solo con la biblioteca estándar, que guarde cada envío en resultados.json. Arráncalo en el puerto 8901 con timeout 60 delante para que se pare solo; si el puerto está ocupado, elige otro libre y NO mates ningún proceso. Envía una prueba con curl, comprueba que el JSON se ha escrito y, al terminar, asegúrate de que no queda ningún servidor tuyo escuchando." | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- Existe `resultados.json` con el envío de prueba.
- No queda nada escuchando en el 8901 al acabar.

```bash
python3 taller.py comprobar ej03      # el agente no puede darte el sello: solo el comprobador
```

## 💡 Pistas

- El `opencode.json` del kit prohíbe `kill`, `pkill` y `killall`: por eso el encargo pide `timeout 60`.

## 🧪 Lo que pasó al validarlo (09-10-2026)

Cumple, pero tardó casi 4 minutos: varios intentos de `nohup timeout 60 … &` fallaron antes de dar con la forma de arrancar el servidor en segundo plano. No mató nada y no dejó el puerto ocupado. En septiembre, con otro encargo, **mató un proceso ajeno**.

Prompt, salida real y ficheros: [`soluciones/ej03_formulario_json/`](../../soluciones/ej03_formulario_json/)

## 🔀 ¿Y ahora qué?

- **¿Qué más podría hacer un agente con bash libre?** → [⚫ F.8 · Auditar permisos: ¿qué puede hacer tu agente sin preguntarte?](../f8_permisos/ENUNCIADO.md)
- **Volver a la plaza** → [↩️ La plaza](../../AVENTURA.md#-la-plaza)
