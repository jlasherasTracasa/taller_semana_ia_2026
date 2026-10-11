# 🔑 Variables de entorno: dónde se guarda tu clave

> ¿Usas el modelo gratuito de opencode? Entonces **no necesitas ninguna clave** y puedes saltarte esta página.
> Solo hace falta si en clase os dan una clave de OpenRouter ([🤖 Modelos](Modelos.md)).

Una **variable de entorno** es un par `NOMBRE=valor` que vive en tu terminal y que pueden leer los programas que
lances desde ella. Las usamos para que la clave **no esté escrita en ningún fichero que se comparta**: opencode
lee `OPENROUTER_API_KEY` directamente del entorno, y en un `opencode.json` las claves se escriben como
`{env:NOMBRE}` («pon aquí lo que valga esa variable»), nunca a mano.

## Las variables del taller

| Variable | Qué lleva | Ejemplo |
|---|---|---|
| `OPENROUTER_API_KEY` | Tu clave de OpenRouter | `sk-or-v1-…` (te la dan en clase) |
| `TALLER_MODELO` | *(opcional)* otro modelo para los ejercicios | `opencode/nemotron-3-ultra-free` |
| `TALLER_TRABAJO` | *(opcional)* dónde crea `taller.py` las carpetas de trabajo | `~/taller-agentes` |
| `LITELLM_API_BASE` · `LITELLM_API_KEY` | *(solo el docente)* su LiteLLM propio | — |

## ✅ La forma fácil: el fichero `.env`

En la carpeta `alumnos`:

```powershell
copy .env.example .env        # 🪟 Windows (PowerShell)
notepad .env
```

```bash
cp .env.example .env          # 🐧 Linux · 🍎 Mac
nano .env                     # o el editor que quieras
```

Rellena la línea:

```bash
OPENROUTER_API_KEY=sk-or-v1-la-clave-que-os-damos
```

Sin espacios alrededor del `=` y sin comillas. **`taller.py` lee este fichero solo** cada vez que lo usas: no hace
falta nada más. `.env` está en `.gitignore`, así que git no lo subirá.

## Si quieres usar `opencode` sin taller.py

`taller.py` carga el `.env` por ti. Si lanzas `opencode` a mano, la variable tiene que estar en tu terminal:

### 🪟 Windows (PowerShell)

```powershell
$env:OPENROUTER_API_KEY = "sk-or-v1-…"          # solo para esta ventana
setx OPENROUTER_API_KEY "sk-or-v1-…"            # para siempre (ventanas que abras DESPUÉS)
```

También: *Inicio → «Editar las variables de entorno de esta cuenta»*. Para cargar el `.env` entero en la ventana:

```powershell
Get-Content .env | Where-Object { $_ -match '^\s*[^#].*=' } | ForEach-Object {
  $n, $v = $_ -split '=', 2; Set-Item "env:$($n.Trim())" $v.Trim()
}
```

En el Símbolo del sistema (cmd): `set OPENROUTER_API_KEY=sk-or-v1-…`.

### 🐧 Linux · 🍎 macOS

```bash
export OPENROUTER_API_KEY="sk-or-v1-…"          # solo para esta terminal
set -a; . ./.env; set +a                         # cargar el .env entero
```

Para siempre, añade al final de `~/.bashrc` (Linux) o `~/.zshrc` (Mac) la línea que carga tu `.env`, mejor que la
clave misma:

```bash
echo 'set -a; . "$HOME/taller_semana_ia_2026/alumnos/.env"; set +a' >> ~/.bashrc
```

## 🔍 Comprobar que está definida (sin enseñar la clave)

```bash
python taller.py entorno             # dice qué modelo usa y si la clave está; nunca la imprime
```

```powershell
if ($env:OPENROUTER_API_KEY) { "definida" } else { "FALTA" }
```

> ⚠️ No hagas `echo $OPENROUTER_API_KEY` con el proyector encendido.

## 🤖 Cómo las usa opencode

En `opencode.json`, `{env:NOMBRE}` se sustituye por el valor de la variable **cuando arranca opencode**.

**Trampa de opencode 2.x:** sin `--standalone`, opencode manda el trabajo a un **servicio en segundo plano** que se
arrancó antes y **no ve las variables que acabas de definir**. Síntomas: `Invalid URL` o `No api key passed in`.
Soluciones:

1. Usar `python taller.py abrir …` o `lanzar …` (ya ponen `--standalone` y leen tu `.env`).
2. Añadir `--standalone`: `opencode --standalone` o `opencode run --standalone "…"`.
3. Reiniciar el servicio después de definir las variables: `opencode service restart`.

## 🔐 Reglas

- La clave va en `.env` o en variables, **nunca** en `opencode.json`, en el código ni en un chat.
- Si se te escapa (la pegas, la proyectas, la subes), díselo al profesor para que la anule y te dé otra.
- Cada persona o pareja, su clave: así se limita el gasto de cada una.
