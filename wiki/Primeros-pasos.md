# 🚀 Primeros pasos

Necesitas un portátil **sin GPU** (vale cualquiera), **Node.js 18+** y **Python 3.10+**. Calcula 10 minutos.

## 1. Descarga el kit

```bash
git clone https://github.com/jlasherasTracasa/taller_semana_ia_2026.git
cd taller_semana_ia_2026/alumnos
```

¿Sin git? Botón verde **Code → Download ZIP** en GitHub, descomprime y entra en `alumnos/`.

## 2. Instala el agente y las bibliotecas

```bash
npm i -g opencode-ai                 # el agente (validado con la 2.0.19)
python3 -m venv .venv                # un entorno de Python solo para el taller
. .venv/bin/activate                 # Windows (PowerShell): .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 3. Tu clave

```bash
cp .env.example .env                 # Windows: copy .env.example .env
```

Abre `.env` y rellena **una** de las dos opciones con lo que te demos en clase:

- **LiteLLM del taller**: `LITELLM_API_BASE` y `LITELLM_API_KEY`.
- **OpenRouter**: `OPENROUTER_API_KEY` (el kit cambia solo a `openrouter/z-ai/glm-5.3-flash`).

> ¿Prefieres variables de entorno, o estás en Windows? Mira [🔑 Variables de entorno](Variables-de-entorno.md).

> 🔐 `.env` es tuyo y de nadie más: no lo subas a git, no lo pegues en un chat, no lo enseñes en pantalla.

## 4. Comprueba que todo está listo

```bash
bash comprobar_entorno.sh            # Windows sin bash: python3 taller.py
python3 taller.py                    # perfiles, áreas, ejercicios y tu progreso
```

## 5. Tu primer encargo

```bash
python3 taller.py empezar ej01       # te explica la situación y prepara ~/taller-agentes/ej01_pagina_personal
python3 taller.py lanzar ej01        # el agente trabaja (tarda unos 30 s)
python3 taller.py comprobar ej01     # ¿lo hizo de verdad? Si sí, queda completado
```

Abre `~/taller-agentes/ej01_pagina_personal/index.html` en el navegador. ¡Es la web de Pilar!

### ¿Y el modelo? ¿Por qué pone «Qwen3.8»?

El LiteLLM del taller publica **GLM-5.3-Flash** con el nombre `Qwen3.8-27B-FP8` por retrocompatibilidad. Es el
mismo modelo. Con OpenRouter verás su nombre real: `z-ai/glm-5.3-flash`.
