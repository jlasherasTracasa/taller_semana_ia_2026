# 🔵 EJ 02 · Agenda de actos a partir de una hoja de cálculo

> 🌐 **Webs** · 🔵 Medio · ⏱ 15 min · 🛠️ opencode interactivo · Recomendado para: 📚

> ✋ **Práctica**: lo haces tú, a tu ritmo. Si te atascas, pregunta al profesor.

## 📌 La situación

La comisión de fiestas tiene el programa en una hoja de cálculo y quiere publicarlo en una página que se lea bien en el móvil.

## 🎯 Objetivo

Convertir una tabla (CSV) en una página de agenda agrupada por franjas.

## 📦 Lo que tienes en esta carpeta

- `programa.csv`: hora, título, lugar y tipo de cada acto.

## 💬 El encargo

**1.** Abre opencode en modo interactivo en tu carpeta de trabajo:

```bash
python taller.py abrir ej02
```

**2.** Copia este encargo, pégalo en opencode y pulsa Enter:

```text
Lee programa.csv y crea agenda.html: una sola columna, agrupada en Mañana y Tarde, diseño festivo, adaptada al móvil y sin dependencias externas. Incluye TODOS los actos del CSV y comprueba al final, contándolos, que no falta ninguno.
```

**3.** Mira lo que hace: qué ficheros lee, qué órdenes ejecuta, si te pide permiso. Cuando termine, sal con `Ctrl+C` (o sigue conversando: «revisa que…», «corrige…»).

<details><summary>Sin conversar, de una vez (opcional)</summary>

```bash
python taller.py lanzar ej02
```

O a mano, desde la carpeta de trabajo: `opencode run --standalone "…el encargo…"`.

</details>

> 💡 Antes de pegarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- `agenda.html` con todos los actos del CSV, agrupados en mañana y tarde.
- Sin dependencias externas.

```bash
python taller.py comprobar ej02      # el agente no decide si está bien: lo decide el comprobador
```

## 🧪 Lo que pasó al validarlo (09-10-2026)

Los 6 actos, agrupados en mañana y tarde, y los contó al final.

Prompt, salida real y ficheros: [`soluciones/ej02_agenda_csv/`](../../soluciones/ej02_agenda_csv/)

## 🔀 Siguiente paso

- **Ahora, que la gente pueda apuntarse** → [🟣 EJ 03 · Formulario web que guarda los envíos (sin matar procesos ajenos)](../ej03_formulario_json/ENUNCIADO.md)
- **Publicarla** → [🔵 EJ 04 · Publicar una web en GitHub Pages (sin darle tus credenciales)](../ej04_github_pages/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
