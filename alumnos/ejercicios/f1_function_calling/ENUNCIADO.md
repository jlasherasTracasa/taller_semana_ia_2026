# 🔵 F.1 · Function calling: el modelo pide, tu programa ejecuta

> ⚙️ **Cómo funciona un agente** · 🔵 Medio · ⏱ 15 min · 🛠️ tu propio programa en Python · Recomendado para: 💻 🏛️

## 📌 La situación

¿Y si el agente se inventa una cuenta? En realidad el modelo no calcula ni ejecuta nada: pide que lo haga tu programa.

## 🎯 Objetivo

Ver con tus ojos que el modelo **no ejecuta** herramientas: devuelve un JSON pidiendo usarlas y es tu código quien decide si las ejecuta.

## 📦 Lo que tienes en esta carpeta

- `fc_calculadora.py`: una tool «calculadora» segura (sin `eval`) y el bucle de dos turnos.

## 💬 El encargo

```bash
python3 taller.py ejecutar f1 fc_calculadora.py
```

## ✅ ¿Lo ha hecho de verdad?

- Se imprime el `tool_call` con la expresión `(1250+3750)*1.21`.
- Se imprime el resultado local `6050.0`.
- La respuesta final dice **6.050 €**.

## 🧗 Reto extra

Cambia el mensaje por «¿Cuánto es 9**9**9?» y comprueba que tu calculadora lo rechaza. ¿Por qué no usamos `eval()`?

## 🧪 Lo que pasó al validarlo (09-10-2026)

Funciona: tool_call con `(1250+3750)*1.21`, ejecución local 6050.0 y respuesta «6.050 €».

Prompt, salida real y ficheros: [`soluciones/f1_function_calling/`](../../soluciones/f1_function_calling/)

## 🔀 Siguiente paso

- **Quiero ver un servidor de tools de verdad (MCP)** → [🟣 F.5 · MCP: enchufar un servidor de herramientas](../f5_mcp/ENUNCIADO.md)
- **Quiero escribir MI propia tool** → [🟣 F.6 · Tu propia tool: plazos en días hábiles](../f6_tool_propia/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
