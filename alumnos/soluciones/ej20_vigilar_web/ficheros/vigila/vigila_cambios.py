#!/usr/bin/env python3
"""Vigila cambios en una página web.

Descarga la URL objetivo, calcula su hash SHA-256 y lo compara con el
guardado en hash.txt. El resultado se registra en log/vigilancia.log.
Solo usa la biblioteca estándar y calcula todas las rutas a partir de la
ubicación del propio script, por lo que funciona desde cualquier directorio
y en cualquier sistema operativo.
"""

import hashlib
import urllib.request
from datetime import datetime
from pathlib import Path

URL = "https://example.com"

# Rutas relativas a este script (no al directorio de trabajo actual)
DIRECTORIO_SCRIPT = Path(__file__).resolve().parent
FICHERO_HASH = DIRECTORIO_SCRIPT / "hash.txt"
DIRECTORIO_LOG = DIRECTORIO_SCRIPT / "log"
FICHERO_LOG = DIRECTORIO_LOG / "vigilancia.log"


def descargar(url):
    """Descarga el contenido de la URL como bytes."""
    peticion = urllib.request.Request(
        url, headers={"User-Agent": "vigila-cambios/1.0"}
    )
    with urllib.request.urlopen(peticion, timeout=15) as respuesta:
        return respuesta.read()


def calcular_sha256(contenido):
    """Devuelve el hash SHA-256 de unos bytes en hexadecimal."""
    return hashlib.sha256(contenido).hexdigest()


def registrar(mensaje):
    """Añade una línea con fecha y hora al fichero de log."""
    DIRECTORIO_LOG.mkdir(parents=True, exist_ok=True)
    marca = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with FICHERO_LOG.open("a", encoding="utf-8") as log:
        log.write(f"{marca} | {mensaje}\n")


def main():
    try:
        contenido = descargar(URL)
    except Exception as error:
        registrar(f"ERROR al descargar {URL}: {error}")
        raise SystemExit(1)

    hash_actual = calcular_sha256(contenido)

    if not FICHERO_HASH.exists():
        # Primera ejecución: guardamos el hash de referencia
        FICHERO_HASH.write_text(hash_actual, encoding="utf-8")
        registrar(f"Inicio. Hash de referencia guardado: {hash_actual}")
    elif FICHERO_HASH.read_text(encoding="utf-8").strip() == hash_actual:
        registrar("Sin cambios.")
    else:
        FICHERO_HASH.write_text(hash_actual, encoding="utf-8")
        registrar(f"CAMBIO DETECTADO. Nuevo hash: {hash_actual}")


if __name__ == "__main__":
    main()
