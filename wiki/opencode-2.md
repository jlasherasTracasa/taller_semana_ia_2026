# 🔄 opencode 2.x para quien venga de la 1.x

El kit se preparó en septiembre con opencode 1.18 y en octubre llegó la 2.0. Cambiaron cinco cosas que rompían
ejercicios. Están todas resueltas en el kit, pero si tienes guías o scripts antiguos:

| Antes (1.x) | Ahora (2.x) | Qué hacer |
|---|---|---|
| `opencode run` ejecutaba todo en el mismo proceso | Usa un **servicio en segundo plano** que no ve las variables de tu terminal | `opencode run --standalone …` |
| `opencode run --command informe-semanal` | `--command` ya no existe | Modo interactivo: `opencode` y `/informe-semanal` |
| Comandos en `.opencode/command/` | `.opencode/commands/` | Renombrar la carpeta |
| Tools propias en `.opencode/tools/*.ts` | La API de plugins v2 no registra tools | Escribir un servidor **MCP** (ejercicio F.6) |
| Las tools MCP aparecían en la lista | Se **buscan en un catálogo** y se llaman desde la tool `execute` | Nada: el modelo lo hace solo; tarda unos segundos en verlas |
| — | Nueva tool `question`: el modelo te pregunta | En `run` bloquea: `"question": "deny"` |
| `bash` en permisos | Se sigue aceptando (internamente se llama `shell`) | Nada |

Y en Python, el SDK de MCP 2.x renombró `FastMCP` a `MCPServer` (`from mcp.server.mcpserver import MCPServer`).

> Moraleja para cualquier herramienta de IA: **fija versiones** y **revalida** antes de usarla con gente. La
> documentación oficial de plugins también estaba desactualizada cuando preparamos el taller.
