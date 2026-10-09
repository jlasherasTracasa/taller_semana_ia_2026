# 🔵 EJ 16 · El informe que se recalcula solo

> 📊 **Puerta C · La bodega** · 🔵 Medio · ⏱ 15 min · 🛠️ `opencode run` · Recomendado para: 📚

## 📖 La escena

Cada lunes, el mismo informe con datos nuevos. Mejor un script que lo recalcule que un texto copiado.

## 🎯 Objetivo

Un informe de texto generado por un script que lee el CSV, para que sirva la semana que viene.

## 📦 Lo que tienes en esta carpeta

- `ventas_tienda.csv`.

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar ej16
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Lee ventas_tienda.csv y escribe un script informe.py que genere informe_semanal.txt con el total por categoría, el mes con más ventas y la tendencia de enero a junio en porcentaje. Ejecútalo. Los números tienen que salir del CSV, nunca escritos a mano." | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- `informe_semanal.txt` con los totales (29.800 / 18.700 / 14.000), mejor mes junio (12.800) y +43,8 %.
- Existe `informe.py` y, si cambias el CSV, el informe cambia.

```bash
python3 taller.py comprobar ej16      # el agente no puede darte el sello: solo el comprobador
```

## 🧪 Lo que pasó al validarlo (09-10-2026)

`informe.py` regenera el informe con 29.800 / 18.700 / 14.000, junio 12.800 y +43,8 %. El encargo antiguo apuntaba a `pptx/ventas_tienda.csv`, una ruta que no existe.

Prompt, salida real y ficheros: [`soluciones/ej16_informe_semanal/`](../../soluciones/ej16_informe_semanal/)

## 🔀 ¿Y ahora qué?

- **Programarlo cada lunes** → [🟣 EJ 21 · Que se ejecute solo (con tu permiso)](../ej21_programar_cron/ENUNCIADO.md)
- **Como comando** → [🔵 F.3 · Comandos: el encargo de todos los lunes en una palabra](../f3_comandos/ENUNCIADO.md)
- **Volver a la plaza** → [↩️ La plaza](../../AVENTURA.md#-la-plaza)
