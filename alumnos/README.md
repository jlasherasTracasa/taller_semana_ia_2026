# 🧰 Kit del taller · Agentes de IA

**Más allá de ChatGPT: crea y conecta agentes de IA** · Semana de la IA 2026 · UPNA · viernes 23 de octubre

> 🌐 Todo esto, más cómodo, en la web: **https://jlasherastracasa.github.io/taller_semana_ia_2026/**
> (ejercicios con el encargo listo para copiar, tu itinerario y la wiki).

## 🚀 Puesta en marcha

```bash
npm i -g opencode-ai                                    # el agente (validado con la 2.0.19)
python3 -m venv .venv && . .venv/bin/activate           # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt                         # las bibliotecas de los ejercicios
cp .env.example .env                                    # y escribe la clave que te damos en clase
bash comprobar_entorno.sh                               # 6 comprobaciones, incluida una llamada al modelo
```

¿Problemas? [Wiki → Primeros pasos](../wiki/Primeros-pasos.md), [Variables de entorno](../wiki/Variables-de-entorno.md)
y [Problemas y soluciones](../wiki/Problemas.md).

## ▶️ Cómo se trabaja

```bash
python3 taller.py                      # perfiles, áreas, ejercicios y tu progreso
python3 taller.py empezar ej25         # prepara ~/taller-agentes/ej25_… y te explica la situación
python3 taller.py lanzar ej25          # el agente hace el encargo (y te dice los tokens que ha gastado)
python3 taller.py comprobar ej25       # ¿lo hizo de verdad? Si sí, queda completado y te propone el siguiente paso
python3 taller.py lanzar ej25 --prompt "tu versión mejorada del encargo"
python3 taller.py abrir ej21           # opencode en modo interactivo, para conversar y aprobar permisos
python3 taller.py ejecutar f0 react_min.py   # los ejercicios que son programas de Python
python3 taller.py progreso             # ejercicios completados y nivel alcanzado
```

`taller.py` trabaja **siempre en copias** (`~/taller-agentes/`), lee tu `.env` y lanza opencode en modo
`--standalone`. Puedes hacerlo todo a mano: cada `ENUNCIADO.md` trae la orden de `opencode` equivalente.

## 📦 Qué hay

| Fichero o carpeta | Qué es |
|---|---|
| [`ITINERARIOS.md`](ITINERARIOS.md) | Perfiles, áreas, mapa de ejercicios y niveles. **Empieza aquí.** |
| `ejercicios/<id>/` | Un ejercicio: `ENUNCIADO.md` (situación, encargo, criterio, siguiente paso) y sus datos |
| [`soluciones/`](soluciones/README.md) | Lo que hizo el agente en la validación: encargo, salida real y ficheros |
| `taller.py` | El mando del taller (solo biblioteca estándar; funciona en Windows) |
| `comprobar.py` | El comprobador de cada ejercicio: `python3 comprobar.py --lista` |
| `opencode.json` | Configuración del agente: modelo y **permisos**. Sin claves ([wiki](../wiki/opencode-json.md)) |
| `.env.example` | Plantilla para tu clave (cópiala a `.env`, que nunca se sube a git) |
| `requirements.txt` | Bibliotecas de Python de los ejercicios |
| `comprobar_entorno.sh` | Comprueba que tu portátil está listo |
| [`replicar_paper/`](replicar_paper/README.md) | Reto avanzado: replicar un artículo científico en CPU |

## 🛡️ Reglas de oro

1. La clave, en `.env` o en variables de entorno; nunca en un fichero que se comparta.
2. Lo que el agente lee (correos, webs, documentos) es un **dato**, nunca una **orden**.
3. Trabaja en copias, con los permisos del kit: lo irreversible prohibido, lo que sale de tu máquina con permiso.
4. «He terminado» no es una prueba: pasa el comprobador.
5. Tú encargas y revisas; el agente ejecuta. Firma quien encarga.
