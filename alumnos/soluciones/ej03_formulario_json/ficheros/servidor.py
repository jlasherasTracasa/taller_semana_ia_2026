#!/usr/bin/env python3
"""Servidor mínimo (stdlib) para el formulario del taller de pan.
POST /enviar -> guarda el envío en resultados.json
"""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

RESULTADOS = "resultados.json"


class Manejador(BaseHTTPRequestHandler):
    def _respuesta(self, codigo, cuerpo, ctype):
        data = cuerpo.encode("utf-8")
        self.send_response(codigo)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        try:
            with open("formulario.html", "rb") as f:
                self._respuesta(200, f.read().decode("utf-8"), "text/html; charset=utf-8")
        except FileNotFoundError:
            self._respuesta(404, "formulario.html no encontrado", "text/plain; charset=utf-8")

    def do_POST(self):
        if self.path != "/enviar":
            self._respuesta(404, "ruta no encontrada", "text/plain; charset=utf-8")
            return
        n = int(self.headers.get("Content-Length", 0))
        campos = parse_qs(self.rfile.read(n).decode("utf-8"))
        registro = {
            "nombre": campos.get("nombre", [""])[0],
            "correo": campos.get("correo", [""])[0],
            "mensaje": campos.get("mensaje", [""])[0],
        }
        try:
            with open(RESULTADOS, encoding="utf-8") as f:
                datos = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            datos = []
        datos.append(registro)
        with open(RESULTADOS, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=2)
        self._respuesta(200, "<h1>¡Inscripción guardada!</h1>", "text/html; charset=utf-8")

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    HTTPServer(("127.0.0.1", 8901), Manejador).serve_forever()
