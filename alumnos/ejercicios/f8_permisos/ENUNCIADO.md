# ⚫ F.8 · Auditar permisos: ¿qué puede hacer tu agente sin preguntarte?

> ⚙️ **Puerta F · La sala de máquinas** · ⚫ Experto · ⏱ 25 min · 🛠️ `opencode run` · Recomendado para: 🏛️

## 📖 La escena

Un compañero comparte su `opencode.json` «que funciona de maravilla». Antes de usarlo, lo auditas.

## 🎯 Objetivo

Encontrar los agujeros de una configuración real (orden de reglas, comodines, clave en claro, directorios externos) y dejarla segura **sin** dejar inservible al agente.

## 📦 Lo que tienes en esta carpeta

- `opencode_inseguro.json`: la configuración del compañero.
- `comandos_prueba.txt`: 17 órdenes con la decisión que deberían tener.
- `simular_permisos.py`: aplica la regla de opencode (**gana la última regla que coincide**).

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar f8
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Audita opencode_inseguro.json. Escribe informe_permisos.md con cada agujero, por qué es peligroso y cómo se corrige (recuerda: en opencode gana la última regla que coincide). Crea opencode_seguro.json corregido, sin ninguna clave escrita (usa {env:LITELLM_API_KEY}), con external_directory en deny, y pruébalo con python3 simular_permisos.py opencode_seguro.json hasta que salgan 17/17." | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- `python3 simular_permisos.py opencode_seguro.json` da 17/17.
- `external_directory` en `deny` y ninguna `apiKey` escrita a mano.
- `informe_permisos.md` explica al menos el orden de reglas, `curl … | sh` y la clave en claro.

```bash
python3 taller.py comprobar f8      # el agente no puede darte el sello: solo el comprobador
```

## 🧗 Reto extra

Piensa como atacante: ¿`python3 -c "import shutil; shutil.rmtree('x')"` lo para algún patrón? Conclusión: los patrones son un cinturón, no una jaula. Para aislar de verdad: contenedor o máquina virtual.

## 🔀 ¿Y ahora qué?

- **A por el correo envenenado, en modo atacante** → [🟢 EJ 10 · El correo envenenado](../ej10_inyeccion_prompt/ENUNCIADO.md)
- **Quiero medir la fiabilidad** → [⚫ F.9 · ¿Funciona siempre? Medir en vez de opinar](../f9_fiabilidad/ENUNCIADO.md)
- **Volver a la plaza** → [↩️ La plaza](../../AVENTURA.md#-la-plaza)
