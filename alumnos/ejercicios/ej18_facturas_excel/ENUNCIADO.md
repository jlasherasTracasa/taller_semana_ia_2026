# 🔵 EJ 18 · Facturas en PDF a Excel

> 🗂️ **Puerta D · El ayuntamiento** · 🔵 Medio · ⏱ 15 min · 🛠️ `opencode run` · Recomendado para: 📚

## 📖 La escena

Dos facturas en PDF para la gestoría. Que alguien las pase a Excel. Ese alguien es tu agente.

## 🎯 Objetivo

Extraer datos económicos de facturas PDF y volcarlos en una hoja de cálculo que cuadre.

## 📦 Lo que tienes en esta carpeta

- `facturas/`: dos facturas en PDF.

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar ej18
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Extrae de los PDF de facturas/ el emisor, la fecha, la base imponible, el IVA y el total, y genera facturas.xlsx con openpyxl. Añade una fila final con la suma de totales escrita como número (no como fórmula) y comprueba que cuadra con la suma de los totales de los PDF." | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- `facturas.xlsx` legible con los dos totales (454,48 y 1.212,90).
- Fila final 1.667,38.

```bash
python3 taller.py comprobar ej18      # el agente no puede darte el sello: solo el comprobador
```

## 🔀 ¿Y ahora qué?

- **Certificados en lote** → [🟢 EJ 19 · Un certificado para cada persona](../ej19_certificados_pdf/ENUNCIADO.md)
- **Volver a la plaza** → [↩️ La plaza](../../AVENTURA.md#-la-plaza)
