#!/usr/bin/env python3
"""El mando de la aventura. Solo usa la biblioteca estándar: funciona igual en Linux, macOS y Windows.

  python3 taller.py                      la plaza: perfiles, puertas y tu pasaporte
  python3 taller.py empezar ej01         prepara la carpeta de trabajo del ejercicio y te cuenta la escena
  python3 taller.py lanzar ej01          ejecuta el encargo del enunciado con opencode (guarda salida.txt)
  python3 taller.py lanzar ej01 --prompt "tu propio encargo"
  python3 taller.py abrir ej21           abre opencode en modo interactivo en la carpeta del ejercicio
  python3 taller.py ejecutar f0 react_min.py [args]   ejecuta un script del ejercicio con tu .env cargado
  python3 taller.py comprobar ej01       pasa el comprobador; si todo está bien, te sella el pasaporte 🏅
  python3 taller.py pasaporte            tus sellos y a qué final has llegado

Las carpetas de trabajo van a ~/taller-agentes/ (cámbialo con la variable TALLER_TRABAJO).
Las claves se leen del fichero .env de este kit; nunca se copian a las carpetas de trabajo.
"""
import json, os, re, shutil, subprocess, sys, time

KIT = os.path.dirname(os.path.abspath(__file__))
TRABAJO = os.path.expanduser(os.environ.get("TALLER_TRABAJO", "~/taller-agentes"))
INDICE = json.load(open(os.path.join(KIT, "ejercicios", "indice.json"), encoding="utf-8"))
EJS = {e["id"]: e for e in INDICE["ejercicios"]}
PASAPORTE = os.path.join(TRABAJO, "pasaporte.json")
WIN = os.name == "nt"


def cargar_env():
    """Lee .env del kit (si existe) y lo añade al entorno. No imprime nunca los valores."""
    env = dict(os.environ)
    ruta = os.path.join(KIT, ".env")
    if os.path.exists(ruta):
        for linea in open(ruta, encoding="utf-8"):
            linea = linea.split("#", 1)[0].strip()
            if "=" in linea:
                k, v = linea.split("=", 1)
                if v.strip():
                    env.setdefault(k.strip(), v.strip())
    return env


def buscar(clave):
    """'ej1', 'EJ 01', 'f.4', 'f4_skills' → id del ejercicio."""
    if clave in EJS:
        return clave
    m = re.match(r"(ej|f)(\d+)", clave.lower().replace(" ", "").replace(".", ""))
    if m:
        prefijo = f"ej{int(m.group(2)):02d}_" if m.group(1) == "ej" else f"f{int(m.group(2))}_"
        for i in EJS:
            if i.startswith(prefijo):
                return i
    if clave.lower() in ("reto", "paper", "replicar_paper"):
        return "replicar_paper"
    sys.exit(f"No encuentro el ejercicio «{clave}». Mira la lista con:  python3 taller.py")


def carpeta(ej):
    return os.path.join(TRABAJO, ej)


def config_opencode(ej, destino, env):
    """opencode.json del kit + el bloque mcp propio del ejercicio, si lo trae. Elige proveedor según las claves."""
    cfg = json.load(open(os.path.join(KIT, "opencode.json"), encoding="utf-8"))
    propio = os.path.join(KIT, "ejercicios", ej, "opencode.json")
    if os.path.exists(propio):
        for k, v in json.load(open(propio, encoding="utf-8")).items():
            if k != "permission":
                cfg[k] = v
    if env.get("OPENROUTER_API_KEY") and not env.get("LITELLM_API_KEY"):
        cfg["model"] = env.get("TALLER_MODELO_OPENROUTER", "openrouter/z-ai/glm-5.3-flash")
    json.dump(cfg, open(os.path.join(destino, "opencode.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)


def empezar(ej, silencioso=False):
    e, d, env = EJS[ej], carpeta(ej), cargar_env()
    if os.path.exists(d):
        if not silencioso:
            print(f"La carpeta {d} ya existe: la dejo como está (bórrala tú si quieres empezar de cero).")
    else:
        shutil.copytree(os.path.join(KIT, "ejercicios", ej), d)
        config_opencode(ej, d, env)
    if not silencioso:
        n = INDICE["niveles"][str(e["nivel"])]
        print(f"\n{e['puerta_icono']} {e['num']} · {e['titulo']}   {n[0]} {n[1]} · ⏱ {e['min']} min\n")
        print(f"📖 {e['escena']}\n")
        print(f"📁 Tu carpeta: {d}")
        if e.get("prompt") and e["modo"] == "run":
            print(f"\n💬 El encargo:\n   {e['prompt']}\n\n▶️  Lánzalo:  python3 taller.py lanzar {e['num_corto']}")
        else:
            print(f"\n📄 Este ejercicio tiene pasos propios: léelos en {os.path.join(d, 'ENUNCIADO.md')}")
            if e["modo"] == "interactivo":
                print(f"▶️  Abre opencode ahí:  python3 taller.py abrir {e['num_corto']}")
        print(f"✅ Y luego:   python3 taller.py comprobar {e['num_corto']}\n")
    return d


def opencode(args, d, env, salida=None):
    cmd = ["opencode"] + args
    if salida is None:
        return subprocess.call(cmd, cwd=d, env=env, shell=WIN)
    with open(salida, "w", encoding="utf-8") as f:
        p = subprocess.Popen(cmd, cwd=d, env=env, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace", shell=WIN)
        for linea in p.stdout:
            linea = re.sub(r"\x1b\[[0-9;]*m", "", linea)
            print(linea, end="")
            f.write(linea)
        return p.wait()


# Precio de GLM-5.3-Flash en OpenRouter (dólares por millón de tokens, octubre de 2026)
PRECIO = {"entrada": 0.15, "salida": 0.50}


def coste(entrada, salida):
    return (entrada * PRECIO["entrada"] + salida * PRECIO["salida"]) / 1e6


def tokens(d, env):
    """Tokens gastados en la carpeta d según las estadísticas de opencode."""
    try:
        r = subprocess.run(["opencode", "stats", "--standalone", "--json", "--all", "--project", "."], cwd=d, env=env,
                           stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=120, shell=WIN)
        t = json.loads(r.stdout)["tokens"]
        return {"entrada": t["input"] + t["cache"]["read"], "salida": t["output"] + t.get("reasoning", 0)}
    except Exception:
        return {"entrada": 0, "salida": 0}


def lanzar(ej, prompt=None):
    e, env = EJS[ej], cargar_env()
    d = empezar(ej, silencioso=True)
    prompt = prompt or e.get("prompt")
    if not prompt:
        sys.exit("Este ejercicio no se lanza con un único encargo: sigue los pasos de su ENUNCIADO.md.")
    if not (env.get("LITELLM_API_KEY") or env.get("OPENROUTER_API_KEY")):
        sys.exit("Falta la clave: copia .env.example a .env en la carpeta del kit y rellénala.")
    print(f"🤖 Encargo: {prompt}\n")
    t0 = time.time()
    rc = opencode(["run", "--standalone", prompt], d, env, salida=os.path.join(d, "salida.txt"))
    print(f"\n⏱ {time.time() - t0:.0f} s · código {rc} · salida guardada en salida.txt")
    t = tokens(d, env)
    if t["entrada"]:
        print(f"🪙 Tokens acumulados en esta carpeta: {t['entrada']:,} de entrada y {t['salida']:,} de salida "
              f"(≈ {coste(t['entrada'], t['salida']):.4f} $ en OpenRouter)")
    print(f"✅ ¿Lo ha hecho de verdad?  python3 taller.py comprobar {e['num_corto']}")
    return rc


def abrir(ej):
    d = empezar(ej, silencioso=True)
    print(f"Abriendo opencode en {d} (sal con Ctrl+C)…")
    return opencode([], d, cargar_env())


def ejecutar(ej, script, args):
    d = empezar(ej, silencioso=True)
    env = cargar_env()
    env["TALLER_KIT"] = KIT
    return subprocess.call([sys.executable, script] + args, cwd=d, env=env)


def leer_pasaporte():
    try:
        return json.load(open(PASAPORTE, encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def comprobar(ej):
    e, d = EJS[ej], carpeta(ej)
    if not os.path.isdir(d):
        sys.exit(f"Aún no has empezado {e['num']}:  python3 taller.py empezar {e['num_corto']}")
    rc = subprocess.call([sys.executable, os.path.join(KIT, "comprobar.py"), ej, d])
    if rc == 0:
        p = leer_pasaporte()
        p[ej] = time.strftime("%Y-%m-%d %H:%M")
        os.makedirs(TRABAJO, exist_ok=True)
        json.dump(p, open(PASAPORTE, "w", encoding="utf-8"), indent=1)
        print(f"\n🏅 ¡Sello conseguido! {e['puerta_icono']} {e['num']} · {e['titulo']}")
    else:
        print("\nSin sello todavía. Mejora el encargo (más CONTEXTO, LÍMITES y CRITERIO) y vuelve a lanzarlo.")
    if e.get("siguiente"):
        print("\n🔀 ¿Y ahora qué?")
        for texto, destino in e["siguiente"]:
            if destino == "PLAZA":
                print(f"   ↩️  {texto}:  python3 taller.py")
            else:
                print(f"   ➡️  {texto}:  python3 taller.py empezar {EJS[destino]['num_corto']}")
    return rc


def final(p):
    puertas = {EJS[i]["puerta"] for i in p if i in EJS}
    expertos = any(EJS[i]["nivel"] == 4 for i in p if i in EJS)
    jefe = "ej10_inyeccion_prompt" in p
    if jefe and puertas >= {"A", "B", "C", "D", "F"} and expertos:
        return 2
    if jefe and len(p) >= 7 and len(puertas - {"X"}) >= 3:
        return 1
    if jefe and len(p) >= 4:
        return 0
    return None


def pasaporte():
    p = leer_pasaporte()
    print(f"\n🛂 Tu pasaporte · {len(p)} sello(s)\n")
    for clave, puerta in INDICE["puertas"].items():
        sellos = [EJS[i] for i in p if i in EJS and EJS[i]["puerta"] == clave]
        print(f"  {puerta['icono']} {puerta['nombre']:24} " + (" ".join(f"🏅{s['num']}" for s in sellos) or "·"))
    f = final(p)
    if f is not None:
        ico, nombre, _, texto = INDICE["finales"][f]
        print(f"\n{ico} FINAL «{nombre}». {texto}")
    else:
        print("\nAún no has llegado a ningún final: el primero pide 3 sellos y vencer al 🐉 correo envenenado (EJ 10).")


def plaza():
    print(INDICE["prologo_corto"])
    print("¿Quién eres? Cada perfil tiene una ruta recomendada (pero puedes ir donde quieras):\n")
    for p in INDICE["perfiles"].values():
        ruta = " → ".join(EJS[i]["num"] for i in p["ruta"] if i in EJS)
        print(f"  {p['icono']} {p['nombre']}: {p['quien']}\n     Ruta: {ruta}\n")
    print("Las puertas:\n")
    for clave, puerta in INDICE["puertas"].items():
        ejs = [e for e in INDICE["ejercicios"] if e["puerta"] == clave]
        print(f"  {puerta['icono']} {puerta['nombre']} · {puerta['tema']}")
        for e in ejs:
            n = INDICE["niveles"][str(e["nivel"])][0]
            hecho = " 🏅" if e["id"] in leer_pasaporte() else ""
            print(f"      {n} {e['num']:5} {e['titulo']}{hecho}")
    print("\nEmpieza con:  python3 taller.py empezar <ejercicio>   (por ejemplo: python3 taller.py empezar ej01)")
    pasaporte()


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        plaza()
    elif a[0] in ("-h", "--help", "ayuda"):
        print(__doc__)
    elif a[0] == "pasaporte":
        pasaporte()
    elif a[0] == "ejecutar" and len(a) > 2:
        sys.exit(ejecutar(buscar(a[1]), a[2], a[3:]))
    elif a[0] in ("empezar", "lanzar", "abrir", "comprobar") and len(a) > 1:
        ej = buscar(a[1])
        if a[0] == "lanzar":
            prompt = a[a.index("--prompt") + 1] if "--prompt" in a else None
            sys.exit(lanzar(ej, prompt))
        sys.exit({"empezar": lambda x: (empezar(x), 0)[1], "abrir": abrir, "comprobar": comprobar}[a[0]](ej))
    else:
        print(__doc__)
