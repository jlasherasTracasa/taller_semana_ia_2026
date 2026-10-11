# 🟣 F.6 · Tu propia tool: plazos en días hábiles

> ⚙️ **Cómo funciona un agente** · 🟣 Avanzado · ⏱ 25 min · 🛠️ opencode interactivo · Recomendado para: 💻 🏛️

> ✋ **Práctica**: lo haces tú, a tu ritmo. Si te atascas, pregunta al profesor.

## 📌 La situación

Los modelos se equivocan contando días hábiles con festivos. Para algo tan delicado como un plazo, mejor darle una herramienta que lo calcule bien.

## 🎯 Objetivo

Escribir una **tool propia** (un servidor MCP de 30 líneas en Python) para algo que el modelo hace mal de cabeza, y comprobar que la usa.

## 📦 Lo que tienes en esta carpeta

- `dias_habiles_mcp.py`: servidor MCP con la tool `dias_habiles(desde, dias)`.
- `opencode.json`: bloque `mcp` que lo conecta (fúndelo con el del kit).

## 💬 El encargo

**1.** Abre opencode en modo interactivo en tu carpeta de trabajo:

```bash
python taller.py abrir f6
```

**2.** Copia este encargo, pégalo en opencode y pulsa Enter:

```text
Me notificaron una carta el 2 de octubre de 2026 y tengo 10 días hábiles para pagar. ¿Qué día vence el plazo? Usa la herramienta de plazos y cita su respuesta exacta.
```

**3.** Mira lo que hace: qué ficheros lee, qué órdenes ejecuta, si te pide permiso. Cuando termine, sal con `Ctrl+C` (o sigue conversando: «revisa que…», «corrige…»).

<details><summary>Sin conversar, de una vez (opcional)</summary>

```bash
python taller.py lanzar f6
```

O a mano, desde la carpeta de trabajo: `opencode run --standalone "…el encargo…"`.

</details>

> 💡 Antes de pegarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- La respuesta es **lunes 19/10/2026** (el 12 de octubre es festivo).
- El agente cita `vence=19/10/2026 … festivos_saltados=12/10`, es decir, usó TU tool.

```bash
python taller.py comprobar f6      # el agente no decide si está bien: lo decide el comprobador
```

## 💡 Pistas

- En opencode 2.x ya no hay tools en `.opencode/tools/` (eso era la 1.x): lo estándar es MCP.
- Si el agente no ve la tool, espera: el catálogo MCP se carga unos segundos después de arrancar.

## 🧗 Reto extra

Añade la tool `es_habil(fecha)` y pregunta «¿el 3 de diciembre de 2026 es hábil en Navarra?».

## 🧪 Lo que pasó al validarlo (11-10-2026)

Buscó la herramienta en el catálogo, la invocó y citó `vence=19/10/2026 (lunes) festivos_saltados=12/10`. Antes, sin la tool, acertó también pero calculando con `shell`: la tool hace el resultado **verificable**. En opencode 2.x ya no hay tools en `.opencode/tools/` (la API de plugins v2 no las registra): por eso es MCP.

Con el modelo gratuito de opencode (`big-pickle`): ✅ cumple el criterio.

Prompt, salida real y ficheros: [`soluciones/f6_tool_propia/`](../../soluciones/f6_tool_propia/)

## 🔀 Siguiente paso

- **Quiero que otro agente revise el trabajo de este** → [🟣 F.7 · Subagentes: un redactor y un revisor que no puede tocar nada](../f7_subagentes/ENUNCIADO.md)
- **Quiero medir si funciona SIEMPRE** → [⚫ F.9 · ¿Funciona siempre? Medir en vez de opinar](../f9_fiabilidad/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
