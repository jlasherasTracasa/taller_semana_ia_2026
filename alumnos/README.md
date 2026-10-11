# 🧰 Kit del taller · Agentes de IA

**Más allá de ChatGPT: crea y conecta agentes de IA** · Semana de la IA 2026 · UPNA · viernes 23 de octubre

> 🌐 Todo esto, más cómodo, en la web: **https://jlasherastracasa.github.io/taller_semana_ia_2026/**
> (ejercicios con el encargo listo para copiar, tu itinerario y la wiki).

## 🚀 Puesta en marcha

> 🛠️ Necesitas **Python 3.10+**, **Node.js 18+** y **Git**. Paso a paso para Windows, Linux y Mac:
> [Wiki → Instalar](../wiki/Instalar.md). ¿No puedes instalar o no tienes portátil? [Wiki → Plan B](../wiki/Plan-B.md).

🪟 **Windows** (PowerShell), desde esta carpeta:

```powershell
npm i -g @opencode/cli@2.0.19          # el agente (validado con la 2.0.19)
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python taller.py entorno                 # 6 comprobaciones, incluida una llamada real al modelo
```

🐧 **Linux** · 🍎 **Mac**:

```bash
npm i -g @opencode/cli@2.0.19
python3 -m venv .venv && . .venv/bin/activate
python -m pip install -r requirements.txt
python taller.py entorno
```

**No hace falta clave**: sin `.env`, el agente usa un modelo gratuito de opencode. Si en clase os dan una clave de
OpenRouter, copia `.env.example` a `.env` y ponla ahí ([Wiki → Modelos](../wiki/Modelos.md)).

## ▶️ Cómo se trabaja

Con el entorno activado (verás `(.venv)`), las órdenes son iguales en todos los sistemas:

```bash
python taller.py                       # perfiles, áreas, ejercicios (🎥 = demo del profesor) y tu progreso
python taller.py empezar ej24          # prepara ~/taller-agentes/ej24_… y te explica la situación
python taller.py abrir ej24            # opencode en MODO INTERACTIVO: pega el encargo y míralo trabajar
python taller.py comprobar ej24        # ¿lo hizo de verdad? Si sí, queda completado y te propone el siguiente paso
python taller.py progreso              # ejercicios completados y nivel alcanzado
python taller.py lanzar ej24           # (alternativa) el encargo de una vez, sin conversar; dice los tokens gastados
python taller.py ejecutar f0 react_min.py   # los ejercicios que son programas de Python (necesitan OpenRouter)
```

`taller.py` trabaja **siempre en copias** (`~/taller-agentes/`), lee tu `.env`, elige el modelo y abre opencode en
modo `--standalone`. Cómo se usa opencode por dentro (teclas, permisos, comandos): [Wiki → Modo interactivo](../wiki/Modo-interactivo.md).

## 📦 Qué hay

| Fichero o carpeta | Qué es |
|---|---|
| [`ITINERARIOS.md`](ITINERARIOS.md) | Perfiles, áreas, mapa de ejercicios y niveles. **Empieza aquí.** |
| `ejercicios/<id>/` | Un ejercicio: `ENUNCIADO.md` (situación, encargo, criterio, siguiente paso) y sus datos |
| [`soluciones/`](soluciones/README.md) | Lo que hizo el agente en la validación: encargo, salida real y ficheros |
| `taller.py` | El mando del taller (solo biblioteca estándar; funciona igual en Windows, Linux y Mac) |
| `comprobar.py` | El comprobador de cada ejercicio: `python comprobar.py --lista` |
| `opencode.json` | Configuración del agente: modelo y **permisos**. Sin claves ([wiki](../wiki/opencode-json.md)) |
| `.env.example` | Plantilla para tu clave de OpenRouter, si la usas (cópiala a `.env`, que nunca se sube a git) |
| `requirements.txt` | Bibliotecas de Python de los ejercicios |
| `comprobar_entorno.sh` | Lo mismo que `python taller.py entorno`, para quien prefiera bash |
| [`replicar_paper/`](replicar_paper/README.md) | Reto avanzado: replicar un artículo científico en CPU |

## 🛡️ Reglas de oro

1. La clave, en `.env` o en variables de entorno; nunca en un fichero que se comparta.
2. Lo que el agente lee (correos, webs, documentos) es un **dato**, nunca una **orden**.
3. Trabaja en copias, con los permisos del kit: lo irreversible prohibido, lo que sale de tu máquina con permiso.
4. «He terminado» no es una prueba: pasa el comprobador.
5. Tú encargas y revisas; el agente ejecuta. Firma quien encarga.
