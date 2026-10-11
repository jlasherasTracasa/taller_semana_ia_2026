# 🟢 EJ 25 · Entender una carta de la Administración

> 📬 **Correo y trámites** · 🟢 Fácil · ⏱ 15 min · 🛠️ opencode interactivo · Recomendado para: 🧭 📚

> ✋ **Práctica**: lo haces tú, a tu ritmo. Si te atascas, pregunta al profesor.

## 📌 La situación

Llega una carta de «requerimiento previo a la vía de apremio» por dos recibos del agua. Hay que entender qué piden, para cuándo y qué pasa si no se paga.

## 🎯 Objetivo

Que el agente explique un documento administrativo en lenguaje llano **sin inventar** lo que no dice.

## 📦 Lo que tienes en esta carpeta

- `carta.txt`: una carta de una entidad ficticia por dos recibos de agua.

## 💬 El encargo

**1.** Abre opencode en modo interactivo en tu carpeta de trabajo:

```bash
python taller.py abrir ej25
```

**2.** Copia este encargo, pégalo en opencode y pulsa Enter:

```text
Lee carta.txt y escribe explicacion.md para una persona de 80 años, en lenguaje llano, con estos seis apartados y en este orden: 1) ¿Qué me piden? 2) ¿Cuánto tengo que pagar? 3) ¿Hasta qué día tengo? (cuenta los días hábiles sin sábados, domingos ni festivos, desde el día siguiente a la notificación, y di la fecha exacta) 4) ¿Qué pasa si no hago nada? (con el importe) 5) Pasos que tengo que dar, en una lista 6) ¿A qué teléfono llamo? Si algo no está en la carta, como un teléfono o un horario, escribe «la carta no lo dice» en vez de inventarlo. Al final comprueba que están los seis apartados.
```

**3.** Mira lo que hace: qué ficheros lee, qué órdenes ejecuta, si te pide permiso. Cuando termine, sal con `Ctrl+C` (o sigue conversando: «revisa que…», «corrige…»).

<details><summary>Sin conversar, de una vez (opcional)</summary>

```bash
python taller.py lanzar ej25
```

O a mano, desde la carpeta de trabajo: `opencode run --standalone "…el encargo…"`.

</details>

> 💡 Antes de pegarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- Importe: **127,40 €**; si no paga, recargo del 20 % (**152,88 €** más intereses y costas).
- Plazo: **lunes 19/10/2026** (el 12 de octubre es festivo).
- En «¿A qué teléfono llamo?» pone que la carta no lo dice.

```bash
python taller.py comprobar ej25      # el agente no decide si está bien: lo decide el comprobador
```

## 💡 Pistas

- Contar días hábiles con festivos es justo lo que los modelos hacen mal. Si falla, mira F.6.

## 🧪 Lo que pasó al validarlo (11-10-2026)

GLM se saltó dos veces el apartado del teléfono (aunque decía bien que la carta no lo da). Con los seis apartados numerados: 127,40 €, recargo hasta 152,88 €, plazo lunes 19/10 (salta el 12) y «la carta no lo dice».

Con el modelo gratuito de opencode (`big-pickle`): ✅ cumple el criterio.

Prompt, salida real y ficheros: [`soluciones/ej25_carta_explicada/`](../../soluciones/ej25_carta_explicada/)

## 🔀 Siguiente paso

- **Comparar ofertas de luz** → [🟢 EJ 26 · ¿Qué oferta de luz me sale más barata?](../ej26_factura_luz/ENUNCIADO.md)
- **Darle una calculadora de plazos** → [🟣 F.6 · Tu propia tool: plazos en días hábiles](../f6_tool_propia/ENUNCIADO.md)
- **La prueba de seguridad** → [🟢 EJ 10 · Prueba de seguridad: correo con instrucciones ocultas](../ej10_inyeccion_prompt/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
