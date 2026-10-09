# Solución · EJ 20 · Vigilar una web pública

## Prompt exacto usado
Ver `prompt.txt` (es el del ENUNCIADO, sin cambios).

## Resultado
`vigila/bin/vigila_cambios.sh` calcula la carpeta `vigila/` a partir de su propia ubicación
(`RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"`), descarga la página con `curl -fsSL`, compara su
SHA-256 con `vigila/hash.txt` y añade una línea a `vigila/log/vigilancia.log`. Ejecución: 10 s.

## Salida real (validado 2026-09-28)
```
[2026-09-28 23:31:59] Inicio de vigilancia. Hash guardado: 7d3e61f8…
[2026-09-28 23:32:00] Sin cambios en https://example.com (hash 7d3e61f8…)
```
Comprobado además a mano lanzándolo desde `/` (`cd / && bash …/vigila_cambios.sh`): añade una tercera línea
«Sin cambios», así que no depende del directorio actual.

## Lo que salió mal antes (y por qué es la mejor lección del ejercicio)
El primer intento, en la máquina del docente, **falló y el agente dijo «Listo»**:

1. opencode cargó también un MCP de Notion de la configuración global del docente: **30 tools extra**. El modelo
   intentó llamar a una tool inexistente (`notion_API-get-block`), encadenó llamadas con argumentos vacíos…
2. …y acabó escribiendo un script de 4 líneas (`echo "Vigilando..."`) sin ejecutarlo, y respondió
   «Listo. El script está en `vigila/bin/vigila_cambios.sh`».

Moralejas: **más tools no es mejor** (cada tool ocupa contexto y aumenta la probabilidad de elegir mal), y
**«el agente dice que ha terminado» no es una prueba**: comprueba tú el criterio de éxito (aquí, que el log
tenga dos líneas). Sin la configuración global, el mismo prompt salió bien a la primera.
