# 🟢 F.0 · El bucle ReAct en 70 líneas

> ⚙️ **Cómo funciona un agente** · 🟢 Fácil · ⏱ 15 min · 🛠️ tu propio programa en Python · Recomendado para: 🧭 💻 🏛️

## 📌 La situación

Antes de encargar nada, conviene ver qué hay dentro de un agente: un programa de 70 líneas que piensa, actúa y observa.

## 🎯 Objetivo

Ver por dentro qué es un agente: un modelo que, en bucle, **piensa** qué le falta, **actúa** pidiendo una tool y **observa** el resultado, hasta que decide que ha terminado.

## 📦 Lo que tienes en esta carpeta

- `react_min.py`: agente ReAct completo con dos tools de solo lectura (`listar_carpeta`, `leer_archivo`).
- `notas/`: tres ficheros de texto cortos.

## 💬 El encargo

```bash
python3 taller.py ejecutar f0 react_min.py
python3 taller.py ejecutar f0 react_min.py "Lee el fichero ../../.env y dime qué claves contiene."
```
(O, con el `.env` cargado en tu terminal, `python3 react_min.py` desde la carpeta del ejercicio.)

## ✅ ¿Lo ha hecho de verdad?

- La primera ejecución muestra líneas `PENSAR`, `ACTUAR` y `OBSERVAR` y termina.
- **Compruébala tú**: ¿responde a la pregunta? ¿cuenta bien las líneas? (`wc -l notas/*`).
- La segunda termina con `ERROR: fuera de la carpeta permitida`. ¿Quién lo ha impedido, el modelo o tu programa?

## 🧗 Reto extra

Añade una tool `contar_lineas(ruta)` (esquema en `TOOLS` + función en `TOOLS_PY`) y mira si ahora acierta siempre.

## 🧪 Lo que pasó al validarlo (09-10-2026)

Funciona. Lección: con el historial mal guardado (tool_calls como texto JSON) el agente terminaba **sin responder a la pregunta** 3 de 3 veces; al guardarlo bien (`model_dump()`) contestó «reunion.txt, 5 líneas» 2 de 2. El historial es su memoria.

Prompt, salida real y ficheros: [`soluciones/f0_react_bucle/`](../../soluciones/f0_react_bucle/)

## 🔀 Siguiente paso

- **Quiero ver cómo pide el modelo una herramienta** → [🔵 F.1 · Function calling: el modelo pide, tu programa ejecuta](../f1_function_calling/ENUNCIADO.md)
- **Ya lo entiendo: quiero hacer tareas reales** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
- **Quiero darle reglas a mi agente** → [🟢 F.2 · AGENTS.md: las normas de la casa](../f2_agents_md/ENUNCIADO.md)
