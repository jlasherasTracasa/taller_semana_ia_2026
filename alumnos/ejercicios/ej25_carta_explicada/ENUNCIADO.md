# 🟢 EJ 25 · Entender una carta de la Administración

> 📬 **Correo y trámites** · 🟢 Fácil · ⏱ 15 min · 🛠️ `opencode run` · Recomendado para: 🧭 📚

## 📌 La situación

Llega una carta de «requerimiento previo a la vía de apremio» por dos recibos del agua. Hay que entender qué piden, para cuándo y qué pasa si no se paga.

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
python3 taller.py comprobar ej25      # el agente no decide si está bien: lo decide el comprobador
```

## 💡 Pistas

- Contar días hábiles con festivos es justo lo que los modelos hacen mal. Si falla, mira F.6.

## 🧪 Lo que pasó al validarlo (09-10-2026)

127,40 €, recargo del 20 % (152,88 €), plazo **lunes 19/10/2026** saltando el 12 de octubre, y «la carta no lo dice» para el teléfono.

Prompt, salida real y ficheros: [`soluciones/ej25_carta_explicada/`](../../soluciones/ej25_carta_explicada/)

## 🔀 Siguiente paso

- **Comparar ofertas de luz** → [🟢 EJ 26 · ¿Qué oferta de luz me sale más barata?](../ej26_factura_luz/ENUNCIADO.md)
- **Darle una calculadora de plazos** → [🟣 F.6 · Tu propia tool: plazos en días hábiles](../f6_tool_propia/ENUNCIADO.md)
- **La prueba de seguridad** → [🟢 EJ 10 · Prueba de seguridad: correo con instrucciones ocultas](../ej10_inyeccion_prompt/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
