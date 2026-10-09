# Solución · EJ 03 · Formulario que guarda en JSON

## Prompt exacto usado
Ver `prompt.txt` (el del ENUNCIADO, con sus límites: puerto 8901, no matar procesos, `timeout 60`).

## Resultado (validado 2026-09-28, 27 s)
- `index.html`: formulario con nombre, correo y mensaje que envía por POST a `/guardar`.
- `servidor.py`: servidor solo con la biblioteca estándar (`ThreadingHTTPServer`); acepta JSON y formulario,
  añade cada envío con fecha a `resultados.json` y, si el 8901 está ocupado, busca otro puerto libre.
- El agente lo arrancó con `nohup timeout 60 python3 servidor.py &`, envió dos pruebas con `curl` (respuesta 201) y
  leyó `resultados.json`. A los 60 s el servidor se paró solo: no quedó ningún proceso vivo.

```json
[
  {"nombre": "Ana",  "correo": "ana@example.com",  "mensaje": "Prueba desde curl",         "fecha": "2026-09-28T23:48:17"},
  {"nombre": "Luis", "correo": "luis@example.com", "mensaje": "Envio del formulario HTML", "fecha": "2026-09-28T23:48:17"}
]
```

## Tres intentos, tres lecciones
Este ejercicio se validó tres veces. Las salidas de los dos primeros intentos se conservan en esta carpeta porque
son la mejor explicación de por qué existen los permisos.

| Intento | Configuración | Qué pasó | Salida |
|---|---|---|---|
| 1 | `bash: allow`, prompt sin límites | El puerto 8000 estaba ocupado y **el agente mató el proceso de otro programa** para liberarlo. Lo contó al final: «maté por error un proceso ajeno». | `salida_incidente.txt` |
| 2 | Kit con `"kill *": "deny"` | opencode bloqueó el `kill` (incluso dentro de `pgrep … \| while read p; do kill $p`). El agente no podía parar **ni su propio servidor**: improvisó un endpoint `/shutdown`, dejó un servidor vivo y dio un PID que no existía. | `salida_sin_kill.txt` |
| 3 | Kit + prompt con «Arranca el servidor con timeout 60 delante» | Limpio: puerto libre, dos envíos, parada automática, nada residual. | `salida.txt` |

Moralejas:
1. Un agente va al objetivo por el camino más corto, aunque ese camino pase por algo tuyo.
2. Un `deny` protege, pero también quita herramientas: dale al agente una alternativa segura (`timeout`).
3. Lo que el agente dice haber hecho (el PID, «servidor parado») hay que comprobarlo: `ss -ltnp | grep 8901`.
