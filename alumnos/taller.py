#!/usr/bin/env python3
"""El mando del taller. Solo usa la biblioteca estándar: funciona igual en Windows, macOS y Linux.

  python taller.py                      perfiles, áreas, ejercicios y tu progreso
  python taller.py entorno              comprueba que tu ordenador está listo (y que el modelo responde)
  python taller.py empezar ej01         prepara la carpeta de trabajo y te explica la situación
  python taller.py empezar ej01 --de-cero    borra tu carpeta de trabajo de ese ejercicio y la prepara otra vez
  python taller.py abrir ej01           abre opencode en MODO INTERACTIVO en esa carpeta: pega ahí el encargo
  python taller.py comprobar ej01       pasa el comprobador; si todo está bien, marca el ejercicio como completado
  python taller.py lanzar ej01          (alternativa) el encargo de una vez, sin conversar (guarda salida.txt)
  python taller.py lanzar ej01 --prompt "tu propio encargo"
  python taller.py abrir ej01 --modelo glm-5.3-flash-free     otro modelo gratuito (si el de siempre se agota)
  python taller.py ejecutar f0 react_min.py [args]   ejecuta un script del ejercicio con tu .env cargado
  python taller.py progreso             ejercicios completados y nivel alcanzado
  python taller.py carpeta ej10 [sub]   dónde está tu carpeta de trabajo, qué hay dentro, y la abre en el explorador

Modelo: sin clave, uno GRATUITO de opencode; con OPENROUTER_API_KEY en .env, GLM-5.3-Flash en OpenRouter.
F.0 y F.1 (programas en Python) necesitan clave: OPENROUTER_API_KEY, o una gratuita de Groq (GROQ_API_KEY, recomendada) o Gemini (GEMINI_API_KEY).
Para elegir otro: variable TALLER_MODELO (por ejemplo, TALLER_MODELO=opencode/glm-5.3-flash-free).
Las carpetas de trabajo van a ~/taller-agentes/ (cámbialo con la variable TALLER_TRABAJO).
Las claves se leen del fichero .env de este kit; nunca se copian a las carpetas de trabajo.
"""
import json, os, re, shutil, subprocess, sys, time

KIT = os.path.dirname(os.path.abspath(__file__))
TRABAJO = os.path.expanduser(os.environ.get("TALLER_TRABAJO", "~/taller-agentes"))
INDICE = json.load(open(os.path.join(KIT, "ejercicios", "indice.json"), encoding="utf-8"))
EJS = {e["id"]: e for e in INDICE["ejercicios"]}
PROGRESO = os.path.join(TRABAJO, "progreso.json")
WIN = os.name == "nt"
PY = "python" if WIN else "python3"   # cómo se escribe en las órdenes que se muestran
GRATIS = "opencode/big-pickle"       # modelo gratuito de opencode por defecto (validado el 11-10-2026)
# Los gratuitos tienen un límite de uso POR MODELO: si uno lo agota, lanzar prueba el siguiente
# Lista actual: https://opencode.ai/zen/v1/models (22-10-2026). El cupo es por modelo: si uno se agota, otro sigue
GRATIS_OTROS = ["opencode/beam-free", "opencode/flint-40b-free", "opencode/glm-5.3-flash-free",
                "opencode/deepseek-v4.1-flash-free", "opencode/mimo-v2.6-flash-free", "opencode/nemotron-3.5-super-vl-free"]
OPENROUTER = "openrouter/z-ai/glm-5.3-flash"
# Lo que dice opencode cuando un modelo gratuito agota su límite de uso (1.x y 2.x)
LIMITE = ("Rate limit exceeded", "Free usage limit reached")
VENV_BIN = os.path.join(KIT, ".venv", "Scripts" if WIN else "bin")

if WIN:   # que los emojis no rompan la consola de Windows
    for flujo in (sys.stdout, sys.stderr):
        try:
            flujo.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass


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
    if os.path.isdir(VENV_BIN):   # el agente usa el Python del kit, con todas las bibliotecas, aunque no lo actives
        env["PATH"] = VENV_BIN + os.pathsep + env.get("PATH", "")
        env["VIRTUAL_ENV"] = os.path.dirname(VENV_BIN)
    return env


def modelo(env):
    """Qué modelo usa el agente: TALLER_MODELO si lo defines; si no, LiteLLM (docente), OpenRouter o el gratuito."""
    if env.get("TALLER_MODELO"):
        return env["TALLER_MODELO"]
    if env.get("LITELLM_API_KEY") and env.get("LITELLM_API_BASE"):
        return None   # el del opencode.json del kit (LiteLLM del docente)
    if env.get("OPENROUTER_API_KEY"):
        return env.get("TALLER_MODELO_OPENROUTER", OPENROUTER)
    return GRATIS


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
    sys.exit(f"No encuentro el ejercicio «{clave}». Mira la lista con:  {PY} taller.py")


def carpeta(ej):
    if os.path.commonpath([os.path.realpath(TRABAJO), KIT]) == KIT:
        sys.exit("La carpeta de trabajo no puede estar dentro del kit: el agente podría tocar enunciados y soluciones.")
    return os.path.join(TRABAJO, ej)


def config_opencode(ej, destino, env):
    """opencode.json del kit + el bloque mcp propio del ejercicio, si lo trae. Elige proveedor según las claves."""
    cfg = json.load(open(os.path.join(KIT, "opencode.json"), encoding="utf-8"))
    propio = os.path.join(KIT, "ejercicios", ej, "opencode.json")
    if os.path.exists(propio):
        for k, v in json.load(open(propio, encoding="utf-8")).items():
            if k != "permission":
                cfg[k] = v
    if modelo(env):
        cfg["model"] = modelo(env)
    json.dump(cfg, open(os.path.join(destino, "opencode.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)


def empezar(ej, silencioso=False, de_cero=False):
    e, d, env = EJS[ej], carpeta(ej), cargar_env()
    if de_cero and os.path.isdir(d):
        shutil.rmtree(d)   # carpeta() ya garantiza que está en ~/taller-agentes y no dentro del kit
        print(f"🧹 Borrada tu carpeta de trabajo de {e['num']}: empiezas de cero.")
    if os.path.exists(d):
        if not silencioso:
            print(f"La carpeta {d} ya existe: la dejo como está. Para empezar de cero:  "
                  f"{PY} taller.py empezar {e['num_corto']} --de-cero")
    else:
        shutil.copytree(os.path.join(KIT, "ejercicios", ej), d)
        config_opencode(ej, d, env)
    if not silencioso:
        n = INDICE["niveles"][str(e["nivel"])]
        print(f"\n{e['puerta_icono']} {e['num']} · {e['titulo']}   {n[0]} {n[1]} · ⏱ {e['min']} min\n")
        print(f"📌 {e['escena']}\n")
        print(f"📁 Tu carpeta: {d}")
        if e.get("demo"):
            print("🎥 Este ejercicio lo hace el profesor EN DIRECTO. Míralo en el proyector y repítelo después si quieres.")
        if e.get("prompt") and e["modo"] == "run":
            print(f"\n💬 El encargo (cópialo):\n   {e['prompt']}\n")
            print(f"▶️  1. Abre opencode en tu carpeta:  {PY} taller.py abrir {e['num_corto']}")
            print("    2. Pega el encargo, pulsa Enter y mira lo que hace. Cuando acabe, sal con Ctrl+C.")
            print(f"    (Sin conversar, de una vez:  {PY} taller.py lanzar {e['num_corto']})")
        else:
            print(f"\n📄 Este ejercicio tiene pasos propios: léelos en {os.path.join(d, 'ENUNCIADO.md')}")
            if e["modo"] == "interactivo":
                print(f"▶️  Abre opencode ahí:  {PY} taller.py abrir {e['num_corto']}")
        print(f"✅ Y luego:   {PY} taller.py comprobar {e['num_corto']}\n")
    return d


def opencode(args, d, env, salida=None):
    # opencode decide en qué carpeta trabaja mirando la variable PWD, no el directorio real del proceso:
    # sin esta línea, el agente escribiría en la carpeta desde la que lanzaste taller.py.
    env = dict(env, PWD=d)
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


def es(n, dec=0):
    """Número en formato español: 62.677 · 0,0107"""
    t = f"{n:,.{dec}f}"
    return t.replace(",", "·").replace(".", ",").replace("·", ".")


def coste(entrada, salida):
    return (entrada * PRECIO["entrada"] + salida * PRECIO["salida"]) / 1e6


def tokens(d, env):
    """Tokens gastados en la carpeta d según las estadísticas de opencode."""
    try:
        r = subprocess.run(["opencode", "stats", "--standalone", "--json", "--all", "--project", "."], cwd=d, env=dict(env, PWD=d),
                           stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=120, shell=WIN)
        t = json.loads(r.stdout)["tokens"]
        return {"entrada": t["input"] + t["cache"]["read"], "salida": t["output"] + t.get("reasoning", 0)}
    except Exception:
        return {"entrada": 0, "salida": 0}


def nombre_modelo(m):
    """'glm-5.3-flash-free' → 'opencode/glm-5.3-flash-free'; con proveedor, tal cual."""
    return m if not m or "/" in m else "opencode/" + m


def lanzar(ej, prompt=None, mod_forzado=None):
    e, env = EJS[ej], cargar_env()
    d = empezar(ej, silencioso=True)
    prompt = prompt or e.get("prompt")
    if not prompt:
        sys.exit("Este ejercicio no se lanza con un único encargo: sigue los pasos de su ENUNCIADO.md.")
    mod = nombre_modelo(mod_forzado) or modelo(env)
    extra = ["-m", mod] if mod_forzado else []
    print(f"🤖 Modelo: {mod or 'el del opencode.json del kit'}\n🤖 Encargo: {prompt}\n")
    t0 = time.time()
    otros = [m for m in [GRATIS] + GRATIS_OTROS if m != mod]
    for intento in range(6):
        rc = opencode(["run", "--standalone"] + extra + [prompt], d, env, salida=os.path.join(d, "salida.txt"))
        texto = open(os.path.join(d, "salida.txt"), encoding="utf-8").read()
        agotado = any(x in texto for x in LIMITE)
        if rc == 0 and not agotado:
            break
        if "exited before reporting readiness" in texto:
            # Si otro opencode arranca a la vez, el servidor privado a veces no llega a arrancar: se reintenta
            print("↻ opencode no ha llegado a arrancar; lo intento otra vez…")
            time.sleep(5 + 5 * intento)
        elif agotado and (mod or "").startswith("opencode/") and otros:
            mod = otros.pop(0)
            extra = ["-m", mod]
            print(f"↻ El modelo gratuito ha llegado a su límite de uso. Pruebo con otro: {mod}")
        else:
            break
    print(f"\n⏱ {time.time() - t0:.0f} s · código {rc} · salida guardada en salida.txt")
    t = tokens(d, env)
    if t["entrada"]:
        print(f"🪙 Tokens acumulados en esta carpeta: {es(t['entrada'])} de entrada y {es(t['salida'])} de salida "
              f"(≈ {es(coste(t['entrada'], t['salida']), 4)} $ si fuera GLM-5.3-Flash en OpenRouter)")
    print(f"✅ ¿Lo ha hecho de verdad?  {PY} taller.py comprobar {e['num_corto']}")
    return rc


def abrir(ej, mod_forzado=None):
    e, env = EJS[ej], cargar_env()
    d = empezar(ej, silencioso=True)
    # Con --modelo (o TALLER_MODELO) manda sobre el opencode.json de la carpeta, que se escribió al hacer «empezar»
    mod = nombre_modelo(mod_forzado or env.get("TALLER_MODELO"))
    print(f"Abriendo opencode en {d}\nModelo: {mod or modelo(env) or 'el del opencode.json del kit'} · sal con Ctrl+C")
    print(f"Si dice «Free usage limit reached» o «Rate limit exceeded»: dentro, /models y elige otro «Free»; "
          f"o sal y usa  {PY} taller.py abrir {e['num_corto']} --modelo {GRATIS_OTROS[0].split('/')[1]}  (o {GRATIS_OTROS[1].split('/')[1]}). "
          f"En clase, mejor la clave de clase (wiki: Clave de clase)")
    if e.get("prompt") and e["modo"] == "run":
        print(f"\n💬 Pega este encargo cuando se abra:\n   {e['prompt']}\n")
    time.sleep(1)
    if mod:   # el modo interactivo de opencode 2 no admite -m: el modelo va en el opencode.json de la carpeta
        ruta = os.path.join(d, "opencode.json")
        cfg = json.load(open(ruta, encoding="utf-8"))
        cfg["model"] = mod
        json.dump(cfg, open(ruta, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    rc = opencode(["--standalone"], d, env)   # sin --standalone usaría el servicio en segundo plano, que no ve tu .env
    print(f"\n✅ ¿Lo ha hecho de verdad?  {PY} taller.py comprobar {e['num_corto']}")
    return rc


def ejecutar(ej, script, args):
    d = empezar(ej, silencioso=True)
    env = dict(cargar_env(), TALLER_KIT=KIT, PWD=d)
    py = os.path.join(VENV_BIN, "python.exe" if WIN else "python")
    return subprocess.call([py if os.path.exists(py) else sys.executable, script] + args, cwd=d, env=env)


def entorno(sin_modelo=False):
    """Comprueba que el ordenador está listo. Funciona igual en Windows, macOS y Linux."""
    fallos = []

    def paso(bien, texto, arreglo=""):
        print(f"  {'✅' if bien else '❌'} {texto}" + ("" if bien or not arreglo else f"\n     → {arreglo}"))
        if not bien:
            fallos.append(texto)
        return bien

    def version(cmd):
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=60, shell=WIN, stdin=subprocess.DEVNULL)
            return (r.stdout + r.stderr).strip()
        except Exception:
            return ""

    env = cargar_env()
    print("\n== 1) Python 3.10 o superior ==")
    py = os.path.join(VENV_BIN, "python.exe" if WIN else "python")
    v = version([py if os.path.exists(py) else sys.executable, "--version"])
    paso(sys.version_info >= (3, 10), f"{v or sys.version.split()[0]}", "instala Python 3.12 (wiki: Instalar en Windows)")
    paso(os.path.exists(py), "entorno .venv del kit creado", f"{PY} -m venv .venv  (en la carpeta alumnos)")

    print("== 2) Bibliotecas de los ejercicios ==")
    mods = {"litellm": "litellm", "mcp": "mcp", "pptx": "python-pptx", "matplotlib": "matplotlib",
            "openpyxl": "openpyxl", "pdfplumber": "pdfplumber", "pypdf": "pypdf", "reportlab": "reportlab",
            "docx": "python-docx", "icalendar": "icalendar", "defusedxml": "defusedxml"}
    codigo = ("import importlib.util as u; print(' '.join(p for m, p in %r.items() if u.find_spec(m) is None))" % mods)
    faltan = version([py if os.path.exists(py) else sys.executable, "-c", codigo])
    paso(not faltan, "todas instaladas" if not faltan else f"faltan: {faltan}",
         ".venv\\Scripts\\python -m pip install -r requirements.txt" if WIN else ".venv/bin/python -m pip install -r requirements.txt")

    print("== 3) Node.js 18 o superior ==")
    v = version(["node", "--version"])
    m = re.match(r"v(\d+)", v)
    paso(bool(m) and int(m.group(1)) >= 18, f"node {v}" if m else "no encuentro node",
         "winget install OpenJS.NodeJS.LTS  y abre otra terminal (wiki: Instalar en Windows)")

    print("== 4) opencode 2.x ==")
    v = version(["opencode", "--version"])
    m = re.search(r"(\d+)\.(\d+)\.(\d+)", v)
    if paso(bool(m), f"opencode {m.group(0)}" if m else "no encuentro opencode", "npm i -g @opencode/cli@2.0.19"):
        if m.group(1) != "2":
            print("  ⚠️  el kit está validado con la 2.0.19:  npm i -g @opencode/cli@2.0.19")
    if WIN:
        bash = shutil.which("bash") or os.path.exists(r"C:\Program Files\Git\bin\bash.exe")
        print(f"  {'✅' if bash else '⚠️ '} Git Bash {'encontrado' if bash else 'no encontrado: instálalo con  winget install Git.Git  (opencode lo usa para sus órdenes)'}")

    print("== 5) Modelo ==")
    mod = modelo(env)
    if mod == GRATIS or (mod or "").startswith("opencode/"):
        print(f"  ✅ {mod}: gratuito de opencode, sin clave")
    elif mod and mod.startswith("openrouter/"):
        print(f"  ✅ {mod}: OpenRouter (clave definida; no se imprime)")
    else:
        print(f"  ✅ {mod or 'LiteLLM del docente (opencode.json del kit)'}")
    clave_py = next((k for k in ("LITELLM_API_KEY", "OPENROUTER_API_KEY", "GROQ_API_KEY", "GEMINI_API_KEY") if env.get(k)), None)
    if clave_py:
        print(f"  ✅ F.0 y F.1 (programas en Python) usarán {clave_py} (no se imprime)")
    else:
        print("  ℹ️  F.0 y F.1 (programas en Python) necesitan clave: OPENROUTER_API_KEY, o una GRATUITA y personal de Groq\n"
              "     (GROQ_API_KEY, wiki: Modelos). Los modelos gratuitos de opencode solo van dentro de opencode")

    print("== 6) Prueba real con el modelo ==")
    if sin_modelo or fallos:
        print("  ⚠️  omitida" + (": arregla antes lo que está en ❌" if fallos else ""))
    else:
        import tempfile
        d = tempfile.mkdtemp(prefix="taller_")
        config_opencode("ej01_pagina_personal", d, env)
        try:
            r = subprocess.run(["opencode", "run", "--standalone", "Responde exactamente: listo para el taller"], cwd=d,
                               env=dict(env, PWD=d), capture_output=True, text=True, encoding="utf-8", errors="replace",
                               timeout=180, shell=WIN, stdin=subprocess.DEVNULL)
            salida = r.stdout + r.stderr
        except subprocess.TimeoutExpired:
            salida = "no contesta en 3 minutos"
        shutil.rmtree(d, ignore_errors=True)
        paso("listo para el taller" in salida.lower(), "el modelo responde",
             salida.strip().splitlines()[-1][:150] if salida.strip() else "sin respuesta (wiki: Problemas)")

    print(f"\n== Resumen: {len(fallos)} cosa(s) por arreglar ==")
    print(f"🎉 Listo para el taller. Siguiente:  {PY} taller.py" if not fallos else
          "Arregla lo que está en ❌ (wiki: Instalar en Windows y Problemas). ¿No hay manera? Plan B en la wiki.")
    return len(fallos)


def leer_progreso():
    try:
        return json.load(open(PROGRESO, encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def comprobar(ej):
    e, d = EJS[ej], carpeta(ej)
    if not os.path.isdir(d):
        sys.exit(f"Aún no has empezado {e['num']}:  {PY} taller.py empezar {e['num_corto']}")
    if e["modo"] == "script":   # F.0, F.1, F.9 y el reto: programas que miras tú, sin comprobador automático
        print(f"{e['num']} no tiene comprobador automático: es un programa que miras tú.\n"
              f"Repasa la lista «✅ ¿Lo ha hecho de verdad?» de su enunciado: {os.path.join(d, 'ENUNCIADO.md')}")
        rc = 0
    elif subprocess.call([sys.executable, os.path.join(KIT, "comprobar.py"), ej, d]) == 0:
        rc = 0
        p = leer_progreso()
        p[ej] = time.strftime("%Y-%m-%d %H:%M")
        os.makedirs(TRABAJO, exist_ok=True)
        json.dump(p, open(PROGRESO, "w", encoding="utf-8"), indent=1)
        print(f"\n✅ Ejercicio completado: {e['num']} · {e['titulo']}")
    else:
        rc = 1
        print("\nTodavía no está. Vuelve a opencode y pídele que lo arregle, o mejora el encargo (más CONTEXTO,\n"
              f"ENTREGA, LÍMITES y CRITERIO) y repítelo:   {PY} taller.py abrir {e['num_corto']}")
    if e.get("siguiente"):
        print("\n🔀 Siguiente paso:")
        for texto, destino in e["siguiente"]:
            if destino == "PLAZA":
                print(f"   ↩️  {texto}:  {PY} taller.py")
            else:
                print(f"   ➡️  {texto}:  {PY} taller.py empezar {EJS[destino]['num_corto']}")
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


def progreso():
    p = leer_progreso()
    print(f"\n📈 Tu progreso · {len(p)} ejercicio(s) completado(s)\n")
    for clave, puerta in INDICE["puertas"].items():
        hechos = [EJS[i] for i in p if i in EJS and EJS[i]["puerta"] == clave]
        print(f"  {puerta['icono']} {puerta['nombre']:34} " + (" ".join(f"✅{s['num']}" for s in hechos) or "·"))
    f = final(p)
    if f is not None:
        ico, nombre, _, texto = INDICE["finales"][f]
        print(f"\n{ico} {nombre.upper()} alcanzado. {texto}")
    else:
        print("\nAún no tienes nivel: el básico pide 3 ejercicios y la prueba de seguridad (EJ 10).")


def ver_carpeta(ej, sub=""):
    """Dice la ruta completa de la carpeta de trabajo (o de una subcarpeta), lista lo que hay y la abre."""
    d = carpeta(ej)
    if not os.path.isdir(d):
        sys.exit(f"Aún no has empezado {EJS[ej]['num']}:  {PY} taller.py empezar {EJS[ej]['num_corto']}")
    ruta = os.path.normpath(os.path.join(d, sub)) if sub else d
    if not os.path.exists(ruta):
        print(f"📁 {d}\n❌ Ahí dentro todavía no existe «{sub}» (¿ha terminado el agente?). Lo que hay:")
        ruta = d
    else:
        print(f"📁 {ruta}")
    if os.path.isfile(ruta):
        print(open(ruta, encoding="utf-8", errors="replace").read())
        return 0
    for raiz, dirs, ficheros in os.walk(ruta):
        dirs[:] = sorted(x for x in dirs if not x.startswith("."))
        nivel = os.path.relpath(raiz, ruta).count(os.sep) + (0 if raiz == ruta else 1)
        if nivel > 2:
            continue
        if raiz != ruta:
            print("   " * (nivel - 1) + f"📂 {os.path.basename(raiz)}/")
        for f in sorted(ficheros):
            if not f.startswith("."):
                print("   " * nivel + f"   {f}")
    try:   # que se abra en el explorador de archivos, si hay pantalla (en Codespaces no la hay: basta con la lista)
        if WIN:
            os.startfile(ruta)
        elif sys.platform == "darwin":
            subprocess.Popen(["open", ruta])
        elif os.environ.get("DISPLAY") or os.environ.get("WAYLAND_DISPLAY"):
            subprocess.Popen(["xdg-open", ruta], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except OSError:
        pass
    print(f"\nPara leer un fichero:  {PY} taller.py carpeta {EJS[ej]['num_corto']} " + (sub.rstrip('/\\') + "/" if sub else "") + "<fichero>")
    return 0


def inicio():
    print(INDICE["prologo_corto"])
    print("Perfiles e itinerarios recomendados (puedes ir a cualquier ejercicio):\n")
    for p in INDICE["perfiles"].values():
        ruta = " → ".join(EJS[i]["num"] for i in p["ruta"] if i in EJS)
        print(f"  {p['icono']} {p['nombre']}: {p['quien']}\n     Itinerario: {ruta}\n")
    print("Áreas y ejercicios:\n")
    for clave, puerta in INDICE["puertas"].items():
        ejs = [e for e in INDICE["ejercicios"] if e["puerta"] == clave]
        print(f"  {puerta['icono']} {puerta['nombre']} · {puerta['tema']}")
        for e in ejs:
            n = INDICE["niveles"][str(e["nivel"])][0]
            hecho = " ✅" if e["id"] in leer_progreso() else ""
            demo = " 🎥" if e.get("demo") else ""
            print(f"      {n} {e['num']:5} {e['titulo']}{demo}{hecho}")
    print(f"\n🎥 = lo hace el profesor en directo · el resto los hacéis vosotros y le preguntáis las dudas.")
    print(f"Empieza con:  {PY} taller.py empezar <ejercicio>   (por ejemplo: {PY} taller.py empezar ej01)")
    progreso()


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        inicio()
    elif a[0] in ("-h", "--help", "ayuda"):
        print(__doc__)
    elif a[0] in ("progreso", "pasaporte"):
        progreso()
    elif a[0] == "entorno":
        sys.exit(entorno("--sin-modelo" in a))
    elif a[0] == "carpeta" and len(a) > 1:
        sys.exit(ver_carpeta(buscar(a[1]), a[2] if len(a) > 2 else ""))
    elif a[0] == "ejecutar" and len(a) > 2:
        sys.exit(ejecutar(buscar(a[1]), a[2], a[3:]))
    elif a[0] in ("empezar", "lanzar", "abrir", "comprobar") and len(a) > 1:
        ej = buscar(a[1])
        mod = a[a.index("--modelo") + 1] if "--modelo" in a and a.index("--modelo") + 1 < len(a) else None
        if a[0] == "lanzar":
            prompt = a[a.index("--prompt") + 1] if "--prompt" in a else None
            sys.exit(lanzar(ej, prompt, mod))
        if a[0] == "abrir":
            sys.exit(abrir(ej, mod))
        sys.exit({"empezar": lambda x: (empezar(x, de_cero="--de-cero" in a), 0)[1], "comprobar": comprobar}[a[0]](ej))
    else:
        print(__doc__)
