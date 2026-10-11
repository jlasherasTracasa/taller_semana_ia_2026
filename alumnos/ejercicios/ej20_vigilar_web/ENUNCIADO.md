# 🟣 EJ 20 · Avisar cuando cambia una web

> 🗂️ **Documentos y tareas repetitivas** · 🟣 Avanzado · ⏱ 15 min · 🛠️ opencode interactivo · Recomendado para: 💻

> ✋ **Práctica**: lo haces tú, a tu ritmo. Si te atascas, pregunta al profesor.

## 📌 La situación

Hay que enterarse cuando cambie una web (por ejemplo, la de convocatorias de ayudas). Preparando este taller, un agente dijo «Listo» sin haber hecho nada.

## 🎯 Objetivo

Un script que comprueba si una web ha cambiado y lo apunta en un log.

## 📦 Lo que tienes en esta carpeta

- Ninguno: el agente crea `vigila/`.

## 💬 El encargo

**1.** Abre opencode en modo interactivo en tu carpeta de trabajo:

```bash
python taller.py abrir ej20
```

**2.** Copia este encargo, pégalo en opencode y pulsa Enter:

```text
Crea vigila/vigila_cambios.py, en Python y solo con la biblioteca estándar: descarga https://example.com, calcula su hash SHA-256, lo compara con el guardado en vigila/hash.txt y añade una línea con fecha y hora a vigila/log/vigilancia.log (inicio, sin cambios o CAMBIO DETECTADO). Las rutas deben calcularse a partir de la ubicación del propio script, sin rutas absolutas, para que funcione se lance desde donde se lance y en cualquier sistema. Ejecútalo dos veces y enséñame el log.
```

**3.** Mira lo que hace: qué ficheros lee, qué órdenes ejecuta, si te pide permiso. Cuando termine, sal con `Ctrl+C` (o sigue conversando: «revisa que…», «corrige…»).

<details><summary>Sin conversar, de una vez (opcional)</summary>

```bash
python taller.py lanzar ej20
```

O a mano, desde la carpeta de trabajo: `opencode run --standalone "…el encargo…"`.

</details>

> 💡 Antes de pegarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- El log tiene dos líneas y el script funciona lanzado desde la raíz del disco (`/` o `C:\`).
- Sin rutas absolutas escritas a mano.

```bash
python taller.py comprobar ej20      # el agente no decide si está bien: lo decide el comprobador
```

## 🧪 Lo que pasó al validarlo (09-10-2026)

Script con rutas relativas a su ubicación; funciona lanzado desde `/`. En septiembre, con 30 tools extra de un MCP global, dijo «Listo» con un script vacío.

Prompt, salida real y ficheros: [`soluciones/ej20_vigilar_web/`](../../soluciones/ej20_vigilar_web/)

## 🔀 Siguiente paso

- **Programarlo para que se ejecute solo** → [🟣 EJ 21 · Programar una tarea periódica (con tu permiso)](../ej21_programar_cron/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
