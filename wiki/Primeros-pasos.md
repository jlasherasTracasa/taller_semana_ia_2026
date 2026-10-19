# 🚀 Primeros pasos

Antes: [🛠️ Instalar](Instalar.md) (Python, Node.js, Git, opencode y el kit). ¿No puedes instalar? [🆘 Plan B](Plan-B.md).

Las órdenes son iguales en Windows, Linux y Mac **con el entorno activado** (verás `(.venv)` al principio de la línea):

| | Para activar el entorno, desde la carpeta `alumnos` |
|---|---|
| 🪟 Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |
| 🐧 Linux · 🍎 macOS | `. .venv/bin/activate` |

## 1. ¿Qué modelo vas a usar?

**No necesitas clave.** Sin `.env`, el kit usa un **modelo gratuito de opencode** (`opencode/big-pickle`). Si en
clase os dan una clave de **OpenRouter**, ponla así:

```powershell
copy .env.example .env        # Windows
```

```bash
cp .env.example .env          # Linux y Mac
```

Abre `.env` con el Bloc de notas (o cualquier editor) y rellena `OPENROUTER_API_KEY=` con la clave. Con ella, el
kit usa **GLM-5.3-Flash**, el modelo con el que se validaron los ejercicios. Más detalles en
[🤖 Modelos](Modelos.md) y [🔑 Variables de entorno](Variables-de-entorno.md).

¿Sin clave de OpenRouter y quieres hacer F.0 y F.1 (los dos ejercicios que son programas de Python)? Saca una clave
**gratuita y personal**, sin tarjeta, en [Google AI Studio](https://aistudio.google.com/apikey) o en
[Groq](https://console.groq.com/keys), y ponla en `.env` en la línea `GEMINI_API_KEY=` o `GROQ_API_KEY=`. Los pasos,
en [🤖 Modelos](Modelos.md), apartado «F.0 y F.1 sin OpenRouter».

> 🔐 `.env` es tuyo y de nadie más: no lo subas a git, no lo pegues en un chat, no lo enseñes en pantalla.

## 2. Comprueba que todo está listo

```bash
python taller.py entorno
```

## 3. Mira el menú

```bash
python taller.py
```

Perfiles, itinerarios, áreas y ejercicios. Los marcados con 🎥 los hace el profesor **en directo**; el resto son
**prácticas** que haces tú (y en las que preguntas al profesor cuando te atasques).

## 4. Tu primer encargo, en modo interactivo

```bash
python taller.py empezar ej24      # prepara ~/taller-agentes/ej24_lista_compra y te cuenta la situación
python taller.py abrir ej24        # abre opencode en esa carpeta
```

Se abre opencode a pantalla completa. **Copia el encargo** que te ha enseñado `empezar` (también está en el
enunciado y en la web), **pégalo** en la caja de abajo (`Ctrl+V`, o clic derecho en Windows) y pulsa **Enter**.

Mira lo que hace: qué ficheros lee (`→ Read`), qué escribe (`← Write`), qué órdenes ejecuta. Cuando termine, sal con
**`Ctrl+C`** (con la caja vacía) o escribiendo `/exit`. Todo lo del modo interactivo, en
[🖥️ Modo interactivo](Modo-interactivo.md).

## 5. ¿Lo ha hecho de verdad?

```bash
python taller.py comprobar ej24
```

Si sale ✅, el ejercicio cuenta como completado y te propone el siguiente. Si sale ❌, vuelve a abrir opencode
(`python taller.py abrir ej24`) y pídele que lo arregle, o mejora el encargo.

Abre `~/taller-agentes/ej24_lista_compra/lista_compra.md` y compruébalo tú también: ¿son 1,2 kg de pochas?

## ¿Y si prefiero no conversar?

`python taller.py lanzar ej24` hace el encargo de una vez, sin abrir la pantalla interactiva (modo `opencode run`),
guarda lo que pasa en `salida.txt` y te dice cuántos tokens ha gastado. Es como se validaron los ejercicios. En clase
usaremos el modo interactivo: se ve mejor qué hace el agente y puedes aprobar permisos y corregirle sobre la marcha.

## Dónde están tus cosas

| Qué | Dónde |
|---|---|
| El kit (no lo toques) | `taller_semana_ia_2026/alumnos/` |
| Tus carpetas de trabajo (copias) | `~/taller-agentes/<ejercicio>/` · en Windows, `C:\Users\<tú>\taller-agentes\` |
| Tu progreso | `~/taller-agentes/progreso.json` (`python taller.py progreso`) |
| Lo que hizo el agente al validar | `alumnos/soluciones/<ejercicio>/` |
