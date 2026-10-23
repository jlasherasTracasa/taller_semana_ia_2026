# 🔑 La clave de clase (con PIN)

En clase hay una **clave de OpenRouter compartida** para usar **GLM-5.3-Flash**, un modelo más rápido y fiable que
los gratuitos. Con ella también funcionan F.0 y F.1. No hace falta: todo el taller funciona sin clave, con el modelo
gratuito de opencode.

La clave está en la web del taller **cifrada**: solo se puede ver con el **PIN** que el profesor da en clase.

## Para usarla (alumnos)

### 1. Abre la página de la clave

En el navegador del portátil (mejor que en el móvil, para poder copiarla):

**<https://jlasherastracasa.github.io/taller_semana_ia_2026/#/clave>**

También está en la diapositiva «Clave de clase», con un código QR.

### 2. Escribe el PIN y pulsa «Ver la clave»

Tarda un par de segundos: el navegador descifra la clave en tu ordenador, sin enviar el PIN a ningún sitio. Si el PIN
no es correcto, dice «Ese PIN no es».

### 3. Copia la línea y pégala en tu `.env`

Sale una línea que empieza por `OPENROUTER_API_KEY=sk-or-v1-…`, con un botón **Copiar**. En la carpeta `alumnos` del kit:

```powershell
copy .env.example .env        # 🪟 Windows (si aún no tienes .env)
notepad .env
```

```bash
cp .env.example .env          # 🐧 Linux · 🍎 Mac · ☁️ Codespaces (si aún no tienes .env)
nano .env                     # o ábrelo en el editor de Codespaces
```

Sustituye la línea `OPENROUTER_API_KEY=` por la que has copiado, sin espacios ni comillas, y guarda.

### 4. Comprueba que el kit la usa

```bash
python taller.py entorno
```

En el apartado **5) Modelo** tiene que poner `openrouter/z-ai/glm-5.3-flash`.

> Los ejercicios que ya habías **empezado** guardan el modelo en su carpeta y siguen con el gratuito. Para pasarlos a
> la clave: `python taller.py abrir ej24 --modelo openrouter/z-ai/glm-5.3-flash`. Los que empieces a partir de ahora ya
> usan la clave.

> 🔐 Es una clave **compartida y con límite de gasto**, solo para el taller: no la publiques, no la subas a git y no la
> uses para otras cosas. Deja de funcionar a los pocos días.

## Cómo funciona

- La página no guarda la clave tal cual, sino **cifrada** con AES-256-GCM: un texto ilegible
  (`herramientas/clave_clase.json` en el repositorio).
- La llave para descifrarla sale del **PIN** con PBKDF2 (un millón de vueltas de SHA-256, para que probar PINs al azar
  sea lento).
- Cuando escribes el PIN, el navegador hace la misma cuenta con WebCrypto y descifra. El PIN no viaja por internet ni
  está escrito en ningún fichero.

**Lo que no protege**: un PIN corto (por ejemplo, de 4 cifras) se puede adivinar probándolos todos en unas horas.
Por eso la clave tiene un **límite de gasto** en OpenRouter, **caduca** a los pocos días y se quita de la web al
terminar el taller.

## Para el profesor: ponerla, cambiar el PIN y quitarla

Desde la raíz del repositorio. Hace falta la biblioteca `cryptography` (ya viene con el kit:
`alumnos/.venv/bin/python`).

**Ponerla o cambiar el PIN** (la clave y el PIN van en variables de entorno, no en ningún fichero):

```bash
CLAVE=sk-or-v1-… PIN=1234 python3 herramientas/cifrar_clave.py
git add herramientas/clave_clase.json && git commit -m "Clave de clase" && git push
```

En un par de minutos la web se actualiza sola (GitHub Actions). Prueba el PIN en `#/clave`.

**Quitarla** al terminar el taller:

```bash
python3 herramientas/cifrar_clave.py --quitar
git commit -am "Quita la clave de clase" && git push
```

Y en <https://openrouter.ai/keys>, desactiva la clave. Antes del taller conviene darle un **límite de gasto** y una
**fecha de caducidad** al crearla (en *Credit limit* y *Expiration*).

> Ojo: el texto cifrado queda en el historial de git aunque lo quites. Por eso lo que de verdad protege es desactivar
> la clave en OpenRouter.

## Las valoraciones

El código QR de la última diapositiva lleva a **<https://jlasherastracasa.github.io/taller_semana_ia_2026/#/valorar>**:
un formulario anónimo (nota de 1 a 5, ritmo, utilidad y comentarios). Cada valoración se envía a ntfy.sh, que la
guarda 12 horas. Una GitHub Action de un repositorio privado del profesor la copia cada 15 minutos a
`valoraciones.json` y actualiza un `RESUMEN.md` con la nota media y todos los comentarios.
