# 🛠️ Instalar en Windows, Linux o Mac

El taller necesita cuatro cosas: **Python 3.10+**, **Node.js 18+**, **Git** y el agente **opencode 2.0.19**. No hace
falta tarjeta gráfica ni clave: el modelo gratuito de opencode funciona sin cuenta. Calcula 15 minutos.

> 💡 ¿No puedes instalar nada (por ejemplo, en un ordenador de la UPNA) o no tienes portátil? Ve directamente al
> [🆘 Plan B](Plan-B.md): todo funciona desde el navegador.

Busca tu sistema: 🪟 **Windows** (primero), 🐧 **Linux** y 🍎 **macOS** (más abajo).

---

## 🪟 Windows

Todo se hace en **PowerShell**: pulsa la tecla Windows, escribe `PowerShell` y ábrelo (no hace falta como
administrador).

### 1. Python, Node.js y Git

```powershell
winget install -e --id Python.Python.3.12
winget install -e --id OpenJS.NodeJS.LTS
winget install -e --id Git.Git
```

**Cierra PowerShell y abre otro** (si no, no encuentra lo que acabas de instalar) y comprueba:

```powershell
py --version        # Python 3.12.x
node --version      # v22.x (vale cualquier v18 o más)
git --version
```

¿Sin `winget`, o te pide permisos de administrador? Descarga los instaladores:

- Python: <https://www.python.org/downloads/>. En la primera pantalla **marca «Add python.exe to PATH»** y elige
  *Install Now* (se instala solo para tu usuario, sin administrador).
- Node.js: <https://nodejs.org> (versión LTS). ¿Sin permisos? Mira el [Plan B](Plan-B.md), opción 1.
- Git: <https://git-scm.com/download/win>. Además de `git`, instala **Git Bash**, que opencode usa para ejecutar
  órdenes en Windows.

### 2. El kit y el agente

```powershell
cd $HOME
git clone https://github.com/jlasherasTracasa/taller_semana_ia_2026.git
cd taller_semana_ia_2026\alumnos
npm i -g @opencode/cli@2.0.19
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

- ¿Sin git? En GitHub, botón verde **Code → Download ZIP**, descomprímelo en tu carpeta personal y entra en
  `alumnos`.
- Si `Activate.ps1` da un error de «ejecución de scripts deshabilitada», ejecuta una vez
  `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, contesta `S` y repite.
- Con el entorno activado verás `(.venv)` al principio de la línea. Desde ahí la orden es **`python`** (no `py`
  ni `python3`).

### 3. Comprueba que todo está listo

```powershell
python taller.py entorno
```

Seis comprobaciones, incluida una llamada real al modelo. Si todas salen ✅, sigue en
[🚀 Primeros pasos](Primeros-pasos.md).

### Cada vez que abras PowerShell

```powershell
cd $HOME\taller_semana_ia_2026\alumnos
.venv\Scripts\Activate.ps1
```

---

## 🐧 Linux (Ubuntu, Debian, Mint…)

### 1. Python, Node.js y Git

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip nodejs npm git
node --version
```

- `python3-venv` es imprescindible: sin él falla `python3 -m venv .venv`.
- Si `node --version` es menor que **v18** (pasa en Ubuntu 22.04 y anteriores), instala Node en tu carpeta, sin
  `sudo`:

  ```bash
  mkdir -p ~/.local/node
  curl -fsSL https://nodejs.org/dist/v22.12.0/node-v22.12.0-linux-x64.tar.xz | tar -xJ -C ~/.local/node --strip-components=1
  echo 'export PATH="$HOME/.local/node/bin:$PATH"' >> ~/.bashrc && . ~/.bashrc
  ```

- Fedora: `sudo dnf install python3 nodejs git`.

### 2. El kit y el agente

```bash
cd ~
git clone https://github.com/jlasherasTracasa/taller_semana_ia_2026.git
cd taller_semana_ia_2026/alumnos
npm i -g @opencode/cli@2.0.19          # si da EACCES: mira Problemas
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
```

### 3. Comprueba

```bash
python taller.py entorno
```

Cada vez que abras una terminal: `cd ~/taller_semana_ia_2026/alumnos && . .venv/bin/activate`.

---

## 🍎 macOS

El `python3` que trae el Mac suele ser el 3.9, **demasiado antiguo**. Con [Homebrew](https://brew.sh):

```bash
brew install python@3.12 node git
cd ~
git clone https://github.com/jlasherasTracasa/taller_semana_ia_2026.git
cd taller_semana_ia_2026/alumnos
npm i -g @opencode/cli@2.0.19
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python taller.py entorno
```

¿Sin Homebrew? Instaladores de <https://www.python.org/downloads/> y <https://nodejs.org>.

---

## ⚠️ Dos avisos

- **El paquete bueno es `@opencode/cli@2.0.19`.** El paquete `opencode-ai` de npm instala la 1.x, que no vale.
- **No actualices opencode durante el taller.** Al abrirlo verás «/update to install v2.0.x»: ignóralo. El kit está
  validado con la 2.0.19 y entre versiones cambian cosas ([🔄 opencode 2.x](opencode-2.md)).

Si algo falla, mira [🔧 Problemas](Problemas.md).
