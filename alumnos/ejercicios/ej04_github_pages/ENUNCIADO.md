# 🔵 EJ 04 · Publicar una web en GitHub Pages (sin darle tus credenciales)

> 🌐 **Webs** · 🔵 Medio · ⏱ 20 min · 🛠️ opencode interactivo · Recomendado para: 📚 💻

> ✋ **Práctica**: lo haces tú, a tu ritmo. Si te atascas, pregunta al profesor.

## 📌 La situación

La web ya está hecha y hay que publicarla gratis. El agente prepara todo; el último paso, con tus credenciales, lo das tú.

## 🎯 Objetivo

Preparar el repositorio y una guía de publicación; el `git push` y la URL los haces tú.

## 📦 Lo que tienes en esta carpeta

- `index.html`: la página que vas a publicar.

## 💬 El encargo

**1.** Abre opencode en modo interactivo en tu carpeta de trabajo:

```bash
python taller.py abrir ej04
```

**2.** Copia este encargo, pégalo en opencode y pulsa Enter:

```text
Voy a publicar index.html en GitHub Pages. Inicializa aquí un repositorio git con un primer commit, escribe un README.md breve y PASOS.md con los pasos numerados para crear el repositorio en GitHub, activar Pages y subir los cambios. Todo en castellano. NO hagas git push ni pidas credenciales: ese paso lo haré yo.
```

**3.** Mira lo que hace: qué ficheros lee, qué órdenes ejecuta, si te pide permiso. Cuando termine, sal con `Ctrl+C` (o sigue conversando: «revisa que…», «corrige…»).

<details><summary>Sin conversar, de una vez (opcional)</summary>

```bash
python taller.py lanzar ej04
```

O a mano, desde la carpeta de trabajo: `opencode run --standalone "…el encargo…"`.

</details>

> 💡 Antes de pegarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- Hay repositorio git local con un commit, `README.md` y `PASOS.md` en castellano.
- El agente no ha hecho `push` ni ha pedido tokens. La URL pública la compruebas tú.

```bash
python taller.py comprobar ej04      # el agente no decide si está bien: lo decide el comprobador
```

## 💡 Pistas

- Usa un token de GitHub con permisos mínimos y caducidad corta. Nunca lo pegues en un chat.

## 🧪 Lo que pasó al validarlo (09-10-2026)

Repositorio con commit, `README.md` y `PASOS.md` en castellano, sin `push` ni credenciales. En septiembre, sin «todo en castellano», respondió en inglés.

Prompt, salida real y ficheros: [`soluciones/ej04_github_pages/`](../../soluciones/ej04_github_pages/)

## 🔀 Siguiente paso

- **¿Es accesible?** → [🔵 EJ 05 · Auditoría de accesibilidad de una web](../ej05_auditoria_web/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
