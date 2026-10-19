# 🤖 Qué modelo usa el agente

opencode es el **agente** (el programa que lee, escribe y ejecuta); el **modelo** es el «cerebro» al que consulta en
cada paso, y está en internet. El kit elige el modelo solo, según lo que tengas en tu `.env`:

| Tienes… | Modelo | Coste | Para qué |
|---|---|---|---|
| **Nada** (sin `.env`) | `opencode/big-pickle`, gratuito de opencode | 0 € | Todos los ejercicios menos F.0 y F.1 |
| `OPENROUTER_API_KEY` | `openrouter/z-ai/glm-5.3-flash` (GLM-5.3-Flash) | ≈ 1 céntimo por ejercicio | Todos, F.0 y F.1 incluidos. Con él se validaron los ejercicios |
| `GEMINI_API_KEY` o `GROQ_API_KEY` | Uno gratuito de Google o de Groq, **solo en F.0 y F.1** | 0 € | Hacer F.0 y F.1 sin OpenRouter. El resto sigue con el gratuito de opencode |
| `TALLER_MODELO` | El que pongas | Depende | Probar otros modelos |

`python taller.py entorno` te dice cuál está usando, y `abrir` y `lanzar` lo muestran al empezar.

## 🆓 Los modelos gratuitos de opencode

opencode ofrece algunos modelos gratis a través de su servicio **OpenCode Zen**. No piden cuenta ni clave.

- **Solo funcionan dentro de opencode.** Por eso F.0 y F.1, que son programas de Python que llaman al modelo
  directamente, necesitan una clave: la de OpenRouter o una gratuita de Gemini o Groq
  (apartado «F.0 y F.1 sin OpenRouter», más abajo). En clase, esos dos son demostraciones del profesor.
- **La lista cambia con el tiempo**: un modelo gratuito puede desaparecer o dejar de ser gratis. Para ver los
  disponibles, dentro de opencode escribe `/models`; los gratuitos llevan «Free» en el nombre (también
  `big-pickle`). El 11-10-2026 había, entre otros, `big-pickle`, `nemotron-3-ultra-free`, `mimo-v2.6-flash-free`,
  `step-5-preview-free` y `ling-3.1-flash-free`.
- **Tienen un límite de uso, y es por modelo.** El 11-10-2026, tras unas cien ejecuciones seguidas desde la misma
  conexión, `big-pickle` respondió `Rate limit exceeded` mientras otros gratuitos seguían funcionando. Si te pasa:
  - en modo interactivo, `/models` y elige otro «Free» (por ejemplo `nemotron-3-ultra-free`);
  - con `python taller.py lanzar`, el kit cambia solo al siguiente gratuito;
  - para todo el taller, pon `TALLER_MODELO=opencode/nemotron-3-ultra-free` en tu `.env` (en clase podemos repartir
    la sala entre dos modelos para no agotar ninguno);
  - y si no hay manera, la clave de OpenRouter.
- **Privacidad**: lo que lee el agente viaja al proveedor del modelo, y los servicios gratuitos pueden usarlo para
  mejorar sus modelos. Con los datos ficticios del taller no hay problema; con los tuyos de verdad, piénsalo.

### Validación con el modelo gratuito

Los ejercicios se validaron el 11-10-2026 con `opencode/big-pickle` además de con GLM-5.3-Flash: todos los que se
lanzan con un encargo cumplieron el criterio también con el gratuito. El resultado de cada uno está en su enunciado,
en «Lo que pasó al validarlo».

## 💳 OpenRouter (GLM-5.3-Flash)

[OpenRouter](https://openrouter.ai) da acceso a cientos de modelos con una sola clave, pagando por uso. Para el
taller, la organización facilita una clave con un límite de gasto. Ponla en `.env`:

```bash
OPENROUTER_API_KEY=sk-or-v1-…
```

Con ella, el kit usa GLM-5.3-Flash: barato (≈ 0,15 $ por millón de tokens de entrada), con *tool calling* y contexto
largo. Precios y presupuesto por alumno en `profesor/PRESUPUESTO.md`.

## 🆓 F.0 y F.1 sin OpenRouter: Gemini o Groq, gratis

F.0 y F.1 son programas de Python que llaman al modelo con `litellm`, sin pasar por opencode. Si no tienes la clave
de OpenRouter, saca **una clave gratuita y personal** en uno de estos dos sitios. Ninguno pide tarjeta, y no hace
falta ningún programa intermedio: `litellm` habla con los dos directamente.

| | Dónde se saca | Variable en `.env` | Modelo que usa el kit |
|---|---|---|---|
| **Google AI Studio** (Gemini) | <https://aistudio.google.com/apikey> → *Create API key* (con tu cuenta de Google) | `GEMINI_API_KEY` | `gemini/gemini-flash-latest` |
| **Groq** | <https://console.groq.com/keys> → *Create API Key* (cuenta con correo, Google o GitHub) | `GROQ_API_KEY` | `groq/openai/gpt-oss-120b` |

Copia `.env.example` a `.env` (como en [🚀 Primeros pasos](Primeros-pasos.md)) y rellena **una** de las dos líneas:

```bash
GEMINI_API_KEY=AIza…
# o bien
GROQ_API_KEY=gsk_…
```

`python taller.py entorno` te dice qué clave usarán F.0 y F.1. Si tienes varias, manda la de OpenRouter, luego
Gemini y luego Groq. El agente (opencode) **no cambia**: sigue con el modelo gratuito de opencode.

- **Es tu clave, no la compartas.** Cada alumno saca la suya: así lo permiten las condiciones de uso de los dos
  servicios, y el límite de uso de cada uno es solo tuyo. Por eso no montamos un servidor común para toda la clase.
- **Los modelos gratuitos cambian cada mes.** Google y Groq retiran modelos, los cambian de nombre o les bajan el
  límite sin avisar. Antes del taller hay que comprobar que el modelo de la tabla sigue siendo gratuito y admite
  *tool calling*: en la página de modelos de [Gemini](https://ai.google.dev/gemini-api/docs/models) y en
  <https://console.groq.com/docs/tool-use>. Si ha cambiado, pon el nuevo en `.env` con `TALLER_MODELO_PY`, por
  ejemplo `TALLER_MODELO_PY=groq/qwen/qwen3-32b`. Esa variable solo la leen F.0 y F.1; no uses `TALLER_MODELO`,
  que cambiaría también el modelo de opencode.
- **Límites**: con la clave gratuita hay unas pocas peticiones por minuto y un tope diario. F.0 hace como mucho 8
  llamadas por ejecución y F.1 dos, así que da de sobra. Si ves `429` o `RESOURCE_EXHAUSTED`, espera un minuto.
- **Privacidad**: en la capa gratuita, Google puede usar lo que envías para mejorar sus modelos. Con los ficheros de
  F.0 y F.1 no hay problema.
- **Sin validar aún**: los ejercicios se validaron con GLM-5.3-Flash. Con Gemini y Groq se ha comprobado que el kit
  llega a los dos servicios, pero no una ejecución completa con clave real.

## 🔁 Cambiar de modelo

Para un rato, dentro de opencode: **`/models`** y elige otro.

Para todos los ejercicios: añade a tu `.env` una línea con el modelo, con el formato `proveedor/modelo`:

```bash
TALLER_MODELO=opencode/nemotron-3-ultra-free
```

`taller.py` lo escribe en el `opencode.json` de cada carpeta de trabajo **la próxima vez que hagas `empezar`** en una
carpeta nueva. Para una carpeta que ya existe, cambia la línea `"model"` de su `opencode.json` o bórrala y vuelve a
`empezar`.

## 🧑‍🏫 LiteLLM (solo para el docente)

El `opencode.json` del kit trae también un proveedor `vllm` que apunta a un LiteLLM propio (`LITELLM_API_BASE` y
`LITELLM_API_KEY`). Lo usa el profesor para validar los ejercicios con GLM-5.3-Flash en local. Si defines esas dos
variables, tienen prioridad sobre OpenRouter y el modelo gratuito.
