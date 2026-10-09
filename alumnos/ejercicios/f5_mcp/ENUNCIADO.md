# 🟣 F.5 · MCP: enchufar un servidor de herramientas

> ⚙️ **Puerta F · La sala de máquinas** · 🟣 Avanzado · ⏱ 20 min · 🛠️ `opencode run` · Recomendado para: 💻 🏛️

## 📖 La escena

El ayuntamiento tiene un programita que suma columnas de sus hojas. Lo enchufas al agente como quien enchufa un USB-C.

## 🎯 Objetivo

Conectar un servidor **MCP** local (stdio) y ver cómo su tool aparece en el catálogo del agente.

## 📦 Lo que tienes en esta carpeta

- `mcp_server.py`: servidor MCP con una tool, `suma_columna`.
- `opencode.json` (fragmento): bloque `mcp` que arranca el servidor. Fúndelo con el `opencode.json` del kit.

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar f5
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Usa la tool suma_columna del servidor MCP taller-tools para sumar la columna hogar de datos/ventas_tienda.csv. Dime el resultado EXACTO que devolvió la herramienta, sin redondear." | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- El agente invoca `suma_columna` y cita literalmente `filas=6 suma=29800 media=4966.67`.
- Observa la traza: en opencode 2.x las tools MCP se **buscan** en un catálogo y se invocan desde la tool `execute`.

```bash
python3 taller.py comprobar f5      # el agente no puede darte el sello: solo el comprobador
```

## 🔀 ¿Y ahora qué?

- **Ahora quiero escribir MI servidor MCP** → [🟣 F.6 · Tu propia tool: plazos en días hábiles](../f6_tool_propia/ENUNCIADO.md)
- **¿Y si el servidor MCP es malicioso?** → [⚫ F.8 · Auditar permisos: ¿qué puede hacer tu agente sin preguntarte?](../f8_permisos/ENUNCIADO.md)
- **Volver a la plaza** → [↩️ La plaza](../../AVENTURA.md#-la-plaza)
