#!/usr/bin/env bash
# Valida las escenas del kit como lo haría un alumno, con taller.py, y deja un resumen.
#
#   bash profesor/validar.sh                 # todas las escenas con encargo único (8 en paralelo)
#   bash profesor/validar.sh ej07 f4         # solo esas
#   PARALELO=4 bash profesor/validar.sh
#
# Después:  python3 herramientas/guardar_soluciones.py <carpeta que imprime al final>
#
# Necesita las claves en alumnos/.env (las lee taller.py). Lo que aprendimos validando y por eso está aquí:
#  - HOME y XDG_CONFIG_HOME aislados: opencode carga MCP y skills GLOBALES (~/.config/opencode, ~/.claude/skills,
#    ~/.agents/skills). Un MCP de Notion con 30 tools provocó un «Listo» falso; una skill pptx global ayudó en
#    EJ 12-13 a escondidas. El alumno no tendrá nada de eso.
#  - taller.py fija PWD: opencode decide su carpeta por PWD, no por el directorio real del proceso.
#  - opencode run --standalone y stdin cerrado: sin eso, el servicio en segundo plano no ve el .env y run se cuelga.
set -uo pipefail
RAIZ="$(cd "$(dirname "$0")/.." && pwd)"
KIT="$RAIZ/alumnos"
RONDA="${RONDA:-/tmp/validacion_taller/$(date +%Y%m%d_%H%M)}"
mkdir -p "$RONDA/logs" "$RONDA/home"
export TALLER_TRABAJO="$RONDA" HOME_REAL="$HOME"
export PATH="$KIT/.venv/bin:$HOME/.local/node/bin:$PATH" CUDA_VISIBLE_DEVICES=""
export XDG_CONFIG_HOME="$RONDA/config" HOME="$RONDA/home"
mkdir -p "$XDG_CONFIG_HOME/opencode"

if [ $# -gt 0 ]; then LISTA="$*"; else
  LISTA=$(python3 -c "
import json; d=json.load(open('$KIT/ejercicios/indice.json'))
print(' '.join(e['num_corto'] for e in d['ejercicios'] if e['modo']=='run' and e.get('prompt')))")
fi

una() {
  local ej="$1" L="$RONDA/logs/$1.log" t0 t1 rc
  t0=$(date +%s)
  case "$ej" in
    f2) python3 "$KIT/taller.py" empezar f2 >/dev/null
        cp "$RONDA"/f2_*/AGENTS.ejemplo.md "$(ls -d "$RONDA"/f2_*)/AGENTS.md"
        python3 "$KIT/taller.py" lanzar f2 > "$L" 2>&1 ;;
    *)  python3 "$KIT/taller.py" lanzar "$ej" > "$L" 2>&1 ;;
  esac
  t1=$(date +%s)
  python3 "$KIT/taller.py" comprobar "$ej" >> "$L" 2>&1; rc=$?
  echo "$ej $([ $rc = 0 ] && echo OK || echo FALLA) $((t1 - t0))s" | tee -a "$RONDA/resumen.txt"
}
export -f una; export KIT RONDA

echo "Ronda en $RONDA · escenas: $LISTA"
printf '%s\n' $LISTA | xargs -P "${PARALELO:-8}" -I{} bash -c 'una {}'
echo
sort "$RONDA/resumen.txt"
echo "OK: $(grep -c ' OK ' "$RONDA/resumen.txt") de $(wc -l < "$RONDA/resumen.txt")"
echo "Revisa A MANO lo que falle (y lo que pase: un OK no es una prueba de que todo esté bien)."
echo "Comprueba que no quedan procesos:  ss -ltnp | grep 89 ;  systemctl --user list-timers | grep vigila"
echo "Guardar como soluciones:  python3 herramientas/guardar_soluciones.py $RONDA"
