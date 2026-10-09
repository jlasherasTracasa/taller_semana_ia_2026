# 🔵 F.1 · Function calling: el modelo pide, tu programa ejecuta

> ⚙️ **Puerta F · La sala de máquinas** · 🔵 Medio · ⏱ 15 min · 🛠️ tu propio programa en Python · Recomendado para: 💻 🏛️

## 📖 La escena

—¿Y si el agente se inventa una cuenta? —pregunta Pilar. Le enseñas que el modelo ni siquiera hace la cuenta: la pide.

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

## 🔀 ¿Y ahora qué?

- **Quiero ver un servidor de tools de verdad (MCP)** → [🟣 F.5 · MCP: enchufar un servidor de herramientas](../f5_mcp/ENUNCIADO.md)
- **Quiero escribir MI propia tool** → [🟣 F.6 · Tu propia tool: plazos en días hábiles](../f6_tool_propia/ENUNCIADO.md)
- **Volver a la plaza** → [↩️ La plaza](../../AVENTURA.md#-la-plaza)
