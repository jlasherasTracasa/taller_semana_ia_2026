# Servidor MCP local mínimo (stdio): expone UNA tool para opencode.
# No hace falta ejecutarlo a mano: opencode lo arranca solo (ver opencode.json de esta carpeta).
from mcp.server.mcpserver import MCPServer  # SDK de MCP 2.x (en 1.x se llamaba FastMCP)

import csv

mcp = MCPServer("taller-tools")

@mcp.tool()
def suma_columna(ruta: str, columna: str) -> str:
    """Suma los valores numéricos de una columna de un CSV local.
    Args:
        ruta: ruta del archivo CSV (relativa al proyecto).
        columna: nombre de la columna numérica a sumar.
    """
    with open(ruta, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        if columna not in (lector.fieldnames or []):
            return f"ERROR: no existe la columna '{columna}'"
        valores = [float(row[columna]) for row in lector]
    total = sum(valores)
    return f"filas={len(valores)} suma={total:g} media={total/len(valores):.2f}"

if __name__ == "__main__":
    mcp.run()  # transporte stdio: opencode hablará con este proceso por stdin/stdout
