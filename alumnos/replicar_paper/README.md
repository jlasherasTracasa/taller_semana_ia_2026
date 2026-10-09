# Réplica a escala reducida: «Performant Lightweight Encoders for Spanish in the Legal and Administrative Domains»

Réplica didáctica (taller T11) del paper de Dueñas-Romero et al. (CEATIC, Univ. de Jaén / iniciativa ALIA),
ejecutada **íntegramente en CPU en ~3,5 minutos**, con **GLM-5.3-Flash por API** para los datos sintéticos.

## Qué replica

El pipeline completo del paper, a escala reducida y end-to-end:

1. **Corpus legal-administrativo público** → pasajes de 150-250 palabras (paper: fuentes BOE, BORME, ministerios…).
2. **Datos sintéticos** con un LLM: una consulta por pasaje, con caché en disco y split **por documento**
   (el paper genera pares query–pasaje inspirándose en Qwen3-Embedding).
3. **Entrenamiento contrastivo del bi-encoder** con currículo de dificultad creciente y minería de
   negativos difíciles con filtrado PAM *Positive-Aware Mining* (descartar falsos negativos:
   `sim(q,d) < sim(q,d+) − δ`, δ=0.1 como en el paper).
4. **Evaluación tipo MTEB** (retrieval): nDCG@10, MRR@10 y Recall@10 de BM25 frente al encoder base y al
   afinado, más un cross-encoder de reranking sobre el top-20.

## Qué se reduce y por qué

| Paper | Réplica | Motivo |
|---|---|---|
| MrBERT-es (backbone propio, ALIA/SINAI) | `paraphrase-multilingual-MiniLM-L12-v2` (118M par.) por defecto; **en T11b también `BSC-LT/MrBERT-es` con `entrenar.py --base mrbert`** (el backbone real SÍ está en Hugging Face) | MiniLM es pequeño y entrena en CPU; MrBERT-es se puede afinar igual (ver tabla T11b) |
| Corpus masivo multifuente (BOE, BORME, ministerios, CTE…) | 7 leyes consolidadas del BOE vía API oficial de datos abiertos (414 pasajes) | Presupuesto de tiempo CPU <30 min; solo fuentes públicas oficiales (los textos del BOE son de dominio público) |
| Varias consultas por pasaje (pipeline multietapa) | 1 consulta/pasaje, GLM-5.3-Flash vía LiteLLM, caché en disco | Coste de API acotado y ejecución reproducible |
| Currículo de 6 fases (2 macroetapas × easy/medium/hard) | 3 fases: aleatorios → difíciles medios → difíciles duros | Misma idea pedagógica en un tercio de fases |
| Minería PAM con FAISS, k∈[10,50], τ=0.8, δ=0.1, 5 negativos | Minería con el propio modelo, ventana de ranking escalada (duros: top-5; medios: 5-19), PAM δ=0.1, 2 negativos | Corpus pequeño; la lógica (filtrar falsos negativos por margen) es idéntica |
| Loss CachedMultipleNegativesRankingLoss | `MultipleNegativesRankingLoss` | Escala reducida no requiere caché |
| Evaluación MTEB completa + reranker ALIA-MrBERT-es | Retrieval test (120 consultas sobre 120 pasajes de leyes nunca vistas) + `bge-reranker-base` como cross-encoder sobre top-20 | CPU; cross-encoder multilingüe pequeño sustituye al reranker propio |
| Batch 256, Optuna | Batch 8, 1 época/fase, lr 2e-5, sin HPO | Tiempo CPU |

**Semillas fijas**: `SEED=42`, `PYTHONHASHSEED=42`. **CPU forzada**: `CUDA_VISIBLE_DEVICES=""` en todos
los scripts y `assert torch.cuda.is_available() == False` en entrenar/evaluar.

## Números reales (verificación con `FRESH=1 bash verificar.sh --reranker`)

Split: 253 train / 40 dev / **120 test** (leyes enteras reservadas: Contratos del Sector Público y Protección de Datos).

| Sistema | nDCG@10 | MRR@10 | Recall@10 |
|---|---|---|---|
| BM25 (rank_bm25) | **0,899** | **0,876** | **0,967** |
| Encoder base (MiniLM sin afinar) | 0,686 | 0,635 | 0,850 |
| **Encoder afinado** (currículo + PAM) | 0,750 | 0,694 | 0,925 |
| Reranker bge-reranker-base (top-20 del afinado) | 0,881 | 0,860 | 0,942 |

Lectura: el afinado mejora claramente al base (+6,3 puntos de nDCG@10), como en el paper; el cross-encoder
recupera casi todo el hueco frente a BM25 sobre este corpus pequeño. Con UN solo documento relevante por
consulta, el IDCG@10 es 1. Advertencia: corpus diminuto y consultas sintéticas de dificultad acotada; las
métricas absolutas NO son comparables con MTEB — solo valen las comparaciones entre sistemas.

### T11b — con los modelos publicados del paper (28-09-2026, CPU)

Sobre el MISMO test de 120 consultas y el mismo corpus:

| Sistema | nDCG@10 | MRR@10 | Recall@10 |
|---|---|---|---|
| BM25 (rank_bm25) | 0,899 | 0,876 | 0,967 |
| Encoder base (MiniLM sin afinar) | 0,686 | 0,635 | 0,850 |
| Encoder afinado (MiniLM + currículo/PAM) | 0,749 | 0,697 | 0,908 |
| **MrBERT-es afinado por nosotros** (`--base mrbert`, currículo+PAM) | 0,758 | 0,697 | 0,950 |
| **ALIA-MrBERT-es publicado, zero-shot** (bi-encoder de los autores) | 0,913 | 0,886 | 0,992 |
| Reranker bge-reranker-base (top-20 del afinado) | 0,889 | 0,868 | 0,950 |
| **ALIA-MrBERT-es reranker publicado, zero-shot** (sobre su propio top-20) | **0,969** | **0,958** | **1,000** |

Lectura: los modelos publicados por los autores ganan a TODO lo que montamos encima, incluido BM25 —
que era la línea base invicta de la T11 original. Nuestro afinado de MrBERT-es apenas roza lo que los
autores consiguieron con su pipeline completo de datos; el modelo publicado es la prueba de qué parte
del rendimiento venía de los datos y del entrenamiento a gran escala, no de la arquitectura.

### T11b — tiempos reales medidos (CPU, torch limitado a 8 hilos para simular un portátil de alumno)

| Paso | Tiempo |
|---|---|
| `entrenar.py --base mrbert` (minería PAM + 3 fases, 8 hilos) | **849 s (~14 min)**; por fase: F1 269 s · F2 266 s · F3 273 s (ninguna supera el límite de 30 min, no hubo que recortar) |
| `evaluar.py --reranker` completo (7 sistemas) | 167 s |

Nota del proceso: en la minería inicial (con MrBERT-es aún cero-shot) PAM descartó el 100 % de los
candidatos en las fases difíciles — todo le resultaba «demasiado cerca» del positivo —, así que esos
pares usaron negativos aleatorios como *fallback* (implementado y avisado en `entrenar.py`). Aun así la
loss cayó 1,72 → 0,43 → 0,20 y el afinado sí mejora al mismo backbone sin afinar.

### Tiempos medidos (CPU única, 192 hilos)

| Paso | Tiempo |
|---|---|
| datos.py (API BOE, 7 leyes, pausas de cortesía) | 16 s |
| sinteticos.py (412 consultas, 4 hilos, caché) | 2 s con servidor caliente / ~60 s en frío |
| entrenar.py (minería PAM + 3 fases MNRL) | 68 s (loss por fase: 0,72 → 0,12 → 0,06) |
| evaluar.py --reranker | 106 s |
| **Total pipeline** | **≈ 3,5 min** (sin contar descarga de modelos la primera vez) |

## Qué replicamos y qué no (T11b)

**Replicado de verdad, sobre el mismo test:**

- El backbone del paper (`BSC-LT/MrBERT-es`), descargado de Hugging Face y afinado por nosotros con
  `entrenar.py --base mrbert`: mismo currículo de 3 fases y misma minería PAM (δ=0.1) que la T11.
- Los dos modelos PUBLICADOS por los autores evaluados zero-shot en nuestro test: el bi-encoder
  (`SINAI/ALIA-MrBERT-es-legal-administrative-embeddings`) y el reranker
  (`SINAI/ALIA-MrBERT-es-legal-administrative-reranker`, top-20, rescoreando su propio ranking).
- Ejecución íntegramente en CPU, con 8 hilos para imitar el portátil de un alumno y tiempos medidos de verdad.

**Lo que NO replicamos (y por qué):**

- **La escala de datos del paper.** Afina sobre 253 pares sintéticos nuestros; los autores entrenaron con
  un corpus legal-administrativo masivo. Por eso nuestro MrBERT-es afinado (0,758 nDCG@10) queda lejos del
  publicado zero-shot (0,913): la diferencia mide sus datos y su pipeline, no la arquitectura.
- **El currículo de 6 fases y el entrenamiento a gran escala** (batch 256, Optuna, loss cacheada): mantuvimos
  la versión reducida de 3 fases y batch 8. Además, en nuestro corpus diminuto PAM solo tuvo margen para
  minar negativos difíciles con MiniLM; con MrBERT-es cero-shot recurrió al fallback documentado.
- **Una comparación justa con MTEB**: sigue siendo un test casero de 120 consultas; solo valen las
  comparaciones internas.

**Aprendizaje clave para los alumnos:** cuando exista el modelo publicado, evalúalo zero-shot ANTES de
entrenar nada — es tu techo realista y te dice cuánto puede aportarte afinar. Y ninguna métrica sustituye
a comparar contra una línea base sencilla (BM25): aquí, lo que BM25 «ganaba» a los encoders pequeños era
en realidad hueco que solo cubren modelos bien entrenados a escala.

## Ficheros

- `datos.py` — descarga y trocea pasajes del BOE → `data/pasajes.json`
- `sinteticos.py` — consultas con GLM-5.3-Flash (LiteLLM, `.env`), caché `data/cache_consultas.json`, split por documento → `data/pares.json`
- `entrenar.py` — currículo 3 fases + minería PAM → `data/modelo_afinado/` (o `--base mrbert` → `data/modelo_afinado_mrbert/`)
- `evaluar.py` — métricas de los sistemas (T11b: 7 con `--reranker`, incluidos los publicados ALIA) → `data/resultados.json`
- `verificar.sh` — pipeline completo de cero + comprobaciones (`--reranker` para incluir el cross-encoder; `FRESH=1` para borrar también la caché de consultas)
- `data/` — artefactos generados y resultados

## Cómo encargársela a opencode (prompt exacto)

Desde esta carpeta (`replicar_paper/`), con el `.env` del kit en la carpeta padre o en esta:

```text
Lee README.md y replica el ejercicio: fuerza CPU (CUDA_VISIBLE_DEVICES="") y
comprueba que torch.cuda.is_available() sea False antes de entrenar. Ejecuta en
orden datos.py, sinteticos.py (necesita LITELLM_API_BASE y LITELLM_API_KEY del
.env, no los imprimas), entrenar.py y evaluar.py --reranker. Con resultados.json
genera data/resultados.csv y una tabla resumen comparada con la sección «Números»
del README, sin tocar las cifras publicadas. Termina con bash verificar.sh
--reranker y confirma que acaba con «réplica verificada con éxito». No instales
nada salvo que falte un paquete de requirements.txt.
```

El paper original está en esta carpeta: `paper_encoders_legales_es.pdf`. Pídele también al agente que
compare su tabla con la del paper y explique **por qué** difieren (escala de datos, modelo, consultas).

## Notas para los alumnos

- Modelos en Hugging Face: la primera ejecución descarga MiniLM (~470 MB) y bge-reranker-base (~1,1 GB)
  a vuestra caché por defecto (`~/.cache/huggingface`); no defináis HF_HOME.
- Instalación: `python3 -m venv .venv && . .venv/bin/activate`, después
  `pip install torch --index-url https://download.pytorch.org/whl/cpu` y `pip install -r requirements.txt`.
- La API del BOE solo sirve en consolidado las normas en vigor; algunos identificadores antiguos dan 404.

---
## Revisión (28-09-2026)

- **Comprobado:**
  - La CPU se fuerza en los tres scripts, con `assert not torch.cuda.is_available()`.
  - Los datos proceden de la API oficial del BOE.
  - Los resultados están en `data/resultados.json`.
- **Error corregido:** la afirmación «MrBERT-es no está en Hugging Face» es **falsa**. Existen `BSC-LT/MrBERT-es`, la
  base del paper, y los modelos publicados por los autores: `SINAI/ALIA-MrBERT-es-legal-administrative-embeddings` y
  su reranker, de unos 600 MB cada uno y viables en CPU. La versión con esos modelos está en T11b.
- **Lectura del resultado:** BM25 (0,899) supera al encoder pequeño afinado (0,750) en este corpus de 120 pasajes. Es
  una buena lección para el taller: comparar siempre con una línea base sencilla.
