#!/usr/bin/env bash
# Verificación de la réplica T11: ejecuta TODO el pipeline desde cero con semilla
# fija, fuerza CPU y comprueba que los ficheros y métricas existen.
# Uso: bash verificar.sh [--reranker]
set -euo pipefail
cd "$(dirname "$0")"

RERANK_FLAG=""
[[ "${1:-}" == "--reranker" ]] && RERANK_FLAG="--reranker"

export CUDA_VISIBLE_DEVICES=""
export PYTHONHASHSEED="42"
# Modelos de Hugging Face en la caché por defecto (~/.cache/huggingface).
export HF_HOME="${HF_HOME:-$HOME/.cache/huggingface}"

# Python: el de $PYTHON, o el .venv del kit/de esta carpeta, o python3 del sistema.
PY="${PYTHON:-}"
for c in .venv/bin/python ../.venv/bin/python; do [[ -z "$PY" && -x "$c" ]] && PY="$c"; done
PY="${PY:-python3}"

"$PY" -c "import torch; assert not torch.cuda.is_available(), 'GPU visible: debe forzarse CPU'; print('[verificar] CPU forzada OK (torch', torch.__version__ + ')')"

# Cargar .env sin imprimir secretos
for f in .env ../.env; do
  if [[ -f "$f" ]]; then set -a; source "$f"; set +a; break; fi
done

rm -rf data/modelo_afinado data/pares.json data/pasajes.json data/negativos.json data/resultados.json
if [[ "${FRESH:-0}" == "1" ]]; then
  rm -f data/cache_consultas.json
  echo "[verificar] caché de consultas borrada (FRESH=1)"
fi

echo "[verificar] Paso 1: datos"
time "$PY" datos.py
echo "[verificar] Paso 2: sintéticos"
time "$PY" sinteticos.py
echo "[verificar] Paso 3: entrenamiento"
time "$PY" entrenar.py
echo "[verificar] Paso 4: evaluación"
time "$PY" evaluar.py $RERANK_FLAG

"$PY" - <<'EOF'
import json
from pathlib import Path

d = Path("data")
fallos = []

def existe(nombre):
    p = d / nombre
    if not p.exists():
        fallos.append(f"falta {nombre}")
    return p

pasajes = json.loads(existe("pasajes.json").read_text(encoding="utf-8"))
pares   = json.loads(existe("pares.json").read_text(encoding="utf-8"))
negs    = json.loads(existe("negativos.json").read_text(encoding="utf-8"))
res     = json.loads(existe("resultados.json").read_text(encoding="utf-8"))

assert 300 <= len(pasajes) <= 500, f"{len(pasajes)} pasajes fuera de rango"
assert all(150 <= len(p["texto"].split()) <= 250 for p in pasajes), "pasaje fuera de 150-250 palabras"
docs_test  = {p["doc"] for p in pares if p["split"] == "test"}
docs_train = {p["doc"] for p in pares if p["split"] == "train"}
assert docs_test and docs_train and docs_test.isdisjoint(docs_train), "split por documento roto"
assert (d / "modelo_afinado").exists(), "falta modelo_afinado"
assert res["metricas"]["Encoder afinado"]["nDCG@10"] > res["metricas"]["Encoder base"]["nDCG@10"], \
    "el afinado no mejora al base"
for sistema in ["BM25", "Encoder base", "Encoder afinado", "Reranker afinado"]:
    assert sistema in res["metricas"], f"faltan métricas de {sistema}"

print("[verificar] TODO CORRECTO:",
      f"{len(pasajes)} pasajes · {sum(1 for p in pares if p['split']=='train')} train ·",
      f"{sum(1 for p in pares if p['split']=='dev')} dev · {sum(1 for p in pares if p['split']=='test')} test")
EOF
echo "[verificar] réplica verificada con éxito."
