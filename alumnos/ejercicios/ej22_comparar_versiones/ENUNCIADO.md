# 🔵 EJ 22 · Qué ha cambiado entre dos versiones de un documento

> 🗂️ **Documentos y tareas repetitivas** · 🔵 Medio · ⏱ 15 min · 🛠️ `opencode run` · Recomendado para: 📚

## 📌 La situación

La memoria anual de una asociación tiene dos versiones y la junta solo quiere saber qué ha cambiado, con las cifras.

## 🎯 Objetivo

Explicar en prosa las diferencias entre dos documentos Word, con las cifras viejas y nuevas.

## 📦 Lo que tienes en esta carpeta

- `informe_v1.docx` e `informe_v2.docx`.

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar ej22
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Lee informe_v1.docx e informe_v2.docx con python-docx, compara su texto y escribe cambios.md: un resumen en prosa, para alguien que no ha visto los documentos, de lo añadido, lo eliminado y lo modificado, con las cifras viejas y nuevas." | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- `cambios.md` en prosa que menciona talleres, socios y remanente con las cifras de ambas versiones.

```bash
python3 taller.py comprobar ej22      # el agente no decide si está bien: lo decide el comprobador
```

## 🧪 Lo que pasó al validarlo (09-10-2026)

Resumen en prosa con talleres, socios y remanente y las cifras de ambas versiones.

Prompt, salida real y ficheros: [`soluciones/ej22_comparar_versiones/`](../../soluciones/ej22_comparar_versiones/)

## 🔀 Siguiente paso

- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
