# -*- coding: utf-8 -*-
"""Paso 1 de la réplica: descarga de pasajes legales/administrativos públicos.

Fuente: Leyes del BOE en texto consolidado, vía la API oficial de datos abiertos
(https://www.boe.es/datosabiertos/documentos/LegislacionConsolidada.html).
Los textos del BOE son datos oficiales de dominio público (art. 13 de la Ley
23/2014, de acceso a la información pública), por lo que pueden descargarse y
reutilizarse libremente citando la fuente. Respetamos el servicio con una pausa
de 2 segundos entre peticiones y una lista cerrada de 7 normas (unas 400
pasajes), lejos de un volcado masivo.

Salida: data/pasajes.json  [{id, doc, titulo, texto}]
"""
import json
import random
import re
import time
import urllib.request
from pathlib import Path

SEED = 42
random.seed(SEED)

OUT_DIR = Path(__file__).parent / "data"
OUT_DIR.mkdir(exist_ok=True)

# Leyes consolidadas en vigor (identificador BOE, título corto, nº máx. de pasajes).
NORMAS = [
    ("BOE-A-1995-25444", "Código Penal", 90),
    ("BOE-A-2015-11430", "Ley del Estatuto de los Trabajadores", 70),
    ("BOE-A-2015-10565", "Ley 39/2015, del Procedimiento Administrativo Común", 70),
    ("BOE-A-2017-12902", "Ley de Contratos del Sector Público", 60),
    ("BOE-A-2018-16673", "Ley de Protección de Datos Personales", 60),
    ("BOE-A-2023-12668", "Ley de Vivienda", 50),
    ("BOE-A-2011-9617", "Ley de Economía Sostenible", 40),
]

API = "https://boe.es/datosabiertos/api/legislacion-consolidada/id/{}"
HEADERS = {"Accept": "application/xml"}
MIN_PALABRAS, MAX_PALABRAS = 150, 250


def descargar(id_norma):
    req = urllib.request.Request(API.format(id_norma), headers=HEADERS)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8")


def extraer_articulos(xml):
    """Devuelve [(titulo_articulo, texto)] a partir del XML consolidado."""
    arts = []
    for m in re.finditer(r'<bloque[^>]*tipo="precepto"[^>]*>(.*?)</bloque>', xml, re.S):
        bloque = m.group(1)
        # Nos quedamos con la versión vigente (la primera de cada bloque).
        v = re.search(r"<version\b.*?</version>", bloque, re.S)
        if not v:
            continue
        cuerpo = v.group(0)
        titulo_m = re.search(r"<p class=\"articulo\">(.*?)</p>", cuerpo, re.S)
        parrafos = re.findall(r"<p class=\"parrafo\">(.*?)</p>", cuerpo, re.S)
        texto = re.sub(r"<[^>]+>", " ", " ".join(parrafos))
        texto = re.sub(r"\s+", " ", texto).strip()
        titulo = _limpia(titulo_m.group(1)) if titulo_m else ""
        if texto:
            arts.append((titulo, texto))
    return arts


def _limpia(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()


def trocear(texto):
    """Trocea en pasajes de MIN-MAX palabras, cortando en frases completas.
    Las frases larguísimas se subdividen por comas (o a la bruta, en último caso)."""
    frases = re.split(r"(?<=[.;])\s+", texto)
    pasajes, actual, n = [], [], 0

    def cierra():
        nonlocal actual, n
        if n >= MIN_PALABRAS:
            pasajes.append(" ".join(actual))
        actual, n = [], 0

    for f in frases:
        if len(f.split()) > MAX_PALABRAS:
            subs = []
            for parte in re.split(r",\s+", f):
                if len(parte.split()) > MAX_PALABRAS:
                    w = parte.split()
                    subs += [" ".join(w[i:i + MAX_PALABRAS])
                             for i in range(0, len(w), MAX_PALABRAS)]
                else:
                    subs.append(parte)
        else:
            subs = [f]
        for sf in subs:
            sw = len(sf.split())
            if n + sw > MAX_PALABRAS:
                cierra()
            actual.append(sf)
            n += sw
    cierra()
    return pasajes


def main():
    t0 = time.time()
    pasajes = []
    for id_norma, titulo, max_pas in NORMAS:
        print(f"[datos] Descargando {id_norma} ({titulo})...")
        try:
            xml = descargar(id_norma)
        except Exception as e:
            print(f"  !! fallo ({str(e)[:80]}), se omite esta norma")
            continue
        arts = extraer_articulos(xml)
        hechos = 0
        for i, (tit_art, texto) in enumerate(arts):
            if hechos >= max_pas:
                break
            for p in trocear(texto):
                pasajes.append({"id": f"{id_norma}-{len(pasajes):04d}",
                                "doc": id_norma,
                                "titulo": f"{titulo} · {tit_art}",
                                "texto": p})
                hechos += 1
                if hechos >= max_pas:
                    break
        print(f"  {hechos} pasajes")
        time.sleep(2)  # cortesía con el servicio público
    with open(OUT_DIR / "pasajes.json", "w", encoding="utf-8") as f:
        json.dump(pasajes, f, ensure_ascii=False, indent=1)
    print(f"[datos] Total: {len(pasajes)} pasajes · "
          f"{len({p['doc'] for p in pasajes})} documentos · "
          f"{time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
