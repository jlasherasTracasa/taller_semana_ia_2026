# 🟣 EJ 20 · Avisar cuando cambia una web

> 🗂️ **Documentos y tareas repetitivas** · 🟣 Avanzado · ⏱ 15 min · 🛠️ `opencode run` · Recomendado para: 💻

## 📌 La situación

Hay que enterarse cuando cambie una web (por ejemplo, la de convocatorias de ayudas). Preparando este taller, un agente dijo «Listo» sin haber hecho nada.

## 🎯 Objetivo

Un script que comprueba si una web ha cambiado y lo apunta en un log.

## 📦 Lo que tienes en esta carpeta

- Ninguno: el agente crea `vigila/`.

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar ej20
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Crea vigila/bin/vigila_cambios.sh: descarga https://example.com con curl, calcula su hash SHA-256, lo compara con el guardado en vigila/hash.txt y añade una línea con fecha a vigila/log/vigilancia.log (inicio, sin cambios o CAMBIO DETECTADO). Las rutas deben calcularse a partir de la ubicación del propio script, sin rutas absolutas, para que funcione se lance desde donde se lance. Ejecútalo dos veces y enséñame el log." | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- El log tiene dos líneas y el script funciona lanzado desde `/`.
- Sin rutas absolutas escritas a mano.

```bash
python3 taller.py comprobar ej20      # el agente no decide si está bien: lo decide el comprobador
```

## 🧪 Lo que pasó al validarlo (09-10-2026)

Script con rutas relativas a su ubicación; funciona lanzado desde `/`. En septiembre, con 30 tools extra de un MCP global, dijo «Listo» con un script vacío.

Prompt, salida real y ficheros: [`soluciones/ej20_vigilar_web/`](../../soluciones/ej20_vigilar_web/)

## 🔀 Siguiente paso

- **Programarlo para que se ejecute solo** → [🟣 EJ 21 · Programar una tarea periódica (con tu permiso)](../ej21_programar_cron/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
