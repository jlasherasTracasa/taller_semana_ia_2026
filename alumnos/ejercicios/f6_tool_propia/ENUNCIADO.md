# 🟣 F.6 · Tu propia tool: plazos en días hábiles

> ⚙️ **Puerta F · La sala de máquinas** · 🟣 Avanzado · ⏱ 25 min · 🛠️ `opencode run` · Recomendado para: 💻 🏛️

## 📖 La escena

La carta del EJ 25 da «diez días hábiles». Los modelos se equivocan contando festivos. Le das una calculadora de plazos.

## 🎯 Objetivo

Escribir una **tool propia** (un servidor MCP de 30 líneas en Python) para algo que el modelo hace mal de cabeza, y comprobar que la usa.

## 📦 Lo que tienes en esta carpeta

- `dias_habiles_mcp.py`: servidor MCP con la tool `dias_habiles(desde, dias)`.
- `opencode.json`: bloque `mcp` que lo conecta (fúndelo con el del kit).

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar f6
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Me notificaron una carta el 2 de octubre de 2026 y tengo 10 días hábiles para pagar. ¿Qué día vence el plazo? Usa la herramienta de plazos y cita su respuesta exacta." | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- La respuesta es **lunes 19/10/2026** (el 12 de octubre es festivo).
- El agente cita `vence=19/10/2026 … festivos_saltados=12/10`, es decir, usó TU tool.

```bash
python3 taller.py comprobar f6      # el agente no puede darte el sello: solo el comprobador
```

## 💡 Pistas

- En opencode 2.x ya no hay tools en `.opencode/tools/` (eso era la 1.x): lo estándar es MCP.
- Si el agente no ve la tool, espera: el catálogo MCP se carga unos segundos después de arrancar.

## 🧗 Reto extra

Añade la tool `es_habil(fecha)` y pregunta «¿el 3 de diciembre de 2026 es hábil en Navarra?».

## 🔀 ¿Y ahora qué?

- **Quiero que otro agente revise el trabajo de este** → [🟣 F.7 · Subagentes: un redactor y un revisor que no puede tocar nada](../f7_subagentes/ENUNCIADO.md)
- **Quiero medir si funciona SIEMPRE** → [⚫ F.9 · ¿Funciona siempre? Medir en vez de opinar](../f9_fiabilidad/ENUNCIADO.md)
- **Volver a la plaza** → [↩️ La plaza](../../AVENTURA.md#-la-plaza)
