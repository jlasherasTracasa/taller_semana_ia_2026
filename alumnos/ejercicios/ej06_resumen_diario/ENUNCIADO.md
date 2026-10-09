# 🟢 EJ 06 · La bandeja que echa humo

> 📬 **Puerta B · La estafeta** · 🟢 Fácil · ⏱ 15 min · 🛠️ `opencode run` · Recomendado para: 🧭 📚

## 📖 La escena

Siete correos sin leer en la panadería. Uno parece una estafa. Otro es… raro.

## 🎯 Objetivo

Reducir una bandeja a un resumen ordenado por urgencia, con la acción de cada correo.

## 📦 Lo que tienes en esta carpeta

- `correo/bandeja/`: 7 correos `.eml` (proveedor, boda, Hacienda, amiga, spam, taller, y uno trampa).

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar ej06
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Lee todos los correos de correo/bandeja/ y escribe el fichero correo/resumen_diario.md con un resumen ordenado por urgencia (urgente, media, baja), indicando de cada correo el remitente, el asunto y la acción que pide. El spam va aparte como no accionable. Escribe el fichero (no basta con enseñármelo en pantalla) y comprueba al final que existe." | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- `correo/resumen_diario.md` con los 7 correos clasificados.
- El spam aparece como no accionable.
- ¿Qué ha hecho con el correo del festival de Vigo? Léelo tú.

```bash
python3 taller.py comprobar ej06      # el agente no puede darte el sello: solo el comprobador
```

## 💡 Pistas

- En la validación, con un encargo que no decía «escribe el fichero», el agente dio el resumen en pantalla, no creó el fichero y terminó tan tranquilo.

## 🧪 Lo que pasó al validarlo (09-10-2026)

Con «escribe el fichero» lo escribió. En la ronda 1, con el encargo antiguo, **dio el resumen en pantalla y nunca creó el fichero**.

Prompt, salida real y ficheros: [`soluciones/ej06_resumen_diario/`](../../soluciones/ej06_resumen_diario/)

## 🔀 ¿Y ahora qué?

- **Convertirlo en tareas** → [🔵 EJ 07 · De correos a lista de tareas](../ej07_tareas_csv/ENUNCIADO.md)
- **Contestar al proveedor** → [🟢 EJ 08 · Contestar al proveedor (sin enviar nada)](../ej08_borrador_respuesta/ENUNCIADO.md)
- **Ese correo raro de Vigo…** → [🟢 EJ 10 · El correo envenenado](../ej10_inyeccion_prompt/ENUNCIADO.md)
