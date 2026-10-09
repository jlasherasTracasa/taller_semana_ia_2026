#!/usr/bin/env python3
"""Genera el kit a partir de herramientas/aventura.py (la fuente única):

  alumnos/ejercicios/<id>/ENUNCIADO.md   un enunciado por escena, con sus bifurcaciones
  alumnos/ejercicios/indice.json         lo que usan taller.py, la web y la presentación
  alumnos/AVENTURA.md                    el libro-juego: prólogo, perfiles, mapa, puertas y finales

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
        return "../../AVENTURA.md#-la-plaza" if desde_ejercicio else "#-la-plaza"
    if destino == "replicar_paper":
        return "../../replicar_paper/README.md" if desde_ejercicio else "replicar_paper/README.md"
    return f"../{destino}/ENUNCIADO.md" if desde_ejercicio else f"ejercicios/{destino}/ENUNCIADO.md"


def nombre_destino(destino):
    if destino == "PLAZA":
        return "↩️ La plaza"
    d = A.POR_ID[destino]
    return f"{A.NIVELES[d['nivel']][0]} {d['num']} · {d['titulo']}"


def enunciado(e):
    p = A.PUERTAS[e["puerta"]]
    ico, nivel, _ = A.NIVELES[e["nivel"]]
    perf = " ".join(A.PERFILES[x]["icono"] for x in e["perfiles"])
    modo = {"run": "`opencode run`", "interactivo": "`opencode` interactivo", "script": "tu propio programa en Python",
            "varios": "varios pasos"}[e["modo"]]
    L = [f"# {ico} {e['num']} · {e['titulo']}", "",
         f"> {p['icono']} **Puerta {e['puerta']} · {p['nombre']}** · {ico} {nivel} · ⏱ {e['min']} min · "
         f"🛠️ {modo} · Recomendado para: {perf}", "",
         "## 📖 La escena", "", e["escena"], "",
         "## 🎯 Objetivo", "", e["objetivo"], ""]
    if e["datos"]:
        L += ["## 📦 Lo que tienes en esta carpeta", ""] + [f"- {x}" for x in e["datos"]] + [""]
    L += ["## 💬 El encargo", ""]
    if e["pasos"]:
        L += [e["pasos"], ""]
    elif e["prompt"]:
        L += ["Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):", "", "```bash",
              f"python3 taller.py lanzar {corto(e)}", "```", "",
              "O a mano, desde la carpeta de trabajo del ejercicio:", "", "```bash",
              f'opencode run --standalone "{e["prompt"]}" | tee salida.txt', "```", ""]
    if e["modo"] == "run" and e["prompt"]:
        L += ["> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, "
              "entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.", ""]
    L += ["## ✅ ¿Lo ha hecho de verdad?", ""] + [f"- {x}" for x in e["criterio"]] + [""]
    if corto(e) not in ("f0", "f1", "f9", "ej21", "reto"):
        L += ["```bash", f"python3 taller.py comprobar {corto(e)}      # el agente no puede darte el sello: solo el comprobador",
              "```", ""]
    if e["pistas"]:
        L += ["## 💡 Pistas", ""] + [f"- {x}" for x in e["pistas"]] + [""]
    if e["reto"]:
        L += ["## 🧗 Reto extra", "", e["reto"], ""]
    v = VAL.get(e["id"])
    if v:
        L += [f"## 🧪 Lo que pasó al validarlo ({v.get('fecha', A.FECHA_VALIDACION)})", "", v["nota"], ""]
        if v.get("solucion"):
            L += [f"Prompt, salida real y ficheros: [`soluciones/{e['id']}/`](../../soluciones/{e['id']}/)", ""]
    if e["siguiente"]:
        L += ["## 🔀 ¿Y ahora qué?", ""]
        L += [f"- **{t}** → [{nombre_destino(d)}]({enlace(d)})" for t, d in e["siguiente"]] + [""]
    return "\n".join(L)


def mermaid():
    L = ["```mermaid", "flowchart LR",
         '  P(("🏛️ La plaza<br/>Puente la Reina"))']
    for k, p in A.PUERTAS.items():
        L.append(f'  {k}["{p["icono"]} {p["nombre"]}<br/><small>{p["tema"]}</small>"]')
        L.append(f"  P --> {k}")
    for k in "ABCDF":
        L.append(f"  {k} -.-> X")
    L += ['  X --> FIN{{"🏁 Finales<br/>🥉 🥈 🥇"}}', '  F --> R["🏔️ La torre<br/>replicar un paper"]', "  R --> FIN",
          "  classDef jefe fill:#7a1f1f,color:#fff,stroke:#f2a93b;", "  class X jefe;", "```"]
    return "\n".join(L)


def aventura_md(indice):
    L = ["# 🧭 Elige tu propia aventura · Agentes de IA en Puente la Reina", "",
         "> Taller «Más allá de ChatGPT: crea y conecta agentes de IA» · Semana de la IA 2026 · UPNA · "
         "viernes 23 de octubre", "", A.PROLOGO, "", "## 🗺️ El mapa", "", mermaid(), "",
         "## 🧑‍🤝‍🧑 ¿Quién eres?", "",
         "Elige el perfil que más se parezca a ti. Es solo una ruta recomendada: puedes cambiar de puerta cuando quieras.", ""]
    for k, p in A.PERFILES.items():
        ruta = " → ".join(f"[{A.POR_ID[i]['num']}]({enlace(i, False)})" for i in p["ruta"])
        L += [f"### {p['icono']} {p['nombre']}", "", f"*{p['quien']}*", "", f"**Ruta:** {ruta}", "", f"💡 {p['consejo']}", ""]
    L += ["## 📶 Niveles", "", "| | Nivel | Para quién |", "|---|---|---|"]
    L += [f"| {i} | {n} | {t} |" for i, n, t in A.NIVELES.values()] + [""]
    L += ["## 🏛️ La plaza", "", "Desde aquí sale todo. Elige una puerta (y vuelve cuando quieras):", ""]
    for k, p in A.PUERTAS.items():
        ejs = [e for e in A.E if e["puerta"] == k]
        L += [f"### {p['icono']} Puerta {k} · {p['nombre']}", "", f"*{p['texto']}*", "",
              "| | Escena | ⏱ | Para |", "|---|---|---|---|"]
        for e in ejs:
            perf = " ".join(A.PERFILES[x]["icono"] for x in e["perfiles"])
            L.append(f"| {A.NIVELES[e['nivel']][0]} | [{e['num']} · {e['titulo']}]({enlace(e['id'], False)}) | {e['min']}' | {perf} |")
        L.append("")
    L += ["### 🏔️ La torre", "", "Reto final para quien quiera más: replicar en CPU un paper de encoders legales en "
          "español. → [replicar_paper/](replicar_paper/README.md)", ""]
    L += ["## 🏁 Los finales", "", "Tu pasaporte (`python3 taller.py pasaporte`) te dice a cuál has llegado.", "",
          "| | Final | Cómo se llega | Qué te llevas |", "|---|---|---|---|"]
    L += [f"| {a} | **{b}** | {c} | {d} |" for a, b, c, d in A.FINALES] + [""]
    L += ["## 🎮 Cómo se juega", "", "```bash",
          "python3 taller.py                 # la plaza: perfiles, puertas y tu pasaporte",
          "python3 taller.py empezar ej01    # prepara la carpeta y te cuenta la escena",
          "python3 taller.py lanzar ej01     # el agente hace el encargo",
          "python3 taller.py comprobar ej01  # ¿lo hizo de verdad? Si sí: 🏅 y te propone adónde ir",
          "```", ""]
    return "\n".join(L)


def main():
    lista = []
    for e in A.E:
        x = {k: v for k, v in e.items() if k in ("id", "num", "titulo", "puerta", "nivel", "min", "modo", "perfiles",
                                                 "escena", "objetivo", "prompt", "criterio", "siguiente")}
        x["num_corto"] = corto(e)
        x["puerta_icono"] = A.PUERTAS[e["puerta"]]["icono"] if e["puerta"] in A.PUERTAS else "🏔️"
        x["validacion"] = VAL.get(e["id"])
        lista.append(x)
        if e["id"] == "replicar_paper":
            continue
        open(os.path.join(EJ_DIR, e["id"], "ENUNCIADO.md"), "w", encoding="utf-8").write(enunciado(e))
    puertas = dict(A.PUERTAS)
    puertas["R"] = {"icono": "🏔️", "nombre": "La torre", "tema": "Reto final", "texto": "Replicar un paper en CPU."}
    indice = {"ejercicios": lista, "puertas": puertas, "perfiles": A.PERFILES,
              "niveles": {str(k): v for k, v in A.NIVELES.items()},
              "finales": A.FINALES, "prologo": A.PROLOGO,
              "prologo_corto": "\n🏛️  LA PLAZA · Puente la Reina / Gares\n\n" + A.PROLOGO.split("\n\n")[1] + "\n",
              "fecha_validacion": A.FECHA_VALIDACION, "opencode": A.OPENCODE, "modelo": A.MODELO}
    json.dump(indice, open(os.path.join(EJ_DIR, "indice.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    open(os.path.join(RAIZ, "alumnos", "AVENTURA.md"), "w", encoding="utf-8").write(aventura_md(indice))
    print(f"{len(lista)} escenas · ENUNCIADO.md, indice.json y AVENTURA.md regenerados")


if __name__ == "__main__":
    main()
