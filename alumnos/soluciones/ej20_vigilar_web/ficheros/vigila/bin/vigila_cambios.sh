#!/usr/bin/env bash
#
# vigila_cambios.sh — vigila cambios en https://example.com
# Todo se resuelve desde la ubicacion de este script (sin rutas absolutas).
#
set -euo pipefail

# Directorio base = padre del directorio donde vive este script (.../vigila)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

HASH_FILE="$BASE_DIR/hash.txt"
LOG_DIR="$BASE_DIR/log"
LOG_FILE="$LOG_DIR/vigilancia.log"
URL="https://example.com"

mkdir -p "$LOG_DIR"
FECHA="$(date '+%Y-%m-%d %H:%M:%S')"

# 1) Descarga y calcula el hash SHA-256 del contenido
if ! CONTENIDO="$(curl -fsS --max-time 30 "$URL")"; then
    echo "[$FECHA] ERROR: no se pudo descargar $URL" >> "$LOG_FILE"
    exit 1
fi
HASH_ACTUAL="$(printf '%s' "$CONTENIDO" | sha256sum | awk '{print $1}')"

# 2) Compara con el hash guardado y deja constancia en el log
if [[ ! -f "$HASH_FILE" ]]; then
    # Primera ejecucion: guardamos el hash de referencia
    echo "$HASH_ACTUAL" > "$HASH_FILE"
    echo "[$FECHA] INICIO: hash de referencia guardado ($HASH_ACTUAL)" >> "$LOG_FILE"
elif [[ "$(cat "$HASH_FILE")" == "$HASH_ACTUAL" ]]; then
    echo "[$FECHA] sin cambios ($HASH_ACTUAL)" >> "$LOG_FILE"
else
    echo "[$FECHA] *** CAMBIO DETECTADO *** (antes: $(cat "$HASH_FILE"), ahora: $HASH_ACTUAL)" >> "$LOG_FILE"
    echo "$HASH_ACTUAL" > "$HASH_FILE"   # actualizamos la referencia
fi

exit 0
