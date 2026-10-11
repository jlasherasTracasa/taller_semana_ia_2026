# ⚫ F.8 · Auditar permisos: ¿qué puede hacer tu agente sin preguntarte?

> ⚙️ **Cómo funciona un agente** · ⚫ Experto · ⏱ 25 min · 🛠️ opencode interactivo · Recomendado para: 🏛️

> ✋ **Práctica**: lo haces tú, a tu ritmo. Si te atascas, pregunta al profesor.

## 📌 La situación

Un compañero te pasa su configuración de opencode «que funciona de maravilla». Antes de usarla con tus ficheros, la auditas.

## 🎯 Objetivo

Encontrar los agujeros de una configuración real (orden de reglas, comodines, clave en claro, directorios externos) y dejarla segura **sin** dejar inservible al agente.

## 📦 Lo que tienes en esta carpeta

- `opencode_inseguro.json`: la configuración del compañero.
- `comandos_prueba.txt`: 17 órdenes con la decisión que deberían tener.
- `simular_permisos.py`: aplica la regla de opencode (**gana la última regla que coincide**).

## 💬 El encargo

**1.** Abre opencode en modo interactivo en tu carpeta de trabajo:

```bash
python taller.py abrir f8
```

**2.** Copia este encargo, pégalo en opencode y pulsa Enter:

```text
Audita opencode_inseguro.json. Escribe informe_permisos.md con cada agujero, por qué es peligroso y cómo se corrige (recuerda: en opencode gana la última regla que coincide). Crea opencode_seguro.json corregido, sin ninguna clave escrita (usa {env:LITELLM_API_KEY}), con external_directory en deny, y pruébalo con python simular_permisos.py opencode_seguro.json hasta que salgan 17/17.
```

**3.** Mira lo que hace: qué ficheros lee, qué órdenes ejecuta, si te pide permiso. Cuando termine, sal con `Ctrl+C` (o sigue conversando: «revisa que…», «corrige…»).

<details><summary>Sin conversar, de una vez (opcional)</summary>

```bash
python taller.py lanzar f8
```

O a mano, desde la carpeta de trabajo: `opencode run --standalone "…el encargo…"`.

</details>

> 💡 Antes de pegarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- `python simular_permisos.py opencode_seguro.json` da 17/17.
- `external_directory` en `deny` y ninguna `apiKey` escrita a mano.
- `informe_permisos.md` explica al menos el orden de reglas, `curl … | sh` y la clave en claro.

```bash
python taller.py comprobar f8      # el agente no decide si está bien: lo decide el comprobador
```

## 🧗 Reto extra

Piensa como atacante: ¿`python -c "import shutil; shutil.rmtree('x')"` lo para algún patrón? Conclusión: los patrones son un cinturón, no una jaula. Para aislar de verdad: contenedor o máquina virtual.

## 🧪 Lo que pasó al validarlo (09-10-2026)

Dejó `opencode_seguro.json` perfecto (17/17, `external_directory: deny`, sin claves) pero **no escribió `informe_permisos.md`** y terminó preguntando si quería que lo escribiera: hizo la parte que tenía comprobación y se saltó la que no.

Prompt, salida real y ficheros: [`soluciones/f8_permisos/`](../../soluciones/f8_permisos/)

## 🔀 Siguiente paso

- **La prueba de seguridad, en modo atacante** → [🟢 EJ 10 · Prueba de seguridad: correo con instrucciones ocultas](../ej10_inyeccion_prompt/ENUNCIADO.md)
- **Quiero medir la fiabilidad** → [⚫ F.9 · ¿Funciona siempre? Medir en vez de opinar](../f9_fiabilidad/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
