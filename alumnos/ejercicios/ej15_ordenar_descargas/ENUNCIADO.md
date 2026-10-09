# 🟢 EJ 15 · La carpeta de Descargas

> 🗂️ **Puerta D · El ayuntamiento** · 🟢 Fácil · ⏱ 10 min · 🛠️ `opencode run` · Recomendado para: 🧭

## 📖 La escena

Once archivos mezclados: facturas, fotos de la playa, el temario de oposiciones… Ordenar sin perder nada.

## 🎯 Objetivo

Clasificar archivos por tipo sin borrar ni renombrar ninguno.

## 📦 Lo que tienes en esta carpeta

- `descargas/`: 11 archivos.

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar ej15
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Organiza descargas/: crea las subcarpetas facturas, fotos, hojas_calculo, documentos e imagenes, y mueve cada archivo a la suya según su tipo y su nombre, sin borrar ni renombrar nada. Al final cuenta los archivos para comprobar que siguen siendo 11 y enséñame el árbol." | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- 5 subcarpetas y los 11 archivos dentro.
- Nada borrado ni renombrado, nada suelto.

```bash
python3 taller.py comprobar ej15      # el agente no puede darte el sello: solo el comprobador
```

## 🔀 ¿Y ahora qué?

- **Certificados para todos** → [🟢 EJ 19 · Un certificado para cada persona](../ej19_certificados_pdf/ENUNCIADO.md)
- **Volver a la plaza** → [↩️ La plaza](../../AVENTURA.md#-la-plaza)
