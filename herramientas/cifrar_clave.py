#!/usr/bin/env python3
"""Cifra la clave de OpenRouter de la clase con un PIN para la página «Clave de clase» de la web (#/clave).

En el repositorio solo queda el texto cifrado (herramientas/clave_clase.json): sin el PIN no se puede leer.
El PIN se dice en clase en voz alta o se escribe en la pizarra; no va en ningún fichero.

Uso:  CLAVE=sk-or-v1-… PIN=1234 python3 herramientas/cifrar_clave.py
      python3 herramientas/cifrar_clave.py --quitar      (borra la clave de la web después del taller)

Cifrado: AES-256-GCM con una clave derivada del PIN con PBKDF2-SHA256 (1.000.000 de iteraciones), igual que lo
descifra el navegador con WebCrypto. Aun así, pon un límite de gasto a la clave y revócala al terminar el taller.
"""
import base64, json, os, sys

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

RUTA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "clave_clase.json")
ITER = 1_000_000


def b64(b):
    return base64.b64encode(b).decode()


def main():
    if "--quitar" in sys.argv:
        if os.path.exists(RUTA):
            os.remove(RUTA)
        print("Clave quitada: la página #/clave dirá que no hay clave de clase.")
        return
    clave, pin = os.environ.get("CLAVE", "").strip(), os.environ.get("PIN", "").strip()
    if not clave.startswith("sk-or-") or len(pin) < 4:
        sys.exit("Pon CLAVE=sk-or-v1-… y un PIN de al menos 4 caracteres en las variables de entorno.")
    sal, iv = os.urandom(16), os.urandom(12)
    k = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=sal, iterations=ITER).derive(pin.lower().encode())
    datos = {"sal": b64(sal), "iv": b64(iv), "iter": ITER, "cifrado": b64(AESGCM(k).encrypt(iv, clave.encode(), None))}
    json.dump(datos, open(RUTA, "w", encoding="utf-8"), indent=1)
    print(f"Cifrada en {os.path.relpath(RUTA)}. Comprueba el PIN en la web (#/clave) después del push.")


if __name__ == "__main__":
    main()
