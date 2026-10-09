# -*- coding: utf-8 -*-
"""Paso 4 de la réplica: evaluación tipo MTEB reducida (retrieval en test).

Métricas sobre el split test (leyes nunca vistas durante el entrenamiento):
nDCG@10, MRR@10 y Recall@10 para estos sistemas:
  1. BM25 léxico (rank_bm25)
  2. Bi-encoder base (paraphrase-multilingual-MiniLM-L12-v2)
  3. Bi-encoder afinado (data/modelo_afinado)
  4. [T11b] Bi-encoder MrBERT-es afinado por nosotros (data/modelo_afinado_mrbert)
  5. [T11b] Bi-encoder PUBLICADO por los autores, zero-shot
     (SINAI/ALIA-MrBERT-es-legal-administrative-embeddings)
Y, opcionalmente (--reranker), cross-encoders rescoreando el top-20:
  6. bge-reranker-base multilingüe, sobre el top-20 del afinado MiniLM
  7. [T11b] Reranker PUBLICADO por los autores, zero-shot
     (SINAI/ALIA-MrBERT-es-legal-administrative-reranker), sobre su propio top-20

Salida: data/resultados.json y data/tiempos.json
"""
import argparse
import json
import math
import os
import time
from pathlib import Path

os.environ["CUDA_VISIBLE_DEVICES"] = ""  # FUERZA CPU

import torch
assert not torch.cuda.is_available(), "¡Hay GPU visible! La réplica debe correr en CPU"

DIR = Path(__file__).parent
DATA = DIR / "data"
K = 10
TOP_RERANK = 20
ALIA_BIENCODER = "SINAI/ALIA-MrBERT-es-legal-administrative-embeddings"
ALIA_RERANKER = "SINAI/ALIA-MrBERT-es-legal-administrative-reranker"


def dcg(rels):
    return sum(rel / math.log2(i + 2) for i, rel in enumerate(rels))


def metricas(ranking_ids, positivo):
    """ranking_ids: ids ordenados; devuelve (nDCG@10, MRR@10, Recall@10).
    Con un único documento relevante por consulta, el IDCG@10 es 1.0
    (el relevante en la posición 1), como en los benchmarks de retrieval."""
    top = ranking_ids[:K]
    rels = [1.0 if pid == positivo else 0.0 for pid in top]
    n = dcg(rels) / 1.0
    mrr = next((1.0 / (i + 1) for i, pid in enumerate(top) if pid == positivo), 0.0)
    rec = 1.0 if positivo in top else 0.0
    return n, mrr, rec


def evaluar_sistema(nombre, rank_fn, test, pasajes):
    t0 = time.time()
    nd = mr = rc = 0.0
    for par in test:
        ranking = rank_fn(par["q"], pasajes)
        n, m, r = metricas(ranking, par["pos_id"])
        nd += n
        mr += m
        rc += r
    total = len(test)
    res = {"nDCG@10": round(nd / total, 4), "MRR@10": round(mr / total, 4),
           "Recall@10": round(rc / total, 4)}
    print(f"[evaluar] {nombre}: {res} · {time.time()-t0:.1f}s")
    return res, time.time() - t0


def metricas_de_rankings(test, rankings):
    res = {"nDCG@10": 0.0, "MRR@10": 0.0, "Recall@10": 0.0}
    for par, ranking in zip(test, rankings):
        n, m, r = metricas(ranking, par["pos_id"])
        res["nDCG@10"] += n / len(test)
        res["MRR@10"] += m / len(test)
        res["Recall@10"] += r / len(test)
    return {k: round(v, 4) for k, v in res.items()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reranker", action="store_true",
                        help="añade cross-encoder bge-reranker-base sobre top-20")
    args = parser.parse_args()

    t0 = time.time()
    pares = json.loads((DATA / "pares.json").read_text(encoding="utf-8"))
    pasajes_list = json.loads((DATA / "pasajes.json").read_text(encoding="utf-8"))
    test = [p for p in pares if p["split"] == "test"]
    corpus = [p for p in pasajes_list if p["doc"] in {t["doc"] for t in test}]
    pasajes = {p["id"]: p["texto"] for p in corpus}
    ids = list(pasajes.keys())
    textos = [pasajes[i] for i in ids]
    print(f"[evaluar] {len(test)} consultas de test · corpus de {len(textos)} pasajes")

    resultados, tiempos = {}, {}

    # --- 1. BM25 ---
    from rank_bm25 import BM25Okapi
    import re as _re

    def tokeniza(s):
        return _re.findall(r"[a-záéíóúüñ]+", s.lower())

    bm25 = BM25Okapi([tokeniza(t) for t in textos])

    def rank_bm25_(q, _):
        scores = bm25.get_scores(tokeniza(q))
        return [ids[i] for i in sorted(range(len(ids)), key=lambda i: -scores[i])]

    resultados["BM25"], tiempos["BM25"] = evaluar_sistema("BM25", rank_bm25_, test, pasajes)

    # --- 2, 3, 4 y 5. Bi-encoders ---
    from sentence_transformers import SentenceTransformer, util

    def evaluar_biencoder(nombre, fuente):
        t0 = time.time()
        modelo = SentenceTransformer(fuente, device="cpu")
        emb_corpus = modelo.encode(textos, batch_size=32, convert_to_tensor=True,
                                   show_progress_bar=False)
        q_embs = modelo.encode([t["q"] for t in test], batch_size=32,
                               convert_to_tensor=True, show_progress_bar=False)
        sims = util.cos_sim(q_embs, emb_corpus)
        rankings = [[ids[i] for i in fila.argsort(descending=True).tolist()] for fila in sims]
        res = metricas_de_rankings(test, rankings)
        print(f"[evaluar] {nombre}: {res} · {time.time()-t0:.1f}s")
        resultados[nombre] = res
        tiempos[nombre] = round(time.time() - t0, 1)
        return rankings

    rank_base = evaluar_biencoder("Encoder base",
                                  "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    rank_af = evaluar_biencoder("Encoder afinado", str(DATA / "modelo_afinado"))
    if (DATA / "modelo_afinado_mrbert").exists():
        evaluar_biencoder("MrBERT-es afinado por nosotros", str(DATA / "modelo_afinado_mrbert"))
    else:
        print("[evaluar] AVISO: no existe data/modelo_afinado_mrbert; "
              "ejecuta antes «entrenar.py --base mrbert» para incluirlo.")
    # Modelo PUBLICADO por los autores del paper, sin afinar nada por nuestra parte
    rank_alia = evaluar_biencoder("ALIA-MrBERT-es publicado (zero-shot)", ALIA_BIENCODER)

    # --- 6 y 7. Rerankers opcionales (cross-encoders sobre top-20) ---
    if args.reranker:
        from sentence_transformers import CrossEncoder

        def evaluar_reranker(nombre, fuente, rankings_biencoder):
            t0 = time.time()
            rr = CrossEncoder(fuente, device="cpu",
                              automodel_args={"torch_dtype": "float32"})
            res = {"nDCG@10": 0.0, "MRR@10": 0.0, "Recall@10": 0.0}
            for par, ranking in zip(test, rankings_biencoder):
                top20 = ranking[:TOP_RERANK]
                pares_in = [(par["q"], pasajes[c]) for c in top20]
                scores = rr.predict(pares_in, batch_size=8, show_progress_bar=False)
                reorden = [top20[i] for i in sorted(range(len(top20)),
                                                    key=lambda i: -scores[i])]
                resto = ranking[TOP_RERANK:]
                n, m, r = metricas(reorden + resto, par["pos_id"])
                res["nDCG@10"] += n / len(test)
                res["MRR@10"] += m / len(test)
                res["Recall@10"] += r / len(test)
            res = {k: round(v, 4) for k, v in res.items()}
            print(f"[evaluar] {nombre}: {res} · {time.time()-t0:.1f}s")
            resultados[nombre] = res
            tiempos[nombre] = round(time.time() - t0, 1)

        # bge-reranker-base: sustituto multilingüe genérico usado en la T11 original
        evaluar_reranker("Reranker afinado", "BAAI/bge-reranker-base", rank_af)
        # Reranker PUBLICADO por los autores, zero-shot, sobre SU PROPIO top-20
        evaluar_reranker("ALIA-MrBERT-es reranker publicado (zero-shot)",
                         ALIA_RERANKER, rank_alia)

    (DATA / "resultados.json").write_text(
        json.dumps({"metricas": resultados,
                    "n_consultas_test": len(test),
                    "tamano_corpus": len(textos),
                    "tiempos_segundos": tiempos},
                   ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"[evaluar] resultados.json guardado · total {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
