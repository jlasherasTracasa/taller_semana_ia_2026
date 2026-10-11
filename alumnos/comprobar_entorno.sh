#!/usr/bin/env bash
# Comprueba que tu ordenador está listo para el taller. Es lo mismo que:  python3 taller.py entorno
# (en Windows:  python taller.py entorno). Añade --sin-modelo para no llamar al modelo.
cd "$(dirname "$0")" && exec python3 taller.py entorno "$@"
