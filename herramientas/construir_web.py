#!/usr/bin/env python3
"""Construye la web de la aventura (GitHub Pages) en _site/ a partir del kit y la wiki.

Uso:  python3 herramientas/construir_web.py        (lo ejecuta también GitHub Actions en cada push a main)
"""
import glob, json, os, re, shutil

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RAIZ, "_site")
REPO = "https://github.com/jlasherasTracasa/taller_semana_ia_2026"
IDX = json.load(open(os.path.join(RAIZ, "alumnos", "ejercicios", "indice.json"), encoding="utf-8"))
VAL = json.load(open(os.path.join(RAIZ, "herramientas", "validacion.json"), encoding="utf-8"))


def enlaces(md):
    """Los enlaces relativos del kit, convertidos a rutas de la web o a GitHub."""
    md = re.sub(r"\]\(\.\./([a-z0-9_]+)/ENUNCIADO\.md\)", r"](#/escena/\1)", md)
    md = re.sub(r"\]\(ejercicios/([a-z0-9_]+)/ENUNCIADO\.md\)", r"](#/escena/\1)", md)
    md = re.sub(r"\]\((?:\.\./\.\./)?ITINERARIOS\.md#[^)]*\)|\]\(#-áreas-y-ejercicios\)", "](#/)", md)
    md = re.sub(r"\]\(\.\./\.\./soluciones/([^)]*)\)", rf"]({REPO}/tree/main/alumnos/soluciones/\1)", md)
    md = re.sub(r"\]\((?:\.\./\.\./)?replicar_paper/README\.md\)", f"]({REPO}/tree/main/alumnos/replicar_paper)", md)
    md = re.sub(r"\]\(\.\./alumnos/ITINERARIOS\.md\)", "](#/)", md)
    md = re.sub(r"\]\(([A-Za-z0-9_-]+)\.md\)", r"](#/wiki/\1)", md)
    return md


def main():
    shutil.rmtree(OUT, ignore_errors=True)
    os.makedirs(os.path.join(OUT, "img"))
    shutil.copytree(os.path.join(RAIZ, "herramientas", "vendor"), os.path.join(OUT, "vendor"))  # marked y mermaid, sin CDN
    for f in ("logo_semana_ia_2026_oscuro.png", "logo_semana_ia_2026_horizontal.png", "logo_semana_ia_2026_horizontal_oscuro.png",
              "encrucijada_semana_ia_2026.jpg", "logo_catedra_ia.png"):
        shutil.copy(os.path.join(RAIZ, "presentacion", "assets", f), os.path.join(OUT, "img", f))
    shutil.copy(os.path.join(RAIZ, "presentacion", "taller-agentes-ia.pdf"), os.path.join(OUT, "taller-agentes-ia.pdf"))
    escenas = {}
    for e in IDX["ejercicios"]:
        p = os.path.join(RAIZ, "alumnos", "ejercicios", e["id"], "ENUNCIADO.md")
        if os.path.exists(p):
            escenas[e["id"]] = enlaces(open(p, encoding="utf-8").read())
    wiki = {os.path.basename(p)[:-3]: enlaces(open(p, encoding="utf-8").read())
            for p in sorted(glob.glob(os.path.join(RAIZ, "wiki", "*.md"))) if not os.path.basename(p).startswith("_")}
    datos = {"indice": IDX, "validacion": VAL, "escenas": escenas, "wiki": wiki, "repo": REPO}
    html = open(os.path.join(RAIZ, "herramientas", "web_plantilla.html"), encoding="utf-8").read()
    html = html.replace("/*DATOS*/null", json.dumps(datos, ensure_ascii=False).replace("</", "<\\/"))
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(html)
    open(os.path.join(OUT, ".nojekyll"), "w").close()
    print(f"_site/ listo: {len(escenas)} escenas, {len(wiki)} páginas de wiki, {len(html) // 1024} KB")


if __name__ == "__main__":
    main()
