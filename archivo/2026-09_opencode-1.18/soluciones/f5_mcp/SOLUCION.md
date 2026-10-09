# Solución · F.3 · Tools externas vía MCP

## Prompt exacto usado
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Lista tus tools disponibles. Deberías tener una \
  llamada suma_columna que viene de un servidor MCP propio. Úsala para sumar la columna \
  'hogar' de datos/ventas_tienda.csv y dime el resultado exacto que devolvió la herramienta."

opencode.json (fragmento) conecta el servidor stdio local:
{ "mcp": { "taller-tools": { "type": "local",
    "command": ["<venv>/bin/python", "mcp_server.py"], "enabled": true } } }
```

## Resultado
opencode listó la tool `suma_columna` del servidor MCP, la llamó ({columna: hogar, ruta: datos/ventas_tienda.csv}) y citó tal cual: filas=6 suma=29800 media=4966.67.

## Salida real (extracto validado 2026-09-28)
```
> build · GLM-5.3-Flash

⚙ taller-tools_suma_columna {"columna":"hogar","ruta":"datos/ventas_tienda.csv"}
→ Read datos/ventas_tienda.csv
La herramienta `taller-tools_suma_columna` devolvió exactamente:

```
filas=6 suma=29800 media=4966.67
```

Es decir, la suma de la columna `hogar` es **29800** (verificado contra el CSV: 4200+3900+4600+5100+5800+6200 = 29800, en 6 filas de datos).
```

Los artefactos generados (archivos de resultado) están en esta misma carpeta.
