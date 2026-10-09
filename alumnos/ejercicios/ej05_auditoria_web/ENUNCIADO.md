# 🔵 EJ 05 · Auditoría de accesibilidad de una web

> 🌐 **Webs** · 🔵 Medio · ⏱ 20 min · 🛠️ `opencode run` · Recomendado para: 📚

## 📌 La situación

La web de un centro de mayores tiene letra pequeña y poco contraste: sus usuarios no la pueden leer. Hay que auditarla y corregirla.

## 🎯 Objetivo

Detectar y corregir fallos de accesibilidad y adaptación al móvil de una página real.

## 📦 Lo que tienes en esta carpeta

- `web_centro_mayores.html`: la página original.

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar ej05
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Audita web_centro_mayores.html: contraste de color, tamaño de letra, adaptación al móvil, atributo lang, textos alternativos de las imágenes y navegación con teclado. Escribe incidencias.md con una lista de cada fallo y su corrección, y guarda la página corregida como web_corregida.html sin tocar el original. No me hagas preguntas: si algo es ambiguo, decide tú y explícalo en incidencias.md." | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- `incidencias.md` con cada fallo y su corrección.
- `web_corregida.html` con `lang="es"`, letra de 14 px o más, media queries y `alt` en todas las imágenes.
- El original sigue intacto.

```bash
python3 taller.py comprobar ej05      # el agente no decide si está bien: lo decide el comprobador
```

## 🧪 Lo que pasó al validarlo (09-10-2026)

Con `question: deny` y «no me hagas preguntas», escribió `incidencias.md` y la página corregida. En la ronda 1 (opencode 2 sin ese permiso) **se paró a preguntar** y, en modo `run`, falló.

Prompt, salida real y ficheros: [`soluciones/ej05_auditoria_web/`](../../soluciones/ej05_auditoria_web/)

## 🔀 Siguiente paso

- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
- **Área de correo y trámites** → [🟢 EJ 06 · Resumen diario de la bandeja de entrada](../ej06_resumen_diario/ENUNCIADO.md)
