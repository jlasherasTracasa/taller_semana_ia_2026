# :teacher: Material del docente

| Fichero o carpeta | Qué es |
|---|---|
| `validar_ejercicio.sh` | Ejecuta un ejercicio del kit como lo haría un alumno y guarda el prompt y la salida real en `alumnos/soluciones/<ejercicio>/`. |
| `ejemplos/` | Banco de ejemplos validados (webs, correo, pptx, rutinas, tools y skills, réplica del paper) con `verificar_todo.sh`. Tiene su propio README. |

## `validar_ejercicio.sh`

```bash
set -a; . ./.env; set +a                              # desde la raíz del repo
bash docs/taller/profesor/validar_ejercicio.sh ej03_formulario_json
```

Qué hace:
1. Copia `alumnos/ejercicios/<ejercicio>/` y el `opencode.json` del kit a `/tmp/curso_agentes/validacion/<ejercicio>/`.
2. **Aísla tu configuración global de opencode** (`XDG_CONFIG_HOME` propio, sin `opencode.json` global). Motivo
   real: un MCP de Notion global añadía 30 tools, y el EJ 20 falló con un «Listo» falso.
3. Extrae el prompt del bloque `opencode run "…"` del ENUNCIADO y lo ejecuta con `timeout 900`, solo CPU.
4. Escribe `prompt.txt` y `salida.txt` (cabecera con fecha, segundos y código de salida, más las últimas 60 líneas sin
   códigos ANSI).

Qué **no** hace: copiar los ficheros generados a `soluciones/` ni escribir `SOLUCION.md`. Eso se hace a mano,
**después de revisar el resultado**: un código de salida 0 no significa que el ejercicio esté bien (EJ 20).
Después, regenera `presentacion/fuente/ejercicios.json` con `extraer_ejercicios.py`.

Cuidado con los procesos que deja el agente (servidores, timers). Compruébalo al terminar:
`ss -ltnp | grep 89` y `systemctl --user list-timers | grep vigila`.

## `ejemplos/verificar_todo.sh`

Dieciocho comprobaciones objetivas sobre el banco, sin LLM ni GPU: respuesta HTTP 200 de los HTML, pptx legibles y
con el número de diapositivas esperado, CSV con sus columnas, totales cuadrados con el CSV, inyección sin efecto,
sintaxis de los scripts y log de vigilancia.

```bash
bash docs/taller/profesor/ejemplos/verificar_todo.sh
```
