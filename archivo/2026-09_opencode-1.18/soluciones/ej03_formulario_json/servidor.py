import json
import os
import socket
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs

BASE = os.path.dirname(os.path.abspath(__file__))
RESULTADOS = os.path.join(BASE, "resultados.json")
INDEX = os.path.join(BASE, "index.html")


def leer_envios():
    if os.path.exists(RESULTADOS):
        with open(RESULTADOS, encoding="utf-8") as f:
            return json.load(f)
    return []


class Manejador(BaseHTTPRequestHandler):
    def _responder(self, codigo, cuerpo, tipo="application/json; charset=utf-8"):
        data = cuerpo.encode("utf-8")
        self.send_response(codigo)
        self.send_header("Content-Type", tipo)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            with open(INDEX, encoding="utf-8") as f:
                self._responder(200, f.read(), "text/html; charset=utf-8")
        elif self.path == "/envios":
            self._responder(200, json.dumps(leer_envios(), indent=2, ensure_ascii=False))
        else:
            self._responder(404, json.dumps({"error": "no encontrado"}))

    def do_POST(self):
        if self.path != "/guardar":
            self._responder(404, json.dumps({"error": "ruta invalida"}))
            return
        longitud = int(self.headers.get("Content-Length", 0))
        cuerpo = self.rfile.read(longitud).decode("utf-8")
        tipo = self.headers.get("Content-Type", "")
        if "application/json" in tipo:
            datos = json.loads(cuerpo)
        else:
            datos = {k: v[0] for k, v in parse_qs(cuerpo).items()}
        registro = {
            "nombre": datos.get("nombre", ""),
            "correo": datos.get("correo", ""),
            "mensaje": datos.get("mensaje", ""),
            "fecha": datetime.now().isoformat(timespec="seconds"),
        }
        envios = leer_envios()
        envios.append(registro)
        with open(RESULTADOS, "w", encoding="utf-8") as f:
            json.dump(envios, f, indent=2, ensure_ascii=False)
        self._responder(201, json.dumps({"ok": True}))


def elegir_puerto(preferido=8901):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(("127.0.0.1", preferido))
            return preferido
        except OSError:
            pass
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def main():
    puerto = elegir_puerto()
    servidor = ThreadingHTTPServer(("127.0.0.1", puerto), Manejador)
    print(f"SERVIDOR:http://127.0.0.1:{puerto}", flush=True)
    servidor.serve_forever()


if __name__ == "__main__":
    main()
