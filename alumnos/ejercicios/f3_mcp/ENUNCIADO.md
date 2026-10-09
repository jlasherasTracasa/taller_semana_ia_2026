# F.3 · Tools externas vía MCP

## Objetivo
Exponer una herramienta propia (un servidor local) y verla aparecer entre las tools del agente.

## Datos de partida
- `mcp_server.py` — servidor MCP con UNA tool (`suma_columna`) y `opencode.json` para conectarlo (ajusta la ruta del intérprete Python). `datos/ventas_tienda.csv`.

## Prompt sugerido
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Lista tus tools disponibles. Deberías tener una \
  llamada suma_columna que viene de un servidor MCP propio. Úsala para sumar la columna \
  'hogar' de datos/ventas_tienda.csv y dime el resultado exacto que devolvió la herramienta."

opencode.json (fragmento) conecta el servidor stdio local:
{ "mcp": { "taller-tools": { "type": "local",
    "command": ["<venv>/bin/python", "mcp_server.py"], "enabled": true } } }
```

## Criterio de éxito
El agente lista `suma_columna` entre sus tools, la invoca y cita el resultado EXACTO devuelto: filas=6 suma=29800 media=4966.67.

## Tiempo estimado
≈ 20 min

## Dificultad
Alta
