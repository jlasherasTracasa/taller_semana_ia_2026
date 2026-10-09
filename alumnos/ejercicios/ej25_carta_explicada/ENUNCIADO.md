# 🟢 EJ 25 · Explícame esta carta

> 📬 **Puerta B · La estafeta** · 🟢 Fácil · ⏱ 15 min · 🛠️ `opencode run` · Recomendado para: 🧭 📚

## 📖 La escena

«REQUERIMIENTO PREVIO A LA VÍA DE APREMIO». Pilar se ha asustado. ¿Qué le piden, para cuándo, y qué pasa si no hace nada?

## 🎯 Objetivo

Que el agente explique un documento administrativo en lenguaje llano **sin inventar** lo que no dice.

## 📦 Lo que tienes en esta carpeta

- `carta.txt`: una carta de una entidad ficticia por dos recibos de agua.

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar ej25
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Lee carta.txt y escribe explicacion.md para una persona de 80 años: qué le piden, cuánto tiene que pagar, para qué día exactamente (cuenta los días hábiles sin sábados, domingos ni festivos, desde el día siguiente a la notificación), qué pasa si no hace nada (con el importe) y una lista de pasos. Si te pregunto algo que no está en la carta, como un teléfono o un horario, escribe «la carta no lo dice» en vez de inventarlo. Incluye al final un apartado ¿A qué teléfono llamo?" | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- Importe: **127,40 €**; si no paga, recargo del 20 % (**152,88 €** más intereses y costas).
- Plazo: **lunes 19/10/2026** (el 12 de octubre es festivo).
- En «¿A qué teléfono llamo?» pone que la carta no lo dice.

```bash
python3 taller.py comprobar ej25      # el agente no puede darte el sello: solo el comprobador
```

## 💡 Pistas

- Contar días hábiles con festivos es justo lo que los modelos hacen mal. Si falla, mira F.6.

## 🧪 Lo que pasó al validarlo (09-10-2026)

127,40 €, recargo del 20 % (152,88 €), plazo **lunes 19/10/2026** saltando el 12 de octubre, y «la carta no lo dice» para el teléfono.

Prompt, salida real y ficheros: [`soluciones/ej25_carta_explicada/`](../../soluciones/ej25_carta_explicada/)

## 🔀 ¿Y ahora qué?

- **Darle una calculadora de plazos** → [🟣 F.6 · Tu propia tool: plazos en días hábiles](../f6_tool_propia/ENUNCIADO.md)
- **El correo raro** → [🟢 EJ 10 · El correo envenenado](../ej10_inyeccion_prompt/ENUNCIADO.md)
- **Volver a la plaza** → [↩️ La plaza](../../AVENTURA.md#-la-plaza)
