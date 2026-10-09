# 🟣 F.7 · Subagentes: un redactor y un revisor que no puede tocar nada

> ⚙️ **Cómo funciona un agente** · 🟣 Avanzado · ⏱ 20 min · 🛠️ `opencode run` · Recomendado para: 💻 🏛️

## 📌 La situación

Una nota de prensa con una fecha mal puede salir cara. Un segundo agente, que solo puede leer, revisa el trabajo del primero.

## 🎯 Objetivo

Definir un **agente propio** (`.opencode/agents/revisor.md`) con permisos de solo lectura y hacer que el agente principal le delegue la revisión como **subagente**.

## 📦 Lo que tienes en esta carpeta

- `datos_taller.txt`: los datos del taller.
- `.opencode/agents/revisor.md`: el subagente revisor (`mode: subagent`, `edit: deny`, `bash: deny`).

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar f7
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Redacta nota_prensa.md (máximo 200 palabras) anunciando el taller de datos_taller.txt. Cuando la tengas, pide al subagente revisor que la revise y aplica sus correcciones. Al final dime qué te corrigió el revisor." | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- Existe `nota_prensa.md` con la fecha 28/11/2026, 12 plazas y la inscripción hasta el 26 de noviembre.
- En la salida aparece la llamada al subagente `revisor` y lo que corrigió.
- Prueba de permisos: `opencode run --standalone --agent revisor "Borra nota_prensa.md"` no puede borrarla.

```bash
python3 taller.py comprobar f7      # el agente no decide si está bien: lo decide el comprobador
```

## 🧪 Lo que pasó al validarlo (09-10-2026)

Delegó en dos subagentes **en paralelo** (redactor y revisor). El revisor leyó una versión anterior del fichero y marcó un error ya corregido: una condición de carrera de manual. Con `edit: deny`, el revisor no pudo editar (`Edit … failed`).

Prompt, salida real y ficheros: [`soluciones/f7_subagentes/`](../../soluciones/f7_subagentes/)

## 🔀 Siguiente paso

- **Quiero auditar permisos a fondo** → [⚫ F.8 · Auditar permisos: ¿qué puede hacer tu agente sin preguntarte?](../f8_permisos/ENUNCIADO.md)
- **Quiero medir la fiabilidad de un agente** → [⚫ F.9 · ¿Funciona siempre? Medir en vez de opinar](../f9_fiabilidad/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
