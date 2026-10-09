# 🔑 Variables de entorno: dónde se guarda tu clave

Una **variable de entorno** es un par `NOMBRE=valor` que vive en tu terminal y que pueden leer los programas que
lances desde ella. Las usamos para que la clave del modelo **no esté escrita en ningún fichero que se comparta**:
`opencode.json` solo dice `{env:LITELLM_API_KEY}` («pon aquí lo que valga esa variable»).

## Las variables del taller

| Variable | Qué lleva | Ejemplo |
|---|---|---|
| `LITELLM_API_BASE` | La URL del LiteLLM del taller, **sin** `/v1` al final | `https://litellm.ejemplo.es` |
| `LITELLM_API_KEY` | Tu clave del LiteLLM | `sk-…` (te la damos en clase) |
| `OPENROUTER_API_KEY` | Tu clave de OpenRouter (alternativa a las dos anteriores) | `sk-or-v1-…` |
| `TALLER_TRABAJO` | *(opcional)* dónde crea `taller.py` las carpetas de trabajo | `~/taller-agentes` |
| `TALLER_MODELO` | *(opcional)* otro modelo para F.0 y F.1 | `openrouter/z-ai/glm-5.3-flash` |

## ✅ La forma fácil: el fichero `.env` + `taller.py`

```bash
cd alumnos
cp .env.example .env        # Windows: copy .env.example .env
```

Abre `.env` con cualquier editor y rellena:

```bash
LITELLM_API_BASE=https://la-url-que-os-damos
LITELLM_API_KEY=la-clave-que-os-damos
```

Sin espacios alrededor del `=` y sin comillas. **`taller.py` lee este fichero solo** cada vez que lo usas: no hace
falta nada más. `.env` está en `.gitignore`, así que git no lo subirá.

## 🐧 Linux y 🍎 macOS (bash o zsh)

### Solo para esta terminal (se pierde al cerrarla)

```bash
export LITELLM_API_BASE="https://la-url"
export LITELLM_API_KEY="la-clave"
```

### Cargar todo el `.env` de golpe

```bash
set -a; . ./.env; set +a      # «set -a» exporta todo lo que se defina a continuación
```

### Para siempre (todas las terminales nuevas)

Añade las líneas `export …` al final de `~/.bashrc` (Linux) o `~/.zshrc` (macOS) y abre una terminal nueva.
Más seguro: no pongas la clave ahí; pon solo la línea que carga tu `.env`:

```bash
echo 'set -a; . "$HOME/taller_semana_ia_2026/alumnos/.env"; set +a' >> ~/.bashrc
```

## 🪟 Windows

### PowerShell, solo para esta ventana

```powershell
$env:LITELLM_API_BASE = "https://la-url"
$env:LITELLM_API_KEY  = "la-clave"
```

### PowerShell, cargar el `.env`

```powershell
Get-Content .env | Where-Object { $_ -match '^\s*[^#].*=' } | ForEach-Object {
  $n, $v = $_ -split '=', 2; Set-Item "env:$($n.Trim())" $v.Trim()
}
```

### Para siempre (tu usuario)

```powershell
setx LITELLM_API_BASE "https://la-url"
setx LITELLM_API_KEY  "la-clave"
```

`setx` solo afecta a las ventanas que abras **después**. También: *Inicio → «Editar las variables de entorno de
esta cuenta»*.

### Símbolo del sistema (cmd), solo para esta ventana

```bat
set LITELLM_API_BASE=https://la-url
set LITELLM_API_KEY=la-clave
```

## 🔍 Comprobar que está definida (sin enseñar la clave)

```bash
bash comprobar_entorno.sh                               # dice «definida (valor oculto)»
[ -n "$LITELLM_API_KEY" ] && echo "definida" || echo "FALTA"
```

```powershell
if ($env:LITELLM_API_KEY) { "definida" } else { "FALTA" }
```

> ⚠️ No hagas `echo $LITELLM_API_KEY` con el proyector encendido.

## 🤖 Cómo las usa opencode

En `opencode.json`, `{env:NOMBRE}` se sustituye por el valor de la variable **cuando arranca opencode**:

```json
"options": {
  "baseURL": "{env:LITELLM_API_BASE}/v1",
  "apiKey": "{env:LITELLM_API_KEY}"
}
```

**Trampa de opencode 2.x:** `opencode run` sin `--standalone` manda el encargo a un **servicio en segundo plano**
que se arrancó antes y **no ve las variables que acabas de definir**. Síntomas: `Invalid URL` o
`No api key passed in`. Soluciones (de más a menos cómoda):

1. Usar `python3 taller.py lanzar …` (ya pone `--standalone` y lee tu `.env`).
2. Añadir `--standalone`: `opencode run --standalone "…"`.
3. Reiniciar el servicio después de definir las variables: `opencode service restart`.

## 🔐 Reglas

- La clave va en `.env` o en variables, **nunca** en `opencode.json`, en el código ni en un chat.
- Si se te escapa (la pegas, la proyectas, la subes), pide otra y que anulen la vieja.
- Cada persona, su clave: así se puede limitar el gasto de cada una.
