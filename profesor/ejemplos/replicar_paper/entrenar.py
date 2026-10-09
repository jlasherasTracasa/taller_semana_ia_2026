# -*- coding: utf-8 -*-
"""Paso 3 de la réplica: entrenamiento del bi-encoder en CPU con currículo y PAM.

Réplica reducida del entrenamiento del paper:
- Backbone: en el paper, MrBERT-es. SÍ está publicado en Hugging Face como
  BSC-LT/MrBERT-es (--base mrbert); por defecto seguimos usando
  paraphrase-multilingual-MiniLM-L12-v2 (118M parámetros, ligero para CPU).
- Currículo de 3 fases (el paper usa 6): F1 negativos aleatorios; F2 negativos difíciles
  "medios" (ventana de ranking lejana); F3 negativos difíciles "duros" (top del ranking),
  en ambas fases minados con PAM (Positive-Aware Mining): se descartan candidatos cuya
  similitud con la query supere sim(q,d+) - δ (falsos negativos), con δ=0.1 como el paper.
- Pérdida: MultipleNegativesRankingLoss (el paper usa su versión cacheada).

Salida: modelo afinado en data/modelo_afinado/ y negativos en data/negativos.json
"""
import argparse
import json
import os
import random
import time
from pathlib import Path

os.environ["CUDA_VISIBLE_DEVICES"] = ""  # FUERZA CPU

import torch
assert not torch.cuda.is_available(), "¡Hay GPU visible! La réplica debe correr en CPU"

SEED = 42
random.seed(SEED)
torch.manual_seed(SEED)

DIR = Path(__file__).parent
DATA = DIR / "data"
MODELOS = {
    # minilm: el backbone de la réplica original T11; mrbert: el backbone REAL del paper
    "minilm": "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    "mrbert": "BSC-LT/MrBERT-es",
}
HILOS_CPU = 8  # simula el portátil de un alumno (T11b)

from sentence_transformers import SentenceTransformer, InputExample, losses
DELTA_PAM = 0.1      # margen del paper: sim(q,d) < sim(q,d+) - delta
MAX_NEG = 2          # el paper usa 5; reducimos por presupuesto CPU
BATCH = 8
EPOCAS_FASE = 1
LIMITE_EPOCA_SEG = 1800  # si una época supera 30 min, reducimos pasos (documentado en el README)


def cargar_pares():
    pares = json.loads((DATA / "pares.json").read_text(encoding="utf-8"))
    pasajes = {p["id"]: p["texto"] for p in
               json.loads((DATA / "pasajes.json").read_text(encoding="utf-8"))}
    train = [p for p in pares if p["split"] == "train"]
    dev = [p for p in pares if p["split"] == "dev"]
    return train, dev, pasajes


def minar_negativos(model, train, pasajes):
    """Minería de negativos difíciles con PAM, réplica del protocolo del paper:
    ventana de ranking k∈[kmin,kmax] sobre pasajes ordenados por sim(q,d),
    descartando d con sim(q,d) >= sim(q,d+) - δ (falsos negativos)."""
    from sentence_transformers.util import cos_sim
    ids_train = list({p["pos_id"] for p in train})
    corpus_emb = model.encode([pasajes[i] for i in ids_train], batch_size=32,
                              convert_to_tensor=True, show_progress_bar=False)
    idx = {pid: i for i, pid in enumerate(ids_train)}
    q_embs = model.encode([p["q"] for p in train], batch_size=32,
                          convert_to_tensor=True, show_progress_bar=False)
    sims = cos_sim(q_embs, corpus_emb)

    negativos = {}
    for n, par in enumerate(train):
        orden = sims[n].argsort(descending=True).tolist()          # ranking desc por sim(q,d)
        sim_pos = float(sims[n][idx[par["pos_id"]]])
        rank_pos = orden.index(idx[par["pos_id"]])
        candidatos = []
        for r, ci in enumerate(orden):
            cid = ids_train[ci]
            if cid == par["pos_id"]:
                continue
            s = float(sims[n][ci])
            if s >= sim_pos - DELTA_PAM:   # PAM: fuera falsos negativos
                continue
            candidatos.append((r, cid, s))
        # Fase media: lejos del top (como kmin=10..kmax=50 del paper, escalado a corpus pequeño)
        medios = [c for c in candidatos if 5 <= c[0] < 20]
        # Fase dura: primeros del ranking admitido
        duros = [c for c in candidatos if c[0] < 5]
        random.shuffle(medios)
        negativos[par["pos_id"]] = {"medio": [m[1] for m in medios[:MAX_NEG]],
                                    "duro": [d[1] for d in duros[:MAX_NEG]]}
        if rank_pos < 3 and n % 50 == 0:
            print(f"[entrenar] aviso: positivo en rank {rank_pos} (par {n})")
    (DATA / "negativos.json").write_text(json.dumps(negativos), encoding="utf-8")
    return negativos


def ejemplos_fase(train, pasajes, negativos, tipo):
    ej = []
    pares_fallback = 0
    for par in train:
        pos = pasajes[par["pos_id"]]
        negs = negativos.get(par["pos_id"], {}).get(tipo, [])
        if tipo != "aleatorio" and len(negs) < 1:
            # Fallback (documentado en el README): con un backbone cero-shot sin
            # espacio de similitud fiable, PAM puede descartarlo todo (todo está
            # "demasiado cerca" del positivo). Para ese par se sustituyen los
            # negativos difíciles por aleatorios en vez de perder el ejemplo.
            pares_fallback += 1
            while len(negs) < MAX_NEG:
                cand = random.choice(train)["pos_id"]
                if cand != par["pos_id"] and cand not in negs:
                    negs.append(cand)
        if tipo == "aleatorio":
            while len(negs) < MAX_NEG:
                cand = random.choice(train)["pos_id"]
                if cand != par["pos_id"]:
                    negs.append(cand)
        ej.append(InputExample(texts=[par["q"], pos] + [pasajes[n] for n in negs[:MAX_NEG]]))
    random.shuffle(ej)
    if pares_fallback:
        print(f"[entrenar] aviso PAM: {pares_fallback}/{len(train)} pares sin negativos "
              f"admitidos en la fase '{tipo}' → fallback a aleatorios para esos pares")
    return ej


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", choices=list(MODELOS), default="minilm",
                        help="backbone a afinar: minilm (réplica T11) o mrbert (backbone real del paper)")
    args = parser.parse_args()

    torch.set_num_threads(HILOS_CPU)  # portátil de un alumno: 8 hilos
    t0 = time.time()
    base_model = MODELOS[args.base]
    dir_salida = DATA / ("modelo_afinado_mrbert" if args.base == "mrbert" else "modelo_afinado")

    train, dev, pasajes = cargar_pares()
    print(f"[entrenar] train={len(train)} dev={len(dev)} pasajes={len(pasajes)} "
          f"base={base_model} hilos={torch.get_num_threads()}")

    model = SentenceTransformer(base_model, device="cpu")

    negativos = minar_negativos(model, train, pasajes)
    print(f"[entrenar] minería PAM completada · {time.time()-t0:.1f}s")

    fases = [("F1 negativos aleatorios", "aleatorio", EPOCAS_FASE),
             ("F2 difíciles medios (PAM)", "medio", EPOCAS_FASE),
             ("F3 difíciles duros (PAM)", "duro", EPOCAS_FASE)]
    tiempos_fases = {}
    for nombre, tipo, epocas in fases:
        tf = time.time()
        ejemplos = ejemplos_fase(train, pasajes, negativos, tipo)
        loader = torch.utils.data.DataLoader(
            [e for e in ejemplos], batch_size=BATCH, shuffle=True,
            collate_fn=model.smart_batching_collate)
        perdida = losses.MultipleNegativesRankingLoss(model)
        model.fit(train_objectives=[(loader, perdida)],
                  epochs=epocas, warmup_steps=10, show_progress_bar=False,
                  optimizer_params={"lr": 2e-5})
        dur = time.time() - tf
        tiempos_fases[nombre] = round(dur, 1)
        if dur > LIMITE_EPOCA_SEG:
            print(f"[entrenar] AVISO: la época de '{nombre}' ha tardado {dur:.0f}s (>30 min). "
                  "Se corta el currículo aquí y se documenta la reducción (presupuesto CPU "
                  "del alumno agotado); el modelo queda guardado con las fases completadas.")
            break
        print(f"[entrenar] {nombre}: {len(ejemplos)} ejemplos · {dur:.1f}s")

    model.save(str(dir_salida))
    total = time.time() - t0
    (DATA / f"tiempos_entrenamiento{'_mrbert' if args.base == 'mrbert' else ''}.json").write_text(
        json.dumps({"base": base_model, "hilos_cpu": torch.get_num_threads(),
                    "fases_segundos": tiempos_fases, "total_segundos": round(total, 1)},
                   ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"[entrenar] modelo guardado en {dir_salida} · total {total:.1f}s")


if __name__ == "__main__":
    main()
