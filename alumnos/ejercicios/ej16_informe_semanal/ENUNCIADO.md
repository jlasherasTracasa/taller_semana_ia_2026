# 🔵 EJ 16 · Informe semanal que se recalcula solo

> 📊 **Informes y presentaciones** · 🔵 Medio · ⏱ 15 min · 🛠️ opencode interactivo · Recomendado para: 📚

> ✋ **Práctica**: lo haces tú, a tu ritmo. Si te atascas, pregunta al profesor.

## 📌 La situación

El informe de ventas se repite cada semana con datos nuevos. Mejor un script que lo recalcule que un texto que hay que rehacer.

## 🎯 Objetivo

Un informe de texto generado por un script que lee el CSV, para que sirva la semana que viene.

## 📦 Lo que tienes en esta carpeta

- `ventas_tienda.csv`.

## 💬 El encargo

**1.** Abre opencode en modo interactivo en tu carpeta de trabajo:

```bash
python taller.py abrir ej16
```

**2.** Copia este encargo, pégalo en opencode y pulsa Enter:

```text
Lee ventas_tienda.csv y escribe un script informe.py que genere informe_semanal.txt con el total por categoría, el mes con más ventas y la tendencia de enero a junio en porcentaje. Ejecútalo. Los números tienen que salir del CSV, nunca escritos a mano.
```

**3.** Mira lo que hace: qué ficheros lee, qué órdenes ejecuta, si te pide permiso. Cuando termine, sal con `Ctrl+C` (o sigue conversando: «revisa que…», «corrige…»).

<details><summary>Sin conversar, de una vez (opcional)</summary>

```bash
python taller.py lanzar ej16
```

O a mano, desde la carpeta de trabajo: `opencode run --standalone "…el encargo…"`.

</details>

> 💡 Antes de pegarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- `informe_semanal.txt` con los totales (29.800 / 18.700 / 14.000), mejor mes junio (12.800) y +43,8 %.
- Existe `informe.py` y, si cambias el CSV, el informe cambia.

```bash
python taller.py comprobar ej16      # el agente no decide si está bien: lo decide el comprobador
```

## 📂 Una solución de ejemplo

¿Te has atascado o no puedes ejecutarlo? Mira lo que hizo el agente con este encargo (el encargo, lo que escribió en pantalla y los ficheros): [`soluciones/ej16_informe_semanal/`](../../soluciones/ej16_informe_semanal/)

## 🔀 Siguiente paso

- **Programarlo cada lunes** → [🟣 EJ 21 · Programar una tarea periódica (con tu permiso)](../ej21_programar_cron/ENUNCIADO.md)
- **Como comando** → [🔵 F.3 · Comandos: el encargo de todos los lunes en una palabra](../f3_comandos/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
