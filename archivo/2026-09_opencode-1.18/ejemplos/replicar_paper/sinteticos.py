# -*- coding: utf-8 -*-
"""Paso 2 de la réplica: consultas sintéticas con GLM-5.3-Flash (LiteLLM).

Réplica reducida del pipeline de generación sintética del paper (inspirado en
Qwen3-Embedding): para cada pasaje se genera UNA consulta natural que alguien
buscaría y que el pasaje responde.

Requisitos: variables LITELLM_API_BASE y LITELLM_API_KEY en .env (no se imprimen).
Caché en disco (data/cache_consultas.json) para no gastar llamadas al repetir.
Split train/dev/test POR DOCUMENTO: dos leyes completas se reservan para test.

Salida: data/pares.json  [{q, pos_id, doc, split}]
"""
import hashlib
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import litellm

os.environ.setdefault("CUDA_VISIBLE_DEVICES", "")

SEED = 42
OUT_DIR = Path(__file__).parent / "data"
CACHE = OUT_DIR / "cache_consultas.json"

# Documentos reservados para TEST (evaluación sobre leyes nunca vistas).
TEST_DOCS = {"BOE-A-2017-12902", "BOE-A-2018-16673"}
DEV_DOCS = {"BOE-A-2011-9617"}

PROMPT = """Eres un generador de datos sintéticos para entrenar un buscador jurídico-administrativo en español.
Dado el siguiente fragmento de una ley española, escribe UNA consulta breve (máximo 20 palabras), en lenguaje natural,
como la escribiría un ciudadano o profesional al buscar esa información. La consulta debe poder responderse
completamente con este fragmento. No cites literalmente frases largas del texto. Responde SOLO con la consulta.

Fragmento ({titulo}):
{texto}

Consulta:"""


def cargar_cache():
    if CACHE.exists():
        return json.loads(CACHE.read_text(encoding="utf-8"))
    return {}


def generar_consulta(pasaje, cache):
    clave = hashlib.sha256(pasaje["texto"].encode()).hexdigest()[:16]
    if clave in cache:
        return clave, cache[clave]
    msgs = [{"role": "user",
             "content": PROMPT.format(titulo=pasaje["titulo"], texto=pasaje["texto"])}]
    for intento in range(4):
        try:
            r = litellm.completion(
                model="openai/GLM-5.3-Flash-no-thinking",
                api_base=os.environ["LITELLM_API_BASE"],
                api_key=os.environ["LITELLM_API_KEY"],
                messages=msgs,
                max_tokens=2000,  # el modelo razona antes de responder; sin esto no llega al contenido
                temperature=0.7,
                timeout=120,
            )
            contenido = (r.choices[0].message.content or "").strip()
            q = contenido.splitlines()[0].strip().strip('"') if contenido else ""
            if 10 <= len(q) <= 200:
                return clave, q
        except Exception as e:
            print(f"[sinteticos] reintento {intento+1}: {str(e)[:100]}", flush=True)
            time.sleep(3 * (intento + 1))
    return clave, None


def main():
    t0 = time.time()
    pasajes = json.loads((OUT_DIR / "pasajes.json").read_text(encoding="utf-8"))
    cache = cargar_cache()
    print(f"[sinteticos] {len(pasajes)} pasajes · caché previa: {len(cache)} consultas")

    tareas = [(p, p) for p in pasajes]
    nuevas = 0
    with ThreadPoolExecutor(max_workers=4) as ex:
        for clave, q in ex.map(lambda t: generar_consulta(t[0], cache), tareas):
            if q and clave not in cache:
                cache[clave] = q
                nuevas += 1

    # Guardar caché tras cada tanda completa
    CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=1), encoding="utf-8")

    pares, fallos = [], 0
    for p in pasajes:
        clave = hashlib.sha256(p["texto"].encode()).hexdigest()[:16]
        q = cache.get(clave)
        if not q:
            fallos += 1
            continue
        split = "test" if p["doc"] in TEST_DOCS else ("dev" if p["doc"] in DEV_DOCS else "train")
        pares.append({"q": q, "pos_id": p["id"], "doc": p["doc"], "split": split})

    with open(OUT_DIR / "pares.json", "w", encoding="utf-8") as f:
        json.dump(pares, f, ensure_ascii=False, indent=1)

    from collections import Counter
    print(f"[sinteticos] nuevas consultas: {nuevas} · sin consulta: {fallos}")
    print(f"[sinteticos] splits: {dict(Counter(p['split'] for p in pares))} · {time.time()-t0:.1f}s")


if __name__ == "__main__":
    if "LITELLM_API_BASE" not in os.environ:
        env = Path(__file__).resolve().parents[3] / ".env"
        if env.exists():
            for line in env.read_text().splitlines():
                if "=" in line and not line.strip().startswith("#"):
                    k, v = line.split("=", 1)
                    os.environ.setdefault(k.strip(), v.strip())
    sys.exit(main())
