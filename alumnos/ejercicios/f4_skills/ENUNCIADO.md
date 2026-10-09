# 🔵 F.4 · Skills: recetas que el agente carga cuando las necesita

> ⚙️ **Puerta F · La sala de máquinas** · 🔵 Medio · ⏱ 20 min · 🛠️ `opencode run` · Recomendado para: 📚 💻

## 📖 La escena

La asociación de vecinos necesita el acta de la reunión con el formato exacto del registro. Hay una receta para eso.

## 🎯 Objetivo

Ver cómo el agente **descubre** una skill por su descripción, la **carga solo cuando la necesita** y sigue sus instrucciones y scripts (aquí, un validador).

## 📦 Lo que tienes en esta carpeta

- `transcripcion_reunion.txt`: la transcripción de la junta.
- `.opencode/skills/acta-reunion/SKILL.md`: la receta (formato del acta) y `validar_acta.py`, su script.

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar f4
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Haz el acta de la reunión de transcripcion_reunion.txt." | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- Existe `actas/2026-10-15_acta.md` y `python3 .opencode/skills/acta-reunion/validar_acta.py` dice `ACTA VÁLIDA`.
- La tabla de acuerdos tiene al menos 4 filas (txaranga, presupuesto, mancomunidad, cartel, cuota).
- En la salida verás que el agente llamó a la tool `skill`: fíjate en que el encargo **no** la nombraba.

```bash
python3 taller.py comprobar f4      # el agente no puede darte el sello: solo el comprobador
```

## 🧗 Reto extra

Crea tu propia skill en `.opencode/skills/<nombre>/SKILL.md` (por ejemplo, «ficha-receta» o «parte-de-incidencias») y comprueba que se activa con un encargo que no la menciona.

## 🔀 ¿Y ahora qué?

- **Quiero darle una herramienta nueva, no una receta** → [🟣 F.6 · Tu propia tool: plazos en días hábiles](../f6_tool_propia/ENUNCIADO.md)
- **Quiero que un segundo agente revise el trabajo** → [🟣 F.7 · Subagentes: un redactor y un revisor que no puede tocar nada](../f7_subagentes/ENUNCIADO.md)
- **Volver a la plaza** → [↩️ La plaza](../../AVENTURA.md#-la-plaza)
