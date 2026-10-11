# 🤖 Qué modelo usa el agente

opencode es el **agente** (el programa que lee, escribe y ejecuta); el **modelo** es el «cerebro» al que consulta en
cada paso, y está en internet. El kit elige el modelo solo, según lo que tengas en tu `.env`:

| Tienes… | Modelo | Coste | Para qué |
|---|---|---|---|
| **Nada** (sin `.env`) | `opencode/big-pickle`, gratuito de opencode | 0 € | Todos los ejercicios menos F.0 y F.1 |
| `OPENROUTER_API_KEY` | `openrouter/z-ai/glm-5.3-flash` (GLM-5.3-Flash) | ≈ 1 céntimo por ejercicio | Todos, F.0 y F.1 incluidos. Con él se validaron los ejercicios |
| `TALLER_MODELO` | El que pongas | Depende | Probar otros modelos |

`python taller.py entorno` te dice cuál está usando, y `abrir` y `lanzar` lo muestran al empezar.

## 🆓 Los modelos gratuitos de opencode

opencode ofrece algunos modelos gratis a través de su servicio **OpenCode Zen**. No piden cuenta ni clave.

- **Solo funcionan dentro de opencode.** Por eso F.0 y F.1, que son programas de Python que llaman al modelo
  directamente, necesitan OpenRouter. En clase, esos dos son demostraciones del profesor.
- **La lista cambia con el tiempo**: un modelo gratuito puede desaparecer o dejar de ser gratis. Para ver los
  disponibles, dentro de opencode escribe `/models`; los gratuitos llevan «Free» en el nombre (también
  `big-pickle`). El 11-10-2026 había, entre otros, `big-pickle`, `nemotron-3-ultra-free`, `mimo-v2.6-flash-free`,
  `step-5-preview-free` y `ling-3.1-flash-free`.
- **Pueden tener límites de uso.** Si un aula entera sale por la misma conexión, quizá respondan más despacio o den
  error de límite. Entonces: espera un minuto, prueba otro modelo gratuito o usa la clave de OpenRouter.
- **Privacidad**: lo que lee el agente viaja al proveedor del modelo, y los servicios gratuitos pueden usarlo para
  mejorar sus modelos. Con los datos ficticios del taller no hay problema; con los tuyos de verdad, piénsalo.

### Validación con el modelo gratuito

Los ejercicios se validaron el 11-10-2026 con `opencode/big-pickle` además de con GLM-5.3-Flash: el resultado de
cada uno está en su enunciado, en «Lo que pasó al validarlo».

## 💳 OpenRouter (GLM-5.3-Flash)

[OpenRouter](https://openrouter.ai) da acceso a cientos de modelos con una sola clave, pagando por uso. Para el
taller, la organización facilita una clave con un límite de gasto. Ponla en `.env`:

```bash
OPENROUTER_API_KEY=sk-or-v1-…
```

Con ella, el kit usa GLM-5.3-Flash: barato (≈ 0,15 $ por millón de tokens de entrada), con *tool calling* y contexto
largo. Precios y presupuesto por alumno en `profesor/PRESUPUESTO.md`.

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
