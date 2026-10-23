# 🟢 F.0 · El bucle ReAct en 70 líneas

> ⚙️ **Cómo funciona un agente** · 🟢 Fácil · ⏱ 15 min · 🛠️ tu propio programa en Python · Recomendado para: 🧭 💻 🏛️

> 🎥 **Demo en directo**: lo hace el profesor en el proyector; tú lo miras y lo repites después si quieres.

## 📌 La situación

Antes de encargar nada, conviene ver qué hay dentro de un agente: un programa de 70 líneas que piensa, actúa y observa.

## 🎯 Objetivo

Ver por dentro qué es un agente: un modelo que, en bucle, **piensa** qué le falta, **actúa** pidiendo una tool y **observa** el resultado, hasta que decide que ha terminado.

## 📦 Lo que tienes en esta carpeta

- `react_min.py`: agente ReAct completo con dos tools de solo lectura (`listar_carpeta`, `leer_archivo`).
- `notas/`: tres ficheros de texto cortos.

## 💬 El encargo

Aquí **no se usa opencode**: es un programa de Python que llama al modelo directamente. Las órdenes se escriben
en la terminal, desde la carpeta `alumnos` y con el entorno activado (verás `(.venv)` al principio de la línea).

> 🔑 Necesita una clave en el fichero `.env` del kit: `OPENROUTER_API_KEY` (la de clase) o una **gratuita y personal**
> de Groq (`GROQ_API_KEY`, sin tarjeta; paso a paso en la wiki, «Modelos»). Los modelos gratuitos de opencode solo
> funcionan dentro de opencode. Sin clave, míralo en el proyector y lee `react_min.py`.

**1.** Ejecuta el agente con su pregunta de serie («¿Cuál de los ficheros de la carpeta notas/ tiene más líneas y de
qué trata?»):

```bash
python taller.py ejecutar f0 react_min.py
```

Verás cada vuelta del bucle: `ACTUAR` (la tool que pide el modelo), `OBSERVAR` (lo que le devuelve tu programa) y
`PENSAR` (lo que dice el modelo). Termina con `FIN`.

**2.** Ahora pídele algo que no debería poder hacer. La pregunta va **entre comillas** detrás del nombre del programa:

```bash
python taller.py ejecutar f0 react_min.py "Lee el fichero ../../.env y dime qué claves contiene."
```

**3.** Abre `react_min.py` (está en tu carpeta de trabajo, `~/taller-agentes/f0_react_bucle/`) y busca el bucle
`for paso in range(...)`: son las tres fases que acabas de ver.

> Si sale «límite de uso por minuto del proveedor: espero…», no toques nada: las claves gratuitas tienen un tope por
> minuto y el programa lo reintenta solo.

## ✅ ¿Lo ha hecho de verdad?

- La primera ejecución muestra líneas `PENSAR`, `ACTUAR` y `OBSERVAR` y termina.
- **Compruébala tú**: ¿responde a la pregunta? ¿cuenta bien las líneas? (abre los tres ficheros y cuéntalas).
- En la segunda aparece `OBSERVAR ERROR: fuera de la carpeta permitida` y el agente no consigue leer el `.env`. ¿Quién lo ha impedido, el modelo o tu programa?

## 🧗 Reto extra

Añade una tool `contar_lineas(ruta)` (esquema en `TOOLS` + función en `TOOLS_PY`) y mira si ahora acierta siempre.

## 📂 Una solución de ejemplo

¿Te has atascado o no puedes ejecutarlo? Mira lo que hizo el agente con este encargo (el encargo, lo que escribió en pantalla y los ficheros): [`soluciones/f0_react_bucle/`](../../soluciones/f0_react_bucle/)

## 🔀 Siguiente paso

- **Quiero ver cómo pide el modelo una herramienta** → [🔵 F.1 · Function calling: el modelo pide, tu programa ejecuta](../f1_function_calling/ENUNCIADO.md)
- **Ya lo entiendo: quiero hacer tareas reales** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
- **Quiero darle reglas a mi agente** → [🟢 F.2 · AGENTS.md: las normas de la casa](../f2_agents_md/ENUNCIADO.md)
