# 🟢 EJ 19 · Un certificado para cada persona

> 🗂️ **Puerta D · El ayuntamiento** · 🟢 Fácil · ⏱ 15 min · 🛠️ `opencode run` · Recomendado para: 🧭 📚

## 📖 La escena

Fin de curso en el centro de mayores: un certificado de asistencia para cada participante.

## 🎯 Objetivo

Generar en lote un documento personalizado por persona a partir de una lista.

## 📦 Lo que tienes en esta carpeta

- `nombres.csv`: nombre, curso y horas.

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar ej19
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Lee nombres.csv y genera en la carpeta certificados/ un PDF por persona llamado certificado_NOMBRE.pdf, con una plantilla sobria hecha con reportlab: nombre, curso y horas. Verifica al final que hay un PDF por fila del CSV y que cada uno lleva su nombre." | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- Un PDF por fila del CSV, cada uno con su nombre, ninguno repetido.

```bash
python3 taller.py comprobar ej19      # el agente no puede darte el sello: solo el comprobador
```

## 🔀 ¿Y ahora qué?

- **Exámenes por corregir** → [🔵 EJ 23 · Corregir con rúbrica (y una trampa)](../ej23_corregir_rubrica/ENUNCIADO.md)
- **Volver a la plaza** → [↩️ La plaza](../../AVENTURA.md#-la-plaza)
