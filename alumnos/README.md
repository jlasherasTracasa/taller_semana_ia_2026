# :robot: Kit del alumno · Agentes de IA para el trabajo de cada día

**Semana de la IA 2026 · Universidad Pública de Navarra · 23 de octubre de 2026**
Cátedra de Ciencias de la Computación e Inteligencia Artificial (UPNA–Tracasa)

Este kit es todo lo que necesitas para hacer el taller y repetirlo en casa: la presentación, la guía, los datos de
partida de cada ejercicio y sus soluciones reales. **Todo funciona sin GPU.**

## :package: Qué hay

| Archivo o carpeta | Qué es |
|---|---|
| `taller-agentes-ia.pptx` | La presentación, con notas y glosario. |
| `guia_alumno.md` | **Empieza aquí.** Conceptos (agente, ReAct, tools, permisos, skills, MCP) y los 26 ejercicios. |
| `ejercicios/<nombre>/` | Enunciado (`ENUNCIADO.md`) y datos de partida, sin solución. |
| `soluciones/<nombre>/` | Prompt exacto, salida real, ficheros generados y un `SOLUCION.md` comentado. |
| `replicar_paper/` | Reto avanzado: replicar un paper de IA en CPU (con el PDF original). |
| `opencode.json` | Configuración de opencode: proveedor y **permisos**. No contiene claves. |
| `.env.example` | Plantilla para tus claves (cópiala a `.env`). |
| `comprobar_entorno.sh` | Comprueba que tu equipo está listo. |

## :rocket: Puesta en marcha (5 minutos)

1. Instala Node.js 18+ y opencode: `npm i -g opencode-ai` y `opencode --version`.
2. Copia `.env.example` a `.env` y escribe la URL y la clave que te dé el profesor. **Nunca subas `.env` a git.**
3. Carga las variables en cada terminal: `set -a; . ./.env; set +a`
   (PowerShell: `Get-Content .env | ForEach-Object { $n,$v = $_ -split '=',2; Set-Item "env:$n" $v }`).
4. Comprueba: `bash comprobar_entorno.sh` y
   `opencode run --model vllm/GLM-5.3-Flash "Di exactamente: listo para el taller"`.

## :test_tube: Cómo hacer un ejercicio

```bash
cp -r ejercicios/ej01_pagina_personal ~/taller/ej01 && cp opencode.json ~/taller/ej01/
cd ~/taller/ej01
cat ENUNCIADO.md                       # objetivo, prompt sugerido y criterio de éxito
opencode run --model vllm/GLM-5.3-Flash "…el prompt del enunciado…"
```

Después **comprueba tú el criterio de éxito** y compara con `soluciones/ej01_pagina_personal/`. Las respuestas del
modelo cambian entre ejecuciones: lo que debe cumplirse es el criterio, no el texto exacto.

## :world_map: Los 26 ejercicios

| Bloque | Ejercicios | En clase |
|---|---|---|
| **F · Por dentro** | `f0_react_bucle` (el bucle ReAct en 70 líneas), `f1_function_calling`, `f2_comando_skill`, `f3_mcp` | F.0 y F.1 |
| **A · Web** | `ej01` página personal · `ej02` agenda desde CSV · `ej03` formulario → JSON · `ej04` GitHub Pages · `ej05` auditoría de accesibilidad | 01, 02 |
| **B · Correo** | `ej06` resumen diario · `ej07` tareas a CSV · `ej08` borrador · `ej09` evento `.ics` · `ej10` **inyección de prompt** | 06, 07, 08, 10 |
| **C · Presentaciones** | `ej11` informe → pptx · `ej12` CSV → pptx con gráfico · `ej13` revisión de estilo · `ej14` traducir un deck | 11, 12 |
| **D · Rutinas** | `ej15` ordenar descargas · `ej16` informe semanal · `ej17` resumir PDF · `ej18` facturas → Excel · `ej19` certificados PDF · `ej20` vigilar una web · `ej21` programarla · `ej22` comparar versiones | 15, 16 |
| **Reto** | `replicar_paper/` (≈ 6 min en CPU; descarga ≈ 1,6 GB de modelos la primera vez) | en casa |

Los 26 se validaron ejecutándolos de verdad el 28-09-2026 con este mismo kit. Sus tropiezos también están
documentados, porque enseñan tanto como los aciertos: el agente que mató un proceso ajeno (EJ 03), el que dijo
«Listo» sin haber hecho nada (EJ 20) o el que cuenta mal líneas que acaba de leer (F.0).

## :shield: Reglas de oro

1. Claves solo en variables de entorno (`{env:…}`), nunca en ficheros que se compartan.
2. Lo que el agente lee (correos, webs, documentos) es **dato**, nunca **instrucción**.
3. Trabaja en copias y con los permisos del kit: se permite lo habitual, se prohíbe lo irreversible (`kill`,
   `rm -rf`, `sudo`) y se pide permiso para lo que sale de tu máquina (`git push`, `crontab`, `systemctl`).
4. «He terminado» no es una prueba: comprueba el resultado.
5. Tú encargas y revisas; el agente ejecuta. Firma quien encarga.
