# 📋 Chuleta: todo en una página

Las órdenes `python taller.py …` van en la **terminal**, desde la carpeta `alumnos` y con el entorno activado
(verás `(.venv)` al principio de la línea). **Dentro de opencode** solo se escribe el encargo o un comando que empieza
por `/`.

| Para activar el entorno, desde `alumnos` | |
|---|---|
| 🪟 Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |
| 🐧 Linux · 🍎 Mac · ☁️ Codespaces | `. .venv/bin/activate` |

## Un ejercicio, de principio a fin

```bash
python taller.py empezar ej24        # 1. prepara tu carpeta y te enseña el encargo
python taller.py abrir ej24          # 2. abre opencode: pega el encargo y pulsa Enter
python taller.py comprobar ej24      # 3. al salir (Ctrl+C), ¿lo ha hecho de verdad?
```

## Todas las órdenes

| Quiero… | Orden |
|---|---|
| Ver perfiles, ejercicios y mi progreso | `python taller.py` |
| Comprobar que mi ordenador está listo | `python taller.py entorno` |
| Preparar un ejercicio | `python taller.py empezar ej24` |
| Abrir opencode para hacerlo | `python taller.py abrir ej24` |
| Saber si está bien | `python taller.py comprobar ej24` |
| Ver mi carpeta de trabajo (ruta, ficheros, y la abre) | `python taller.py carpeta ej24` |
| Leer un fichero de esa carpeta | `python taller.py carpeta ej24 lista_compra.md` |
| Empezar un ejercicio otra vez desde cero | `python taller.py empezar ej24 --de-cero` |
| Abrirlo con otro modelo | `python taller.py abrir ej24 --modelo beam-free` |
| Hacerlo de una vez, sin conversar | `python taller.py lanzar ej24` |
| F.0, F.1 y F.9 (programas, no usan opencode) | `python taller.py ejecutar f1 fc_calculadora.py "tu pregunta"` |
| Mi nivel | `python taller.py progreso` |

## Dentro de opencode

| Tecla o comando | Qué hace |
|---|---|
| **Enter** | Envía el encargo |
| `Ctrl+V` (o clic derecho en Windows) | Pega |
| **Esc** | Para al agente mientras trabaja |
| **Ctrl+C** con la caja vacía, o `/exit` | Sale |
| `/models` | Cambia de modelo (escribe `free` para ver los gratuitos) |
| `/` + Enter + Enter | Elige un comando del proyecto y lo envía (F.3) |
| *Permission required* | Lee la orden: **Allow once**, **Always allow** o **Reject** |

## El modelo

| Situación | Qué hacer |
|---|---|
| En clase (recomendado) | La **[🔑 clave de clase](Clave-de-clase.md)**: abre `…/#/clave` en la web, escribe el PIN de la pizarra y pega la línea en `alumnos/.env` |
| `Free usage limit reached` | El gratuito se ha agotado: la clave de clase, o dentro de opencode `/models` y otro «Free» (`beam-free`, `flint-40b-free`…) |
| Sin clave, en casa | No hace falta nada: el kit usa un modelo gratuito de opencode |
| F.0 y F.1 | Necesitan clave: la de clase, o una gratuita de Groq ([🤖 Modelos](Modelos.md)) |

## Si algo falla

| Lo que ves | Qué hacer |
|---|---|
| «No se reconoce python» / abre la Microsoft Store | [🛠️ Instalar](Instalar.md) · en Windows, crea el entorno con `py` |
| `Activate.ps1 no se puede cargar` | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` y repite |
| `Invalid URL` o `No api key` | Abre siempre con `python taller.py abrir …`, no con `opencode` a secas |
| El agente dice «No tengo acceso a tu correo» | Dile: «Son ficheros de esta carpeta, en correo/bandeja/. Léelos con tus herramientas» |
| He escrito `python taller.py …` dentro de opencode | Sal con `Ctrl+C` y escríbelo en la terminal |
| El agente dice «Listo», pero el comprobador dice ❌ | Manda el comprobador: vuelve a abrir opencode y pídele que lo arregle |
| No puedo instalar nada | [🆘 Plan B](Plan-B.md): Codespaces en el navegador, en pareja o «en seco» |
| Otra cosa | [🔧 Problemas y soluciones](Problemas.md) o pregunta al profesor |

## Enlaces

- Web del taller: <https://jlasherastracasa.github.io/taller_semana_ia_2026/>
- 🔑 Clave de clase: <https://jlasherastracasa.github.io/taller_semana_ia_2026/#/clave>
- 🛡️ Prueba de seguridad (obligatoria): [EJ 10 paso a paso](Prueba-de-seguridad.md)
- ⭐ Valora el taller (al final): <https://jlasherastracasa.github.io/taller_semana_ia_2026/#/valorar>
