# 🔧 Problemas y soluciones

Primero, siempre: `python taller.py entorno`. Te dice qué falta y cómo arreglarlo.

## «No sé qué hacer» (lo más preguntado)

| Duda | Respuesta |
|---|---|
| ¿Qué tengo que pegar en opencode? | El texto del bloque **«💬 El encargo»** del enunciado (en la web, el que tiene el botón **Copiar**). `python taller.py abrir <ej>` también lo enseña antes de abrir opencode. Si el enunciado tiene **pasos numerados** (F.2, F.3, EJ 10, EJ 21), síguelos en orden: cada paso dice qué pegar |
| He escrito `python taller.py …` dentro de opencode y no pasa nada (o el agente lo ejecuta) | Las órdenes `python taller.py …` van en la **terminal**, fuera de opencode. Sal con `Ctrl+C` (con la caja vacía) y escríbela ahí. Dentro de opencode solo va el encargo o un comando que empieza por `/` |
| F.0, F.1: ¿dónde pego el encargo? | En ninguna parte: **no usan opencode**. Son programas de Python que se lanzan con `python taller.py ejecutar …` |
| F.0, F.1: ¿cómo le hago otra pregunta (por ejemplo «¿Cuánto es 9\*\*9\*\*9?»)? | Escríbela **entre comillas** al final de la orden: `python taller.py ejecutar f1 fc_calculadora.py "¿Cuánto es 9**9**9?"`. Para probar la calculadora sin el modelo: `python taller.py ejecutar f1 fc_calculadora.py --sin-modelo "9**9**9"` |
| F.1: el modelo no le pasa `9**9**9` a la calculadora | Es normal: el modelo elige los argumentos y a veces cambia la cuenta o se niega. Por eso existe `--sin-modelo`, para ver qué hace tu calculadora con esa expresión |
| F.0 o F.1: `(límite de uso por minuto del proveedor: espero…)` | La clave gratuita de Groq admite 8.000 tokens por minuto. No toques nada: el programa espera y lo reintenta solo |
| F.0 o F.1: `(el modelo no ha dicho nada: le pido que siga)` | El modelo gratuito ha respondido en blanco. El programa se lo vuelve a pedir; no hay que hacer nada |
| `comprobar f0` (o `f1`) dice que no tiene comprobador | F.0, F.1 y F.9 son programas que miras tú: repasa la lista «✅ ¿Lo ha hecho de verdad?» del enunciado |
| F.2: ¿dónde está mi carpeta de trabajo para copiar `AGENTS.md`? | En `~/taller-agentes/f2_agents_md/` (en Windows, `C:\Users\<tú>\taller-agentes\f2_agents_md\`). `python taller.py empezar f2` te la dice |
| F.3: he escrito `/informe-semanal` y no hace nada | Al escribir `/` sale una lista: el primer **Enter** elige el comando y el segundo **Enter** lo envía |

## Instalación

| Síntoma | Por qué pasa | Arreglo |
|---|---|---|
| `Free usage limit reached. Subscribe to OpenCode Go…` o `Rate limit exceeded` | El modelo gratuito de opencode ha agotado su cupo desde tu conexión | **No hace falta pagar.** Pasos con capturas en [🤖 Modelos](Modelos.md#-si-se-acaba-el-modelo-gratuito) |
| 🖥️ Codespace: «Do you trust the authors of the files in this folder?» | VS Code abre el repositorio en modo restringido | Pulsa **Trust Folder & Continue** ([🆘 Plan B](Plan-B.md)) |
| 🪟 `python` o `py` «no se reconoce» | Python no está instalado o no está en el PATH | [🛠️ Instalar](Instalar.md). Reinstala marcando «Add python.exe to PATH» y abre otra PowerShell |
| 🪟 `python3` o `python` abre la Microsoft Store | Windows trae un alias que no es Python | Usa `py` para crear el `.venv`; dentro del entorno, `python`. O quita el alias en *Configuración → Aplicaciones → Alias de ejecución de aplicaciones* |
| 🪟 `Activate.ps1 no se puede cargar… ejecución de scripts deshabilitada` | Política de PowerShell | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` y repite |
| 🪟 `opencode`, `node` o `npm` no se encuentran | La PowerShell se abrió antes de instalar | Cierra PowerShell y abre otra |
| 🪟 `winget` pide administrador o no existe | Ordenador de aula o Windows antiguo | Instaladores de python.org y nodejs.org, o el [🆘 Plan B](Plan-B.md) |
| 🐧 `The virtual environment was not created successfully` | En Ubuntu/Debian falta `python3-venv` | `sudo apt install python3-venv` |
| 🐧 `npm i -g` da `EACCES: permission denied` | El Node del sistema instala «para todos» | `npm config set prefix ~/.npm-global`, añade `export PATH="$HOME/.npm-global/bin:$PATH"` a `~/.bashrc`, abre otra terminal y repite. O el Node en tu carpeta de [Instalar](Instalar.md) |
| 🐧 `node --version` menor que v18 | Ubuntu 22.04 o anterior | El Node en tu carpeta de [Instalar](Instalar.md) |
| 🍎 Python 3.9 o anterior | El del sistema es antiguo | `brew install python@3.12` |
| `opencode --version` dice 1.x | Se instaló el paquete antiguo `opencode-ai` | `npm uninstall -g opencode-ai` y `npm i -g @opencode/cli@2.0.19` |
| `No module named pptx` (u openpyxl, reportlab…) | Faltan las bibliotecas | Con el entorno activado: `python -m pip install -r requirements.txt` |

## El modelo

| Síntoma | Por qué pasa | Arreglo |
|---|---|---|
| `Error: Invalid URL` o `No api key passed in` | opencode 2.x manda el trabajo a un **servicio en segundo plano** que arrancó antes de que cargaras tu `.env` | Usa `python taller.py abrir …`/`lanzar …` o añade `--standalone`. También vale `opencode service restart` |
| El modelo gratuito no contesta, va muy lento o da error de límite | Mucha gente a la vez por la misma conexión, o el modelo ha dejado de ser gratuito | Espera un minuto; prueba otro con `/models`; usa la clave de OpenRouter ([🤖 Modelos](Modelos.md)) |
| F.0 o F.1: «necesita una clave en el .env del kit» | Son programas de Python: los modelos gratuitos de opencode solo funcionan dentro de opencode | Pon en `.env` la clave de OpenRouter o una gratuita de Groq ([🤖 Modelos](Modelos.md), paso a paso), o mira la demo del profesor |
| F.0 o F.1 con Gemini o Groq: `404`, `model not found` o `does not support tools` | El modelo gratuito ha cambiado de nombre o ya no es gratuito | Busca uno actual con *tool calling* y ponlo en `.env` con `TALLER_MODELO_PY=` ([🤖 Modelos](Modelos.md)) |
| F.0 o F.1 con Gemini o Groq: `429` o `RESOURCE_EXHAUSTED` | Límite por minuto o diario de la capa gratuita | Espera un minuto; si es el diario, prueba con el otro servicio |
| F.0 o F.1 con Gemini: `503`, `This model is currently experiencing high demand` | Google tiene el modelo gratuito saturado (nos pasó el 22-10-2026) | Saca una clave de Groq ([🤖 Modelos](Modelos.md)) o espera un rato |
| `Standalone server exited before reporting readiness` | Dos opencode arrancando a la vez en el mismo usuario | Vuelve a lanzarlo (`taller.py lanzar` ya lo reintenta solo) |

## Trabajando con el agente

| Síntoma | Por qué pasa | Arreglo |
|---|---|---|
| No sé cómo salir de opencode | — | `Ctrl+C` con la caja vacía, o `/exit`. Más en [🖥️ Modo interactivo](Modo-interactivo.md) |
| El agente se para con «Permission required» | La orden está en `ask` | Léela y elige *Allow once* o *Reject* con las flechas y Enter |
| `opencode run` se queda colgado sin hacer nada | Una orden está en `ask` y nadie contesta, o espera texto por la entrada | Usa el modo interactivo (`python taller.py abrir …`) |
| «The user dismissed this question» | El modelo usó la tool `question` en modo `run` | Ya está `"question": "deny"` en el kit. Si usas otro `opencode.json`, añádelo |
| `/informe-semanal` no aparece | Los comandos solo existen en el **modo interactivo**, y en la carpeta del ejercicio | `python taller.py abrir f3` y escribe `/` |
| El agente no encuentra la tool MCP | El catálogo MCP tarda unos segundos, o el Python que lo arranca no tiene `mcp` | Repite el encargo; comprueba `python taller.py entorno` (el agente usa el Python del `.venv` del kit) |
| `No module named 'mcp.server.fastmcp'` | En el SDK de MCP 2.x `FastMCP` pasó a llamarse `MCPServer` | `from mcp.server.mcpserver import MCPServer` (ya así en el kit) |
| Los ficheros aparecen en otra carpeta | opencode toma la carpeta de la variable `PWD` | Usa `taller.py`, o haz `cd` a la carpeta del ejercicio antes de lanzar `opencode` |
| 🪟 El agente ejecuta órdenes de Linux (`ls`, `cat`) y fallan | No encuentra Git Bash y usa PowerShell o cmd | Instala Git for Windows (`winget install -e --id Git.Git`) y abre otra PowerShell |
| El comprobador dice ❌ pero el agente dijo «Listo» | Pasa. Es la lección del taller | Lee qué falla, vuelve a abrir opencode y pídele que lo arregle, o mejora el encargo |
| La clave ha aparecido en pantalla o en un fichero | — | Díselo al profesor para que la anule. No la subas a ningún sitio |

¿Otra cosa? Mira lo que hizo el agente al validar en `alumnos/soluciones/<ejercicio>/salida.txt` o pregunta en clase.
