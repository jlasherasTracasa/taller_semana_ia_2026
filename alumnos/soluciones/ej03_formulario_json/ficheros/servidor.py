"""Servidor mínimo de inscripciones: solo biblioteca estándar.

- Sirve formulario.html en GET /
- Guarda cada POST /enviar en resultados.json
- Se apaga solo a los 60 segundos (threading.Timer), sin matar procesos:
  funciona igual en Windows, macOS y Linux.
- Si el puerto pedido está ocupado, prueba el siguiente libre.
"""

import json
import os
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FORMULARIO = os.path.join(BASE_DIR, "formulario.html")
RESULTADOS = os.path.join(BASE_DIR, "resultados.json")
PUERTO_FILE = os.path.join(BASE_DIR, "puerto.txt")

PUERTO_INICIAL = 8901
PUERTO_MAXIMO = 8999
SEGUNDOS_VIDA = 60

lock = threading.Lock()


def guardar_envio(datos):
    """Añade el envío a resultados.json de forma segura entre hilos."""
    with lock:
        try:
            with open(RESULTADOS, encoding="utf-8") as f:
                lista = json.load(f)
            if not isinstance(lista, list):
                lista = []
        except (FileNotFoundError, json.JSONDecodeError):
            lista = []
        lista.append({"recibido": time.strftime("%Y-%m-%d %H:%M:%S"), **datos})
        with open(RESULTADOS, "w", encoding="utf-8") as f:
            json.dump(lista, f, ensure_ascii=False, indent=2)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            with open(FORMULARIO, "rb") as f:
                cuerpo = f.read()
        except FileNotFoundError:
            self.send_error(404, "Falta formulario.html")
            return
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(cuerpo)))
        self.end_headers()
        self.wfile.write(cuerpo)

    def do_POST(self):
        if self.path != "/enviar":
            self.send_error(404)
            return
        longitud = int(self.headers.get("Content-Length", 0))
        campos = parse_qs(self.rfile.read(longitud).decode("utf-8"))
        datos = {k: v[0] for k, v in campos.items()}
        guardar_envio(datos)
        cuerpo = "Envío guardado. ¡Gracias!".encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(cuerpo)))
        self.end_headers()
        self.wfile.write(cuerpo)

    def log_message(self, formato, *args):
        pass  # log silencioso para no ensuciar salida en segundo plano


def abrir_puerto():
    """Devuelve un servidor en el primer puerto libre desde 8901."""
    for puerto in range(PUERTO_INICIAL, PUERTO_MAXIMO + 1):
        try:
            servidor = ThreadingHTTPServer(("127.0.0.1", puerto), Handler)
            return servidor, puerto
        except OSError:
            continue  # ocupado: probamos el siguiente, sin matar nada
    raise RuntimeError("No hay puertos libres entre 8901 y 8999")


def main():
    servidor, puerto = abrir_puerto()
    with open(PUERTO_FILE, "w") as f:
        f.write(str(puerto))
    print(f"Servidor escuchando en http://127.0.0.1:{puerto} "
          f"(se apagará solo en {SEGUNDOS_VIDA}s)")

    # Autoapagado: un temporizador llama a shutdown(); es multiplataforma.
    temporizador = threading.Timer(SEGUNDOS_VIDA, servidor.shutdown)
    temporizador.daemon = True
    temporizador.start()

    try:
        servidor.serve_forever()
    finally:
        servidor.server_close()
        temporizador.join()
        try:
            os.remove(PUERTO_FILE)
        except OSError:
            pass
        print("Servidor apagado limpiamente.")


if __name__ == "__main__":
    main()
