# 🔵 F.4 · Skills: recetas que el agente carga cuando las necesita

> ⚙️ **Cómo funciona un agente** · 🔵 Medio · ⏱ 20 min · 🛠️ opencode interactivo · Recomendado para: 📚 💻

> 🎥 **Demo en directo**: lo hace el profesor en el proyector; tú lo miras y lo repites después si quieres.

## 📌 La situación

Una asociación de vecinos necesita el acta de cada reunión con el formato exacto que pide el registro de asociaciones.

## 🎯 Objetivo

Ver cómo el agente **descubre** una skill por su descripción, la **carga solo cuando la necesita** y sigue sus instrucciones y scripts (aquí, un validador).

## 📦 Lo que tienes en esta carpeta

- `transcripcion_reunion.txt`: la transcripción de la junta.
- `.opencode/skills/acta-reunion/SKILL.md`: la receta (formato del acta) y `validar_acta.py`, su script.

## 💬 El encargo

**1.** Abre opencode en modo interactivo en tu carpeta de trabajo:

```bash
python taller.py abrir f4
```

**2.** Copia este encargo, pégalo en opencode y pulsa Enter:

```text
Haz el acta de la reunión de transcripcion_reunion.txt.
```

**3.** Mira lo que hace: qué ficheros lee, qué órdenes ejecuta, si te pide permiso. Cuando termine, sal con `Ctrl+C` (o sigue conversando: «revisa que…», «corrige…»).

<details><summary>Sin conversar, de una vez (opcional)</summary>

```bash
python taller.py lanzar f4
```

O a mano, desde la carpeta de trabajo: `opencode run --standalone "…el encargo…"`.

</details>

> 💡 Antes de pegarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- Existe `actas/2026-10-15_acta.md` y `python .opencode/skills/acta-reunion/validar_acta.py` dice `ACTA VÁLIDA`.
- La tabla de acuerdos tiene al menos 4 filas (txaranga, presupuesto, mancomunidad, cartel, cuota).
- En la salida verás que el agente llamó a la tool `skill`: fíjate en que el encargo **no** la nombraba.

```bash
python taller.py comprobar f4      # el agente no decide si está bien: lo decide el comprobador
```

## 🧗 Reto extra

Crea tu propia skill en `.opencode/skills/<nombre>/SKILL.md` (por ejemplo, «ficha-receta» o «parte-de-incidencias») y comprueba que se activa con un encargo que no la menciona.

## 📂 Una solución de ejemplo

¿Te has atascado o no puedes ejecutarlo? Mira lo que hizo el agente con este encargo (el encargo, lo que escribió en pantalla y los ficheros): [`soluciones/f4_skills/`](../../soluciones/f4_skills/)

## 🔀 Siguiente paso

- **Quiero darle una herramienta nueva, no una receta** → [🟣 F.6 · Tu propia tool: plazos en días hábiles](../f6_tool_propia/ENUNCIADO.md)
- **Quiero que un segundo agente revise el trabajo** → [🟣 F.7 · Subagentes: un redactor y un revisor que no puede tocar nada](../f7_subagentes/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
