# 🐍 Instalar Python (y Node.js)

El taller necesita **Python 3.10 o superior** y **Node.js 18 o superior**. Comprueba si ya los tienes:

```bash
python3 --version      # Windows: py --version
node --version
```

Si ves `Python 3.10` o más y `v18` o más, salta a [🚀 Primeros pasos](Primeros-pasos.md). Si no, sigue tu sistema.

## 🪟 Windows

En **PowerShell**:

```powershell
winget install Python.Python.3.12
winget install OpenJS.NodeJS.LTS
```

Cierra la terminal y abre otra nueva. ¿Sin `winget`? Descarga los instaladores de <https://www.python.org/downloads/>
y <https://nodejs.org>. En el de Python **marca «Add python.exe to PATH»** en la primera pantalla.

- En Windows la orden es `py` (o `python`), no `python3`: escribe `py taller.py …` donde la guía pone `python3 taller.py …`.
- Si `python3` abre la Microsoft Store, desactívalo en *Configuración → Aplicaciones → Alias de ejecución de aplicaciones*.
- Si PowerShell no deja activar el entorno (`.venv\Scripts\Activate.ps1`):
  `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` y vuelve a intentarlo.

## 🍎 macOS

El `python3` que trae el Mac suele ser el 3.9, que es **demasiado antiguo**. Con [Homebrew](https://brew.sh):

```bash
brew install python@3.12 node
```

¿Sin Homebrew? Descarga los instaladores de <https://www.python.org/downloads/> y <https://nodejs.org>.

## 🐧 Linux (Ubuntu, Debian, Mint…)

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip nodejs npm
```

`python3-venv` es imprescindible: sin él falla `python3 -m venv .venv`. Si `node --version` es menor que 18, instala
la versión LTS desde <https://nodejs.org>. En Fedora: `sudo dnf install python3 nodejs`.

## ✅ Y después

```bash
npm i -g @opencode/cli@2.0.19     # el agente. Ojo: el paquete «opencode-ai» instala la 1.x, que no vale
```

Sigue en [🚀 Primeros pasos](Primeros-pasos.md). Si algo falla, mira [🔧 Problemas](Problemas.md).
