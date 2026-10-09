# 🔧 Problemas y soluciones

| Síntoma | Por qué pasa | Arreglo |
|---|---|---|
| `Error: Invalid URL` o `No api key passed in` | opencode 2.x manda la orden a un **servicio en segundo plano** que arrancó antes de que cargaras tu `.env` | Usa `python3 taller.py lanzar …` o añade `--standalone`. También vale `opencode service restart` tras cargar el `.env` |
| `opencode run` se queda colgado sin hacer nada | Espera texto por la entrada estándar, o una orden está en `ask` | Lanza con `< /dev/null` (taller.py ya lo hace); para `ask`, usa el modo interactivo (`python3 taller.py abrir …`) |
| «The user dismissed this question» | El modelo usó la tool `question` en modo `run`, donde nadie contesta | Ya está `"question": "deny"` en el kit. Si usas otro `opencode.json`, añádelo |
| El agente no encuentra la tool MCP | El catálogo MCP se carga unos segundos después de arrancar, o `python3` no tiene el paquete `mcp` | Activa el `.venv` y `pip install -r requirements.txt`; repite el encargo |
| `No module named 'mcp.server.fastmcp'` | En el SDK de MCP 2.x `FastMCP` pasó a llamarse `MCPServer` | `from mcp.server.mcpserver import MCPServer` (ya así en el kit) |
| Los ficheros aparecen en otra carpeta | opencode toma la carpeta de la variable `PWD` | Usa `taller.py`, o haz `cd` a la carpeta antes de lanzar `opencode` |
| `/informe-semanal` no hace nada | Los comandos solo existen en el **modo interactivo** | `python3 taller.py abrir f3` y escribe `/informe-semanal` |
| `No module named pptx` (u openpyxl, reportlab…) | Falta instalar las bibliotecas | `pip install -r requirements.txt` con el `.venv` activado |
| Windows: `opencode` no se encuentra | El instalador de npm crea un `.cmd` que la terminal aún no ve | Cierra y abre la terminal después de `npm i -g opencode-ai` |
| El comprobador dice ❌ pero el agente dijo «Listo» | Pasa. Es la lección del taller | Lee qué falla, mejora el encargo y vuelve a lanzarlo: `--prompt "…"` |
| La clave ha aparecido en pantalla o en un fichero | — | Pide otra al profesor y borra la vieja. No la subas a ningún sitio |

¿Otra cosa? Mira la salida real de la validación en `alumnos/soluciones/<escena>/salida.txt` o pregunta en clase.
