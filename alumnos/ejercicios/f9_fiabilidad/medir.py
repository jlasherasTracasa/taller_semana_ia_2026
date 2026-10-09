#!/usr/bin/env python3
"""¿Sale bien siempre? Repite un ejercicio N veces en carpetas limpias, pasa el comprobador y resume.

Uso (desde el kit):  python3 taller.py ejecutar f9 medir.py ej07 5 [--prompt "otro encargo"]
"""
import json, os, shutil, subprocess, sys, time

KIT = os.environ.get("TALLER_KIT") or sys.exit("Lánzalo con:  python3 taller.py ejecutar f9 medir.py ej07 5")
sys.path.insert(0, KIT)
import taller  # noqa: E402  (el mando del kit: sabe preparar carpetas y lanzar opencode)

ej = taller.buscar(sys.argv[1] if len(sys.argv) > 1 else "ej07")
n = int(sys.argv[2]) if len(sys.argv) > 2 else 3
prompt = sys.argv[sys.argv.index("--prompt") + 1] if "--prompt" in sys.argv else taller.EJS[ej]["prompt"]
env = taller.cargar_env()
base = os.path.join(os.getcwd(), "intentos", ej)
shutil.rmtree(base, ignore_errors=True)
filas = []
for i in range(1, n + 1):
    d = os.path.join(base, f"intento_{i}")
    shutil.copytree(os.path.join(KIT, "ejercicios", ej), d)
    taller.config_opencode(ej, d, env)
    t0 = time.time()
    with open(os.path.join(d, "salida.txt"), "w", encoding="utf-8") as f:
        subprocess.call(["opencode", "run", "--standalone", prompt], cwd=d, env=dict(env, PWD=d), stdin=subprocess.DEVNULL,
                        stdout=f, stderr=subprocess.STDOUT, shell=taller.WIN)
    seg = time.time() - t0
    ok = subprocess.call([sys.executable, os.path.join(KIT, "comprobar.py"), ej, d], stdout=subprocess.DEVNULL) == 0
    tok = taller.tokens(d, env)
    filas.append((i, ok, seg, tok))
    print(f"intento {i}: {'✅' if ok else '❌'}  {seg:5.0f} s  {tok['entrada']:>8,} tokens de entrada  {tok['salida']:>6,} de salida")

aciertos = sum(1 for f in filas if f[1])
p = aciertos / n
print(f"\n{ej}: {aciertos}/{n} aciertos (tasa {p:.0%}) · {sum(f[2] for f in filas) / n:.0f} s de media")
print(f"pass^{n} estimado (que salgan bien los {n} seguidos): {p ** n:.0%}")
ent = sum(f[3]["entrada"] for f in filas) / n
sal = sum(f[3]["salida"] for f in filas) / n
print(f"Tokens medios por intento: {ent:,.0f} de entrada y {sal:,.0f} de salida "
      f"≈ {taller.coste(ent, sal):.4f} $ en OpenRouter (GLM-5.3-Flash)")
json.dump([{"intento": i, "ok": o, "segundos": s, **t} for i, o, s, t in filas],
          open(os.path.join(base, "resultados.json"), "w"), indent=1)
