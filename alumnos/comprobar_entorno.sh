#!/usr/bin/env bash
# Comprueba que tu entorno está listo para el taller (SOLO CPU).
# Uso: bash comprobar_entorno.sh        (ejecútalo desde la carpeta del kit)
set -u
OK=0; FALLOS=0

pasa() { echo "  ✓ $1"; OK=$((OK+1)); }
falla() { echo "  ✗ $1"; FALLOS=$((FALLOS+1)); }
avisa() { echo "  ! $1"; }

echo "== 1) Python 3.10+ =="
if command -v python3 >/dev/null 2>&1; then
  V=$(python3 -c 'import sys; print("%d.%d"%sys.version_info[:2])')
  MENOR=$(python3 -c 'import sys; print(1 if sys.version_info<(3,10) else 0)')
  [ "$MENOR" = "0" ] && pasa "python3 $V" || falla "python3 $V (se necesita 3.10+)"
else
  falla "no hay python3"
fi

echo "== 2) Node 18+ =="
if command -v node >/dev/null 2>&1; then
  V=$(node --version | sed 's/^v//')
  MAYOR=$(node -e 'console.log(parseInt(process.versions.node)<18?1:0)')
  [ "$MAYOR" = "0" ] && pasa "node $V" || falla "node $V (se necesita 18+)"
else
  falla "no hay node — instala Node.js LTS (https://nodejs.org)"
fi

echo "== 3) opencode =="
if command -v opencode >/dev/null 2>&1; then
  pasa "opencode $(opencode --version 2>/dev/null | head -1)"
else
  falla "opencode no está instalado — npm i -g opencode-ai"
fi

echo "== 4) Variables de entorno de la API (no se imprimen) =="
if [ -n "${LITELLM_API_BASE:-}" ]; then pasa "LITELLM_API_BASE definida"; else
  if [ -f .env ] && grep -q '^LITELLM_API_BASE=.\+' .env; then avisa "están en .env pero no cargadas: haz  set -a; . ./.env; set +a"; else falla "LITELLM_API_BASE sin definir (revisa el README.md del kit)"; fi
fi
if [ -n "${LITELLM_API_KEY:-}" ]; then pasa "LITELLM_API_KEY definida (valor oculto)"; else
  if [ -f .env ] && grep -q '^LITELLM_API_KEY=.\+' .env; then avisa "está en .env pero no cargada: haz  set -a; . ./.env; set +a"; else falla "LITELLM_API_KEY sin definir (te la dará el profesor)"; fi
fi

echo "== 5) torch en CPU (solo para replicar_paper; opcional) =="
PY=".venv/bin/python"; [ -x "$PY" ] || PY="python3"
if "$PY" -c "import torch" 2>/dev/null; then
  if "$PY" -c "import torch,sys; sys.exit(0 if not torch.cuda.is_available() else 1)"; then
    pasa "torch $($PY -c 'import torch;print(torch.__version__)') usa CPU (CUDA no visible)"
  else
    avisa "torch ve una GPU (no pasa nada: verificar.sh de la réplica ya fuerza CUDA_VISIBLE_DEVICES=\"\")"
  fi
else
  avisa "torch no instalado en este intérprete (solo hace falta para replicar_paper: pip install -r requirements.txt)"
fi

echo
echo "== Resumen: $OK comprobaciones superadas, $FALLOS fallos =="
[ "$FALLOS" = "0" ] && echo "ENTORNO LISTO ✓" || echo "CORRIGE LOS ✗ ANTES DEL TALLER"
exit "$FALLOS"
