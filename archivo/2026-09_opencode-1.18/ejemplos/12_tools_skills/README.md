# 12 · Tools y skills — (validado 2026-09-28)

Cuatro ejemplos que demuestran cómo un agente «toca el mundo»: llamadas a herramientas
(function calling), paquetes de instrucciones reutilizables (skills/comandos) y
herramientas externas vía MCP. Ejecutados en `/tmp/curso_agentes/tools_skills/` con
GLM-5.3-Flash a través de LiteLLM, solo CPU y sin claves reales.

| Carpeta | Qué demuestra | Comando / prueba |
|---|---|---|
| `12d_react_min/` | **El bucle ReAct** en ~70 líneas: pensar → actuar (tool) → observar, con dos tools de solo lectura y una «jaula» de carpeta | `python react_min.py` · `python react_min.py "Lee ../../.env…"` |
| `12a_fc_litellm/` | Function calling puro: el modelo devuelve un tool_call JSON y **nuestro código** ejecuta la función | `.venv/bin/python fc_calculadora.py` |
| `12b_comando_informe/` | Un comando personalizado de opencode (`.opencode/command/informe-semanal.md`) actúa de «skill»: lee un CSV y genera un pptx | `opencode run --model vllm/GLM-5.3-Flash --command informe-semanal` |
| `12c_mcp_local/` | Servidor MCP local mínimo (stdio) con una tool `suma_columna`, conectado a opencode | `opencode run "…usa suma_columna…"` |

## Verificación objetiva (sin LLM, sin GPU)

```text
OK  12d: react_min.py resuelve el objetivo en 3 pasos (listar → leer ×3 → responder).
        Error real del modelo en la respuesta: dice que compra.txt tiene 2 líneas (tiene 3).
        Con un objetivo malicioso el modelo SÍ intenta leer ../.env; lo bloquea _dentro()
        («ERROR: fuera de la carpeta permitida»), no el modelo
OK  12a: fc_calculadora.py termina (exit 0); el modelo pide calculadora con
        argumentos JSON '{"expresion": "(1250+3750)*1.21"}' y la respuesta final
        cita 6.050 € (= resultado de NUESTRA función, no del modelo)
OK  12b: informe_semanal.pptx abre con python-pptx; 3 diapositivas; totales
        hogar 29.800 · textil 18.700 · bazar 14.000 (cuadran con ventas_tienda.csv)
OK  12c: el servidor MCP responde a list_tools y call_tool standalone
        ('filas=6 suma=29800 media=4966.67') y opencode muestra la llamada
        ⚙ taller-tools_suma_columna {"columna":"hogar","ruta":"datos/ventas_tienda.csv"}
        devolviendo exactamente ese resultado
```
**(validado 2026-09-28)**

## Notas de replicación

- En LiteLLM el proveedor va en el nombre del modelo: `openai/GLM-5.3-Flash` apuntando
  al endpoint `/v1` de LiteLLM (`api_base`, `api_key` por variables de entorno).
- Los comandos personalizados se registran en `.opencode/command/*.md`; en modo no
  interactivo se invocan con `--command informe-semanal` (el slash `/informe-semanal`
  funciona en el TUI, no en `opencode run`).
- El SDK `mcp` 2.x renombró FastMCP: usar `from mcp.server.mcpserver import MCPServer`.
