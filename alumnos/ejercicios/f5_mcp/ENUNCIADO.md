# 🟣 F.5 · MCP: enchufar un servidor de herramientas

> ⚙️ **Cómo funciona un agente** · 🟣 Avanzado · ⏱ 20 min · 🛠️ `opencode run` · Recomendado para: 💻 🏛️

## 📌 La situación

El ayuntamiento ya tiene un programa que hace cálculos sobre sus hojas de datos. Se trata de conectarlo al agente sin reescribirlo.

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
python3 taller.py comprobar f5      # el agente no decide si está bien: lo decide el comprobador
```

## 🧪 Lo que pasó al validarlo (09-10-2026)

Cita literalmente `filas=6 suma=29800 media=4966.67`. En opencode 2.x la tool MCP no aparece suelta: el modelo la **busca en un catálogo** y la llama escribiendo código (tool `execute`), y el catálogo puede tardar unos segundos en cargarse.

Prompt, salida real y ficheros: [`soluciones/f5_mcp/`](../../soluciones/f5_mcp/)

## 🔀 Siguiente paso

- **Ahora quiero escribir MI servidor MCP** → [🟣 F.6 · Tu propia tool: plazos en días hábiles](../f6_tool_propia/ENUNCIADO.md)
- **¿Y si el servidor MCP es malicioso?** → [⚫ F.8 · Auditar permisos: ¿qué puede hacer tu agente sin preguntarte?](../f8_permisos/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
