#!/usr/bin/env bash
# Comprueba que tu portátil está listo para el taller (sin GPU).
# Uso, desde la carpeta alumnos/:   bash comprobar_entorno.sh            (añade --sin-modelo para no llamar al modelo)
set -u
cd "$(dirname "$0")"
OK=0; FALLOS=0
pasa()  { echo "  ✅ $1"; OK=$((OK+1)); }
falla() { echo "  ❌ $1"; FALLOS=$((FALLOS+1)); }
avisa() { echo "  ⚠️  $1"; }

# Lee .env sin imprimir nada (las variables ya definidas en la terminal tienen prioridad)
if [ -f .env ]; then
  while IFS='=' read -r k v; do
    k="${k%%#*}"; k="$(echo "$k" | tr -d '[:space:]')"; v="${v%%#*}"; v="$(echo "$v" | sed 's/^ *//; s/ *$//')"
    [ -n "$k" ] && [ -n "$v" ] && [ -z "${!k:-}" ] && export "$k=$v"
  done < .env
fi

echo "== 1) Python 3.10 o superior =="
PY=python3; [ -x .venv/bin/python ] && PY=.venv/bin/python
if command -v "$PY" >/dev/null 2>&1 && "$PY" -c 'import sys; sys.exit(sys.version_info < (3, 10))'; then
  pasa "$("$PY" --version) ($PY)"
else
  falla "hace falta Python 3.10+ (https://www.python.org)"
fi

echo "== 2) Bibliotecas de los ejercicios (requirements.txt) =="
FALTAN=$("$PY" - <<'EOF' 2>/dev/null
import importlib.util
mods = {"litellm": "litellm", "mcp": "mcp", "pptx": "python-pptx", "matplotlib": "matplotlib", "openpyxl": "openpyxl",
        "pdfplumber": "pdfplumber", "pypdf": "pypdf", "reportlab": "reportlab", "docx": "python-docx",
        "icalendar": "icalendar", "defusedxml": "defusedxml"}
print(" ".join(p for m, p in mods.items() if importlib.util.find_spec(m) is None))
EOF
)
if [ -z "$FALTAN" ]; then pasa "todas instaladas"; else
  falla "faltan: $FALTAN  →  python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt"; fi

echo "== 3) Node 18 o superior =="
if command -v node >/dev/null 2>&1 && node -e 'process.exit(parseInt(process.versions.node) < 18 ? 1 : 0)'; then
  pasa "node $(node --version)"
else
  falla "hace falta Node.js 18+ (https://nodejs.org)"
fi

echo "== 4) opencode 2.x =="
if command -v opencode >/dev/null 2>&1; then
  V=$(opencode --version 2>/dev/null | grep -oE '[0-9]+\.[0-9]+\.[0-9]+' | head -1)
  case "$V" in
    2.*) pasa "opencode $V (validado con 2.0.19)" ;;
    *)   avisa "opencode $V: el kit está validado con la 2.0.19 →  npm i -g opencode-ai@2.0.19" ;;
  esac
else
  falla "no está instalado →  npm i -g opencode-ai"
fi

echo "== 5) Clave del modelo (no se imprime) =="
if [ -n "${LITELLM_API_KEY:-}" ] && [ -n "${LITELLM_API_BASE:-}" ]; then pasa "LiteLLM del taller: URL y clave definidas"
elif [ -n "${OPENROUTER_API_KEY:-}" ]; then pasa "OpenRouter: clave definida"
else falla "sin clave: copia .env.example a .env y rellénala (wiki: Variables de entorno)"; fi
case "${LITELLM_API_BASE:-}" in */v1|*/v1/) avisa "LITELLM_API_BASE no debe terminar en /v1 (el kit lo añade)";; esac

echo "== 6) Prueba real con el modelo =="
if [ "${1:-}" = "--sin-modelo" ]; then avisa "omitida (--sin-modelo)"
elif [ "$FALLOS" -gt 0 ]; then avisa "omitida: arregla antes lo que está en ❌"
else
  D=$(mktemp -d); cp opencode.json "$D/"
  [ -z "${LITELLM_API_KEY:-}" ] && sed -i.bak 's#"model": "vllm/[^"]*"#"model": "openrouter/z-ai/glm-5.3-flash"#' "$D/opencode.json"
  R=$(cd "$D" && PWD="$D" timeout 120 opencode run --standalone "Responde exactamente: listo para el taller" < /dev/null 2>&1 | tail -3)
  rm -rf "$D"
  if echo "$R" | grep -qi "listo para el taller"; then pasa "el modelo responde"; else falla "el modelo no responde: $(echo "$R" | tail -1 | cut -c1-120)  (wiki: Problemas)"; fi
fi

echo
echo "== Resumen: $OK correctas, $FALLOS por arreglar =="
[ "$FALLOS" = 0 ] && echo "🎉 Listo para el taller. Siguiente:  python3 taller.py" || echo "Arregla lo que está en ❌ (wiki: Primeros pasos y Problemas)."
exit "$FALLOS"
