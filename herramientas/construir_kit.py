#!/usr/bin/env python3
"""Genera el kit a partir de herramientas/aventura.py (la fuente única):

  alumnos/ejercicios/<id>/ENUNCIADO.md   un enunciado por escena, con sus bifurcaciones
  alumnos/ejercicios/indice.json         lo que usan taller.py, la web y la presentación
  alumnos/ITINERARIOS.md                    el libro-juego: prólogo, perfiles, mapa, puertas y finales

Uso:  python3 herramientas/construir_kit.py
"""
import json, os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "herramientas"))
import aventura as A  # noqa: E402

EJ_DIR = os.path.join(RAIZ, "alumnos", "ejercicios")
VALID = os.path.join(RAIZ, "herramientas", "validacion.json")
VAL = json.load(open(VALID, encoding="utf-8")) if os.path.exists(VALID) else {}


def corto(e):
    if e["id"] == "replicar_paper":
        return "reto"
    m = re.match(r"(ej|f)(\d+)_", e["id"])
    return f"{m.group(1)}{int(m.group(2)):02d}" if m.group(1) == "ej" else f"f{int(m.group(2))}"


def enlace(destino, desde_ejercicio=True):
    if destino == "PLAZA":
        return "../../ITINERARIOS.md#-áreas-y-ejercicios" if desde_ejercicio else "#-áreas-y-ejercicios"
    if destino == "replicar_paper":
        return "../../replicar_paper/README.md" if desde_ejercicio else "replicar_paper/README.md"
    return f"../{destino}/ENUNCIADO.md" if desde_ejercicio else f"ejercicios/{destino}/ENUNCIADO.md"


def nombre_destino(destino):
    if destino == "PLAZA":
        return "↩️ Inicio: todas las áreas"
    d = A.POR_ID[destino]
    return f"{A.NIVELES[d['nivel']][0]} {d['num']} · {d['titulo']}"


def enunciado(e):
    p = A.PUERTAS[e["puerta"]]
    ico, nivel, _ = A.NIVELES[e["nivel"]]
    perf = " ".join(A.PERFILES[x]["icono"] for x in e["perfiles"])
    modo = {"run": "opencode interactivo", "interactivo": "solo opencode interactivo", "script": "tu propio programa en Python",
            "varios": "varios pasos"}[e["modo"]]
    quien = ("🎥 **Demo en directo**: lo hace el profesor en el proyector; tú lo miras y lo repites después si quieres."
             if e.get("demo") else "✋ **Práctica**: lo haces tú, a tu ritmo. Si te atascas, pregunta al profesor.")
    L = [f"# {ico} {e['num']} · {e['titulo']}", "",
         f"> {p['icono']} **{p['nombre']}** · {ico} {nivel} · ⏱ {e['min']} min · "
         f"🛠️ {modo} · Recomendado para: {perf}", "", f"> {quien}", "",
         "## 📌 La situación", "", e["escena"], "",
         "## 🎯 Objetivo", "", e["objetivo"], ""]
    if e["datos"]:
        L += ["## 📦 Lo que tienes en esta carpeta", ""] + [f"- {x}" for x in e["datos"]] + [""]
    L += ["## 💬 El encargo", ""]
    if e["pasos"]:
        L += [e["pasos"], ""]
    elif e["prompt"]:
        L += ["**1.** Abre opencode en modo interactivo en tu carpeta de trabajo:", "", "```bash",
              f"python taller.py abrir {corto(e)}", "```", "",
              "**2.** Copia este encargo, pégalo en opencode y pulsa Enter:", "", "```text", e["prompt"], "```", "",
              "**3.** Mira lo que hace: qué ficheros lee, qué órdenes ejecuta, si te pide permiso. Cuando termine, sal con "
              "`Ctrl+C` (o sigue conversando: «revisa que…», «corrige…»).", "",
              "<details><summary>Sin conversar, de una vez (opcional)</summary>", "", "```bash",
              f"python taller.py lanzar {corto(e)}", "```", "",
              f"O a mano, desde la carpeta de trabajo: `opencode run --standalone \"…el encargo…\"`.", "", "</details>", ""]
    if e["modo"] == "run" and e["prompt"]:
        L += ["> 💡 Antes de pegarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, "
              "entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.", ""]
    L += ["## ✅ ¿Lo ha hecho de verdad?", ""] + [f"- {x}" for x in e["criterio"]] + [""]
    if corto(e) not in ("f0", "f1", "f9", "reto"):
        L += ["```bash", f"python taller.py comprobar {corto(e)}      # el agente no decide si está bien: lo decide el comprobador",
              "```", ""]
    if e["pistas"]:
        L += ["## 💡 Pistas", ""] + [f"- {x}" for x in e["pistas"]] + [""]
    if e["reto"]:
        L += ["## 🧗 Reto extra", "", e["reto"], ""]
    v = VAL.get(e["id"])
    if v:
        if v.get("solucion"):
            L += ["## 📂 Una solución de ejemplo", "",
                  f"¿Te has atascado o no puedes ejecutarlo? Mira lo que hizo el agente con este encargo (el encargo, lo que "
                  f"escribió en pantalla y los ficheros): [`soluciones/{e['id']}/`](../../soluciones/{e['id']}/)", ""]
    if e["siguiente"]:
        L += ["## 🔀 Siguiente paso", ""]
        L += [f"- **{t}** → [{nombre_destino(d)}]({enlace(d)})" for t, d in e["siguiente"]] + [""]
    return "\n".join(L)


def mermaid():
    L = ["```mermaid", "flowchart LR",
         '  P(("👤 Tu perfil"))']
    for k, p in A.PUERTAS.items():
        L.append(f'  {k}["{p["icono"]} {p["nombre"]}<br/><small>{p["tema"]}</small>"]')
        L.append(f"  P --> {k}")
    for k in "ABCDF":
        L.append(f"  {k} -.-> X")
    L += ['  X --> FIN{{"🎯 Nivel alcanzado<br/>básico · intermedio · avanzado"}}', '  F --> R["🔬 Reto avanzado<br/>replicar un artículo"]', "  R --> FIN",
          "  classDef seg fill:#5a2a24,color:#fff,stroke:#e4b858;", "  class X seg;", "```"]
    return "\n".join(L)


def aventura_md(indice):
    L = ["# 🧭 Itinerarios del taller · Elige tu camino", "",
         "> Taller «Más allá de ChatGPT: crea y conecta agentes de IA» · Semana de la IA 2026 · UPNA · "
         "viernes 23 de octubre", "", A.PROLOGO, "", "## 🗺️ Mapa", "", mermaid(), "",
         "## 👤 Elige tu perfil", "",
         "Elige el perfil que más se parezca a ti. Es un itinerario recomendado: puedes cambiar de área cuando quieras.", ""]
    for k, p in A.PERFILES.items():
        ruta = " → ".join(f"[{A.POR_ID[i]['num']}]({enlace(i, False)})" for i in p["ruta"])
        L += [f"### {p['icono']} {p['nombre']}", "", f"*{p['quien']}*", "", f"**Itinerario:** {ruta}", "", f"💡 {p['consejo']}", ""]
    L += ["## 🎥 Demos en directo y ✋ prácticas", "",
          "- **🎥 Demo en directo**: la hace el profesor en el proyector, explicando cada paso. Tú miras (y, si quieres, la repites después).",
          "- **✋ Práctica**: la haces tú en tu ordenador, a tu ritmo, en clase o en casa. Cuando te atasques o algo no "
          "cuadre, **pregunta al profesor**: para eso está.", "",
          "Demos: " + " · ".join(f"[{e['num']} · {e['titulo']}]({enlace(e['id'], False)})" for e in A.E if e.get("demo")), "",
          "## 📶 Niveles", "", "| | Nivel | Para quién |", "|---|---|---|"]
    L += [f"| {i} | {n} | {t} |" for i, n, t in A.NIVELES.values()] + [""]
    L += ["## 📚 Áreas y ejercicios", "", "Elige un área y un ejercicio. Cada uno te propone el siguiente paso al terminar.", ""]
    for k, p in A.PUERTAS.items():
        ejs = [e for e in A.E if e["puerta"] == k]
        L += [f"### {p['icono']} {p['nombre']}", "", f"*{p['texto']}*", "",
              "| | Ejercicio | Quién | ⏱ | Perfiles |", "|---|---|---|---|---|"]
        for e in ejs:
            perf = " ".join(A.PERFILES[x]["icono"] for x in e["perfiles"])
            quien = "🎥 demo" if e.get("demo") else "✋ tú"
            L.append(f"| {A.NIVELES[e['nivel']][0]} | [{e['num']} · {e['titulo']}]({enlace(e['id'], False)}) | {quien} | {e['min']}' | {perf} |")
        L.append("")
    L += ["### 🔬 Reto avanzado", "", "Para quien quiera más: replicar en CPU un artículo científico sobre encoders "
          "legales en español. → [replicar_paper/](replicar_paper/README.md)", ""]
    L += ["## 🎯 Niveles", "", "`python taller.py progreso` te dice qué nivel has alcanzado.", "",
          "| | Nivel | Cómo se llega | Qué te llevas |", "|---|---|---|---|"]
    L += [f"| {a} | **{b}** | {c} | {d} |" for a, b, c, d in A.FINALES] + [""]
    L += ["## ▶️ Cómo se trabaja", "", "Con el entorno activado (`.venv\\Scripts\\Activate.ps1` en Windows, "
          "`. .venv/bin/activate` en Mac y Linux):", "", "```bash",
          "python taller.py                 # perfiles, áreas y tu progreso",
          "python taller.py empezar ej24    # prepara la carpeta y te explica la situación",
          "python taller.py abrir ej24      # abre opencode en modo interactivo: pega el encargo y míralo trabajar",
          "python taller.py comprobar ej24  # ¿lo hizo de verdad? Si sí, queda completado y te propone el siguiente paso",
          "```", "", "También en la web: https://jlasherastracasa.github.io/taller_semana_ia_2026/", ""]
    return "\n".join(L)


def main():
    lista = []
    for e in A.E:
        x = {k: v for k, v in e.items() if k in ("id", "num", "titulo", "puerta", "nivel", "min", "modo", "perfiles",
                                                 "escena", "objetivo", "prompt", "criterio", "siguiente", "demo")}
        x["num_corto"] = corto(e)
        x["puerta_icono"] = A.PUERTAS[e["puerta"]]["icono"] if e["puerta"] in A.PUERTAS else "🔬"
        x["validacion"] = VAL.get(e["id"])
        lista.append(x)
        if e["id"] == "replicar_paper":
            continue
        open(os.path.join(EJ_DIR, e["id"], "ENUNCIADO.md"), "w", encoding="utf-8").write(enunciado(e))
    puertas = dict(A.PUERTAS)
    puertas["R"] = {"icono": "🔬", "nombre": "Reto avanzado", "tema": "Investigación", "texto": "Replicar un artículo científico en CPU."}
    indice = {"ejercicios": lista, "puertas": puertas, "perfiles": A.PERFILES,
              "niveles": {str(k): v for k, v in A.NIVELES.items()},
              "finales": A.FINALES, "prologo": A.PROLOGO,
              "prologo_corto": "\n🧭  TALLER DE AGENTES DE IA · itinerarios\n\n" + A.PROLOGO.split("\n\n")[0] + "\n",
              "fecha_validacion": A.FECHA_VALIDACION, "opencode": A.OPENCODE, "modelo": A.MODELO}
    json.dump(indice, open(os.path.join(EJ_DIR, "indice.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    open(os.path.join(RAIZ, "alumnos", "ITINERARIOS.md"), "w", encoding="utf-8").write(aventura_md(indice))
    print(f"{len(lista)} ejercicios · ENUNCIADO.md, indice.json y ITINERARIOS.md regenerados")


if __name__ == "__main__":
    main()
