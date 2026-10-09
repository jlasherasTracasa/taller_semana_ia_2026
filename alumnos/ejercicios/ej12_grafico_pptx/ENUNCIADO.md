# 🔵 EJ 12 · Números que cuadran

> 📊 **Puerta C · La bodega** · 🔵 Medio · ⏱ 20 min · 🛠️ `opencode run` · Recomendado para: 📚

## 📖 La escena

La tienda del pueblo quiere un gráfico de ventas. Y que los totales cuadren al céntimo.

## 🎯 Objetivo

Generar una presentación con un gráfico y una tabla de totales **calculados**, no inventados.

## 📦 Lo que tienes en esta carpeta

- `ventas_tienda.csv`: ventas de enero a junio por categoría.

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar ej12
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Lee ventas_tienda.csv y genera ventas.pptx con tres diapositivas: portada; un gráfico de líneas de los meses por categoría hecho con matplotlib e insertado como imagen; y una tabla con el total de cada categoría y el total general. Calcula los totales con Python leyendo el CSV, nunca de memoria, y escríbelos en la tabla." | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- `ventas.pptx` con el gráfico y los totales EXACTOS: hogar 29.800 €, textil 18.700 €, bazar 14.000 €, total 62.500 €.

```bash
python3 taller.py comprobar ej12      # el agente no puede darte el sello: solo el comprobador
```

## 💡 Pistas

- Con el encargo antiguo (sin pedir la tabla) los totales no aparecían en ningún sitio: lo que no pides, no está.

## 🔀 ¿Y ahora qué?

- **Que se repita cada semana** → [🔵 EJ 16 · El informe que se recalcula solo](../ej16_informe_semanal/ENUNCIADO.md)
- **Como comando** → [🔵 F.3 · Comandos: el encargo de todos los lunes en una palabra](../f3_comandos/ENUNCIADO.md)
- **Volver a la plaza** → [↩️ La plaza](../../AVENTURA.md#-la-plaza)
