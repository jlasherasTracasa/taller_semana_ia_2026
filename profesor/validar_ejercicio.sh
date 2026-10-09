#!/usr/bin/env bash
# Valida un ejercicio del kit como lo haría un alumno: copia sus datos a un directorio limpio, ejecuta con opencode
# el prompt sugerido del ENUNCIADO y guarda el prompt y la salida real en soluciones/<ej>/.
# Uso (desde la raíz del repo, con el .env cargado): bash docs/taller/profesor/validar_ejercicio.sh ej03_formulario_json
set -uo pipefail
EJ="$1"; KIT="$(cd "$(dirname "$0")/.." && pwd)/alumnos"; W="/tmp/curso_agentes/validacion/$EJ"
export PATH="$HOME/.local/node/bin:$PATH" CUDA_VISIBLE_DEVICES=""
[ -n "${LITELLM_API_BASE:-}" ] && [ -n "${LITELLM_API_KEY:-}" ] || { echo "Faltan LITELLM_API_BASE/LITELLM_API_KEY: carga antes el .env (set -a; . ./.env; set +a)"; exit 3; }
# Aísla la configuración global del docente (p. ej. un MCP de Notion con 30 tools confunde al modelo): el alumno
# solo tendrá el opencode.json del kit.
export XDG_CONFIG_HOME="/tmp/curso_agentes/config_vacia"
if [ ! -d "$XDG_CONFIG_HOME/opencode" ]; then
  mkdir -p "$XDG_CONFIG_HOME/opencode"
  cp -r "$HOME/.config/opencode/." "$XDG_CONFIG_HOME/opencode/" 2>/dev/null
  rm -f "$XDG_CONFIG_HOME"/opencode/opencode.json{,c}   # sin MCP ni ajustes globales
fi
rm -rf "$W"; mkdir -p "$W"; cp -r "$KIT/ejercicios/$EJ/." "$W/"; cp "$KIT/opencode.json" "$W/"
PROMPT=$(python3 - "$KIT/ejercicios/$EJ/ENUNCIADO.md" <<'PY'
import re,sys
s=open(sys.argv[1]).read()
m=re.search(r'opencode run[^"]*"(.*?)"\s*$',s,re.S|re.M)
print(m.group(1) if m else "")
PY
)
[ -z "$PROMPT" ] && { echo "SIN PROMPT en $EJ"; exit 2; }
printf '%s\n' "$PROMPT" > "$KIT/soluciones/$EJ/prompt.txt"
cd "$W"; T0=$(date +%s)
timeout 900 opencode run --model vllm/GLM-5.3-Flash "$PROMPT" > "$W/.salida_completa.txt" 2>&1; RC=$?
T1=$(date +%s)
{ echo "# Ejecución real: $(date -I) · $((T1-T0)) s · código $RC · opencode + GLM-5.3-Flash · solo CPU"; echo; tail -n 60 "$W/.salida_completa.txt" | sed -E "s/\x1b\[[0-9;]*m//g"; } > "$KIT/soluciones/$EJ/salida.txt"
echo "$EJ rc=$RC $((T1-T0))s"
