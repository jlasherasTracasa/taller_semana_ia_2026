# 🔵 F.1 · Function calling: el modelo pide, tu programa ejecuta

> ⚙️ **Cómo funciona un agente** · 🔵 Medio · ⏱ 15 min · 🛠️ tu propio programa en Python · Recomendado para: 💻 🏛️

> 🎥 **Demo en directo**: lo hace el profesor en el proyector; tú lo miras y lo repites después si quieres.

## 📌 La situación

¿Y si el agente se inventa una cuenta? En realidad el modelo no calcula ni ejecuta nada: pide que lo haga tu programa.

## 🎯 Objetivo

Ver con tus ojos que el modelo **no ejecuta** herramientas: devuelve un JSON pidiendo usarlas y es tu código quien decide si las ejecuta.

## 📦 Lo que tienes en esta carpeta

- `fc_calculadora.py`: una tool «calculadora» segura (sin `eval`) y el bucle que se la ofrece al modelo.

## 💬 El encargo

Como F.0, aquí **no se usa opencode**: las órdenes se escriben en la terminal, desde la carpeta `alumnos` y con el
entorno activado. Necesita una clave en `.env`: `OPENROUTER_API_KEY`, o una gratuita de Groq (`GROQ_API_KEY`; paso a
paso en la wiki, «Modelos»).

**1.** Ejecuta la demo con su pregunta de serie (el total de un pedido con IVA):

```bash
python taller.py ejecutar f1 fc_calculadora.py
```

Fíjate en las tres partes: `RESPUESTA 1 DEL MODELO` (no trae texto, trae un `tool_calls` en JSON), `EJECUCIÓN LOCAL`
(la cuenta la hace tu programa) y `RESPUESTA 2 DEL MODELO` (el texto final, ya con el resultado).

**2.** Hazle tu propia pregunta: escríbela **entre comillas** detrás del nombre del programa:

```bash
python taller.py ejecutar f1 fc_calculadora.py "Compro 3 libros de 18,50 € y 2 de 12 €. ¿Cuánto pago?"
```

## ✅ ¿Lo ha hecho de verdad?

- Se imprime el `tool_call` con la expresión `(1250+3750)*1.21`.
- Se imprime el resultado local `6050.0`.
- La respuesta final dice **6.050 €**.

## 🧗 Reto extra

Los argumentos de la tool los escribe el modelo (o un atacante, con una inyección de prompt). ¿Qué pasa si llega
algo peligroso? Prueba la calculadora **sin el modelo** (no gasta clave) con `--sin-modelo` y la expresión entre comillas:

```bash
python taller.py ejecutar f1 fc_calculadora.py --sin-modelo "9**9**9"
python taller.py ejecutar f1 fc_calculadora.py --sin-modelo "__import__('os')"
```

Las dos dan `ERROR: operación no permitida`. Con `eval()`, la primera dejaría el ordenador calculando un número de
369 millones de cifras y la segunda podría ejecutar cualquier cosa. Pregúntaselo después al modelo:

```bash
python taller.py ejecutar f1 fc_calculadora.py "¿Cuánto es 9**9**9?"
```

¿Le pasa a la calculadora la expresión tal cual, la cambia o se niega? Recuerda: quien decide qué se ejecuta es tu programa.

## 📂 Una solución de ejemplo

¿Te has atascado o no puedes ejecutarlo? Mira lo que hizo el agente con este encargo (el encargo, lo que escribió en pantalla y los ficheros): [`soluciones/f1_function_calling/`](../../soluciones/f1_function_calling/)

## 🔀 Siguiente paso

- **Quiero ver un servidor de tools de verdad (MCP)** → [🟣 F.5 · MCP: enchufar un servidor de herramientas](../f5_mcp/ENUNCIADO.md)
- **Quiero escribir MI propia tool** → [🟣 F.6 · Tu propia tool: plazos en días hábiles](../f6_tool_propia/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
