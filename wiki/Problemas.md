# 🔧 Problemas y soluciones

Primero, siempre: `python taller.py entorno`. Te dice qué falta y cómo arreglarlo.

## Instalación

| Síntoma | Por qué pasa | Arreglo |
|---|---|---|
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
| F.0 o F.1: «necesita OPENROUTER_API_KEY» | Son programas de Python: los modelos gratuitos solo funcionan dentro de opencode | Pon la clave de OpenRouter en `.env`, o mira la demo del profesor |
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
