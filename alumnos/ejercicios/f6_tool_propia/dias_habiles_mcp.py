# Tu propia tool para el agente, en 30 líneas: un servidor MCP local (stdio) con UNA herramienta.
# opencode lo arranca solo (ver opencode.json de esta carpeta) y el modelo puede pedirle que calcule plazos.
# Reto: añade una segunda tool, por ejemplo  es_habil(fecha) -> "sí"/"no, es festivo: …".
import datetime as dt

from mcp.server.mcpserver import MCPServer  # SDK de MCP 2.x (en 1.x se llamaba FastMCP)

mcp = MCPServer("plazos")

# Festivos nacionales y de Navarra de 2026 (los locales de cada municipio no están incluidos)
FESTIVOS = {"2026-01-01", "2026-01-06", "2026-03-19", "2026-04-02", "2026-04-03", "2026-04-06", "2026-05-01",
            "2026-07-25", "2026-08-15", "2026-10-12", "2026-11-01", "2026-12-03", "2026-12-08", "2026-12-25"}
DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]


@mcp.tool()
def dias_habiles(desde: str, dias: int) -> str:
    """Calcula el día en que vence un plazo de N días hábiles (lunes a viernes, sin festivos nacionales ni de
    Navarra de 2026), contando desde el día siguiente a la notificación. Úsala SIEMPRE para plazos
    administrativos: no calcules fechas de cabeza.
    Args:
        desde: fecha de notificación, AAAA-MM-DD.
        dias: número de días hábiles del plazo.
    """
    d, contados, saltados = dt.date.fromisoformat(desde), 0, []
    while contados < dias:
        d += dt.timedelta(days=1)
        if d.isoformat() in FESTIVOS:
            saltados.append(d.strftime("%d/%m"))
        elif d.weekday() < 5:
            contados += 1
    return f"vence={d.strftime('%d/%m/%Y')} ({DIAS[d.weekday()]}) festivos_saltados={','.join(saltados) or 'ninguno'}"


if __name__ == "__main__":
    mcp.run()  # transporte stdio: opencode habla con este proceso por stdin/stdout
