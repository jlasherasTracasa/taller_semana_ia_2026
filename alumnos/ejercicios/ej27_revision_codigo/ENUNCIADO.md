# 🟣 EJ 27 · Revisión de código de un cambio (pull request)

> ⚙️ **Cómo funciona un agente** · 🟣 Avanzado · ⏱ 20 min · 🛠️ `opencode run` · Recomendado para: 💻 🏛️

## 📌 La situación

Un compañero en prácticas pide mezclar hoy su cambio. Antes, una revisión de código como la haría alguien con experiencia.

## 🎯 Objetivo

Usar al agente como **revisor**: encontrar fallos de seguridad, regresiones y malas prácticas en un diff, con severidad y propuesta.

## 📦 Lo que tienes en esta carpeta

- `cambio.diff`: el cambio propuesto.
- `DESCRIPCION_PR.md`: lo que dice el autor.

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar ej27
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Revisa cambio.diff (y DESCRIPCION_PR.md) como un desarrollador senior. Escribe revision.md con cada problema ordenado por severidad (crítico, alto, medio, bajo): fichero y línea, qué pasa, por qué importa y cómo corregirlo con código. Termina con un veredicto: aprobar o pedir cambios. No modifiques cambio.diff ni ningún otro fichero existente: lo único que creas es revision.md." | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- Detecta la **inyección SQL** en la búsqueda y la **clave escrita en el código**.
- Detecta la **regresión de la cuota** (65 años ya no es jubilado) y los **tests borrados** para que pase.
- Señala el `except: pass` que oculta errores y el envío de teléfonos a un tercero (datos personales).
- Veredicto: **pedir cambios**.

```bash
python3 taller.py comprobar ej27      # el agente no decide si está bien: lo decide el comprobador
```

## 💡 Pistas

- Primera validación: con «No modifiques nada: solo revisa», el agente hizo la revisión en pantalla y **no creó `revision.md`**: entendió que tampoco podía escribir el informe. Distingue lo que no debe tocar de lo que tiene que entregar.

## 🧗 Reto extra

Pide después al agente que aplique sus propias correcciones en una rama y que los tests vuelvan a estar. ¿Se revisa bien a sí mismo?

## 🧪 Lo que pasó al validarlo (09-10-2026)

Encontró los seis problemas (inyección SQL, clave en el código, regresión de la cuota a los 65, tests borrados, `except: pass` y datos personales a un tercero) y pidió cambios. **En el primer intento**, con «No modifiques nada: solo revisa», hizo la revisión en pantalla y **no creó `revision.md`**.

Prompt, salida real y ficheros: [`soluciones/ej27_revision_codigo/`](../../soluciones/ej27_revision_codigo/)

## 🔀 Siguiente paso

- **Que un subagente revise siempre** → [🟣 F.7 · Subagentes: un redactor y un revisor que no puede tocar nada](../f7_subagentes/ENUNCIADO.md)
- **Tests primero** → [🟣 F.10 · Tests primero: el agente no puede hacer trampa](../f10_tests_primero/ENUNCIADO.md)
- **Auditar permisos del agente** → [⚫ F.8 · Auditar permisos: ¿qué puede hacer tu agente sin preguntarte?](../f8_permisos/ENUNCIADO.md)
