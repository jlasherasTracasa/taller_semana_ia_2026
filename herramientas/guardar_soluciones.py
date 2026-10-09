#!/usr/bin/env python3
"""Copia a alumnos/soluciones/ lo que hizo el agente en una ronda de validación (profesor/validar.sh).

Uso:  python3 herramientas/guardar_soluciones.py <carpeta_de_la_ronda> [otra_carpeta_que_tiene_prioridad …]

Por cada ejercicio guarda: el encargo (prompt.txt), la salida real del agente (salida.txt, con las rutas y el usuario
anonimizados), los ficheros que creó o cambió y un SOLUCION.md con el veredicto del comprobador y lo que pasó.
Nunca copia opencode.json, .env, entornos virtuales ni los datos de partida sin cambios.
"""
import filecmp, json, os, re, shutil, subprocess, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KIT = os.path.join(RAIZ, "alumnos")
DEST = os.path.join(KIT, "soluciones")
IDX = {e["id"]: e for e in json.load(open(os.path.join(KIT, "ejercicios", "indice.json"), encoding="utf-8"))["ejercicios"]}
VAL = json.load(open(os.path.join(RAIZ, "herramientas", "validacion.json"), encoding="utf-8"))
NUNCA = {"opencode.json", ".env", "ENUNCIADO.md", "salida.txt", ".salida.txt", ".prompt", "servidor.log"}
DIRS_FUERA = {".venv", "venv", "__pycache__", "node_modules", "unpacked", "intentos", ".git", "tmp", "_tmp", "extraido"}
MAX = 2_000_000  # bytes por fichero


def anonimizar(t, origen):
    t = t.replace(origen, "~/taller-agentes/" + os.path.basename(origen))
    t = re.sub(r"/tmp/claude-[^\s'\"`)]*/scratchpad/r\w+/", "~/taller-agentes/", t)
    t = re.sub(r"/tmp/claude-[^\s'\"`)]*", "/tmp/…", t)
    t = re.sub(r"/home/[^/\s]+/", "~/", t)
    t = re.sub(r"jlasheras@tcsa\.local|usuarios del dominio@tcsa\.local", "alumno", t)
    t = t.replace("tcsa.local", "ejemplo.local")
    for var in ("LITELLM_API_KEY", "OPENROUTER_API_KEY"):  # las claves reales, sin escribirlas aquí
        if len(os.environ.get(var, "")) > 5:
            t = t.replace(os.environ[var], "***")
    t = re.sub(r"sk-[A-Za-z0-9_-]{16,}|ghp_[A-Za-z0-9]{20,}|github_pat_\w{20,}", "***", t)
    return re.sub(r"\x1b\[[0-9;]*m", "", t)


def nuevos(orig, hecho):
    """Ficheros de 'hecho' que no estaban en 'orig' o que han cambiado."""
    for base, dirs, files in os.walk(hecho):
        dirs[:] = [d for d in dirs if d not in DIRS_FUERA]
        for f in files:
            p = os.path.join(base, f)
            rel = os.path.relpath(p, hecho)
            o = os.path.join(orig, rel)
            if f in NUNCA or f.endswith((".pyc", ".log")) or os.path.getsize(p) > MAX:
                continue
            if os.path.exists(o) and filecmp.cmp(o, p, shallow=False):
                continue
            yield rel


def guardar(ej, d):
    e = IDX[ej]
    out = os.path.join(DEST, ej)
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(os.path.join(out, "ficheros"))
    for rel in nuevos(os.path.join(KIT, "ejercicios", ej), d):
        dst = os.path.join(out, "ficheros", rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        src = os.path.join(d, rel)
        try:
            txt = open(src, encoding="utf-8").read()
            open(dst, "w", encoding="utf-8").write(anonimizar(txt, d))
        except (UnicodeDecodeError, ValueError):
            shutil.copy2(src, dst)
    if not os.listdir(os.path.join(out, "ficheros")):
        os.rmdir(os.path.join(out, "ficheros"))
    sal = os.path.join(d, "salida.txt")
    if os.path.exists(sal):
        open(os.path.join(out, "salida.txt"), "w", encoding="utf-8").write(anonimizar(open(sal, encoding="utf-8", errors="replace").read(), d))
    if e.get("prompt"):
        open(os.path.join(out, "prompt.txt"), "w", encoding="utf-8").write(e["prompt"] + "\n")
    comp = subprocess.run([sys.executable, os.path.join(KIT, "comprobar.py"), ej, d], capture_output=True, text=True)
    v = VAL.get(ej, {})
    ico = {"ok": "✅", "parcial": "🟡", "fallo": "❌"}.get(v.get("estado"), "·")
    tok = f" · {v['entrada']:,} tokens de entrada y {v['salida']:,} de salida".replace(",", ".") if v.get("entrada") else ""
    seg = f" · {v['segundos']} s" if v.get("segundos") else ""
    md = [f"# {ico} Solución · {e['num']} · {e['titulo']}", "",
          f"Ejecución real del {v.get('fecha', '')} con opencode 2.0.19 y GLM-5.3-Flash, solo CPU{seg}{tok}.", "",
          "## Qué pasó", "", v.get("nota", "—"), ""]
    if comp.stdout.strip():
        md += ["## Veredicto del comprobador", "", "```text", anonimizar(comp.stdout.strip(), d), "```", ""]
    md += ["## Qué hay en esta carpeta", "",
           "- `prompt.txt`: el encargo exacto." if e.get("prompt") else "- Pasos: los del ENUNCIADO.",
           "- `salida.txt`: lo que dijo e hizo el agente (rutas y usuario anonimizados).",
           "- `ficheros/`: lo que creó o cambió el agente." if os.path.isdir(os.path.join(out, "ficheros")) else "", "",
           "> Las respuestas de un modelo cambian entre ejecuciones. Compara el **criterio**, no el texto.", ""]
    open(os.path.join(out, "SOLUCION.md"), "w", encoding="utf-8").write("\n".join(l for l in md if l is not None))
    return ico


if __name__ == "__main__":
    rondas = sys.argv[1:]
    if not rondas:
        sys.exit(__doc__)
    hechos = {}
    for r in rondas:  # las últimas tienen prioridad
        for ej in IDX:
            if os.path.isdir(os.path.join(r, ej)):
                hechos[ej] = os.path.join(r, ej)
    for ej, d in sorted(hechos.items()):
        print(guardar(ej, d), ej)
    open(os.path.join(DEST, "README.md"), "w", encoding="utf-8").write(
        "# 🧪 Soluciones reales\n\nLo que hizo el agente en la validación, ejercicio por ejercicio: el encargo, la salida y los "
        "ficheros. **Úsalas para comparar, no para copiar**: el sello te lo da `comprobar.py` sobre TU carpeta.\n\n"
        + "\n".join(f"- [{IDX[ej]['num']} · {IDX[ej]['titulo']}]({ej}/SOLUCION.md)" for ej in sorted(hechos, key=list(IDX).index)) + "\n")
