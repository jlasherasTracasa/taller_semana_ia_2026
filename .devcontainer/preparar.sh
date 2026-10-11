#!/usr/bin/env bash
# Prepara el kit dentro de GitHub Codespaces (plan B: sin portátil o sin poder instalar nada).
# Lo ejecuta Codespaces solo al crear el espacio; tarda unos 3 minutos.
set -euo pipefail
cd "$(dirname "$0")/.."

if ! command -v node >/dev/null 2>&1 || [ "$(node -e 'console.log(parseInt(process.versions.node))')" -lt 18 ]; then
  echo "== Node.js 22"
  V=v22.12.0
  mkdir -p "$HOME/.local/node"
  curl -fsSL "https://nodejs.org/dist/$V/node-$V-linux-x64.tar.xz" | tar -xJ -C "$HOME/.local/node" --strip-components=1
  export PATH="$HOME/.local/node/bin:$PATH"
  echo 'export PATH="$HOME/.local/node/bin:$PATH"' >> "$HOME/.bashrc"
fi

echo "== opencode 2.0.19"
npm i -g @opencode/cli@2.0.19

echo "== Bibliotecas de Python del kit"
python3 -m venv alumnos/.venv
alumnos/.venv/bin/pip install -q -r alumnos/requirements.txt
# Cada terminal nueva empieza en alumnos/ con el entorno de Python activado
echo 'cd /workspaces/*/alumnos 2>/dev/null && . .venv/bin/activate' >> "$HOME/.bashrc"

echo
echo "Listo. En la terminal:  python taller.py entorno   y después   python taller.py empezar ej24"
