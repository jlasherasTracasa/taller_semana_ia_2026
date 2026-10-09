#!/usr/bin/env bash
# Notas privadas del docente: en el repositorio solo van CIFRADAS (AES-256-CBC, PBKDF2 con 600.000 iteraciones).
#
#   bash profesor/notas.sh descifrar   → profesor_privado/NOTAS_PROFESOR.md y presentacion/taller-agentes-ia-con-notas.pptx
#   bash profesor/notas.sh cifrar      → profesor/notas_profesor.md.enc y profesor/taller-con-notas.pptx.enc
#
# La contraseña NO está en el repositorio. Pásala en NOTAS_CLAVE o escríbela cuando te la pida.
# profesor_privado/ y los pptx «con-notas» están en .gitignore: nunca se suben en claro.
set -euo pipefail
RAIZ="$(cd "$(dirname "$0")/.." && pwd)"
PARES=("$RAIZ/profesor_privado/NOTAS_PROFESOR.md:$RAIZ/profesor/notas_profesor.md.enc"
       "$RAIZ/presentacion/taller-agentes-ia-con-notas.pptx:$RAIZ/profesor/taller-con-notas.pptx.enc")
if [ -z "${NOTAS_CLAVE:-}" ]; then read -rsp "Contraseña de las notas: " NOTAS_CLAVE; echo; fi
export NOTAS_CLAVE
OPC=(-aes-256-cbc -pbkdf2 -iter 600000 -salt -pass env:NOTAS_CLAVE)
case "${1:-}" in
  cifrar)
    for p in "${PARES[@]}"; do claro="${p%%:*}"; cifrado="${p##*:}"
      [ -f "$claro" ] || { echo "No existe $claro (¿lo has descifrado o generado?)"; continue; }
      openssl enc "${OPC[@]}" -in "$claro" -out "$cifrado" && echo "🔒 $cifrado"; done ;;
  descifrar)
    mkdir -p "$RAIZ/profesor_privado"
    for p in "${PARES[@]}"; do claro="${p%%:*}"; cifrado="${p##*:}"
      openssl enc -d "${OPC[@]}" -in "$cifrado" -out "$claro" && echo "🔓 $claro"; done ;;
  *) sed -n '2,8p' "$0"; exit 1 ;;
esac
