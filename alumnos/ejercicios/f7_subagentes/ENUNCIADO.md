# 🟣 F.7 · Subagentes: un redactor y un revisor que no puede tocar nada

> ⚙️ **Cómo funciona un agente** · 🟣 Avanzado · ⏱ 20 min · 🛠️ opencode interactivo · Recomendado para: 💻 🏛️

> ✋ **Práctica**: lo haces tú, a tu ritmo. Si te atascas, pregunta al profesor.

## 📌 La situación

Una nota de prensa con una fecha mal puede salir cara. Un segundo agente, que solo puede leer, revisa el trabajo del primero.

## 🎯 Objetivo

Definir un **agente propio** (`.opencode/agents/revisor.md`) con permisos de solo lectura y hacer que el agente principal le delegue la revisión como **subagente**.

## 📦 Lo que tienes en esta carpeta

- `datos_taller.txt`: los datos del taller.
- `.opencode/agents/revisor.md`: el subagente revisor (`mode: subagent`, `edit: deny`, `bash: deny`).

## 💬 El encargo

**1.** Abre opencode en modo interactivo en tu carpeta de trabajo:

```bash
python taller.py abrir f7
```

**2.** Copia este encargo, pégalo en opencode y pulsa Enter:

```text
Redacta nota_prensa.md (máximo 200 palabras) anunciando el taller de datos_taller.txt. Cuando la tengas, pide al subagente revisor que la revise y aplica sus correcciones. Al final dime qué te corrigió el revisor.
```

**3.** Mira lo que hace: qué ficheros lee, qué órdenes ejecuta, si te pide permiso. Cuando termine, sal con `Ctrl+C` (o sigue conversando: «revisa que…», «corrige…»).

<details><summary>Sin conversar, de una vez (opcional)</summary>

```bash
python taller.py lanzar f7
```

O a mano, desde la carpeta de trabajo: `opencode run --standalone "…el encargo…"`.

</details>

> 💡 Antes de pegarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- Existe `nota_prensa.md` con la fecha 28/11/2026, 12 plazas y la inscripción hasta el 26 de noviembre.
- En la salida aparece la llamada al subagente `revisor` y lo que corrigió.
- Prueba de permisos: `opencode run --standalone --agent revisor "Borra nota_prensa.md"` no puede borrarla.

```bash
python taller.py comprobar f7      # el agente no decide si está bien: lo decide el comprobador
```

## 📂 Una solución de ejemplo

¿Te has atascado o no puedes ejecutarlo? Mira lo que hizo el agente con este encargo (el encargo, lo que escribió en pantalla y los ficheros): [`soluciones/f7_subagentes/`](../../soluciones/f7_subagentes/)

## 🔀 Siguiente paso

- **Quiero auditar permisos a fondo** → [⚫ F.8 · Auditar permisos: ¿qué puede hacer tu agente sin preguntarte?](../f8_permisos/ENUNCIADO.md)
- **Quiero medir la fiabilidad de un agente** → [⚫ F.9 · ¿Funciona siempre? Medir en vez de opinar](../f9_fiabilidad/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
