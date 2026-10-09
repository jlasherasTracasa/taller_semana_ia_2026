# 🔵 EJ 11 · De informe escrito a presentación

> 📊 **Informes y presentaciones** · 🔵 Medio · ⏱ 15 min · 🛠️ `opencode run` · Recomendado para: 📚

## 📌 La situación

Una bodega presenta los resultados de la vendimia en la asamblea de la cooperativa. Tiene el informe escrito; falta la presentación.

## 🎯 Objetivo

Generar una presentación sobria de 5-6 diapositivas a partir de un informe en Markdown.

## 📦 Lo que tienes en esta carpeta

- `informe_cosecha.md`: el informe de la vendimia 2025.

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar ej11
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Lee informe_cosecha.md y genera presentacion.pptx con python-pptx (está en el requirements.txt del kit): entre 5 y 6 diapositivas 16:9 sobrias, con portada, resumen, rendimiento por variedad, evolución y conclusiones. Copia las cifras tal cual del informe. Al final, abre el pptx con python-pptx y dime cuántas diapositivas tiene." | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- `presentacion.pptx` abre sin errores y tiene 5 o 6 diapositivas.
- Cifras fieles: 84.000 kg, −12 % frente a 95.500 kg.

```bash
python3 taller.py comprobar ej11      # el agente no decide si está bien: lo decide el comprobador
```

## 🧪 Lo que pasó al validarlo (09-10-2026)

6 diapositivas con 84.000 kg y −12 % frente a 95.500 kg.

Prompt, salida real y ficheros: [`soluciones/ej11_informe_pptx/`](../../soluciones/ej11_informe_pptx/)

## 🔀 Siguiente paso

- **Con gráfico de verdad** → [🔵 EJ 12 · Presentación con gráfico y totales que cuadran](../ej12_grafico_pptx/ENUNCIADO.md)
- **Revisar un deck ajeno** → [🔵 EJ 13 · Revisar y corregir una presentación ajena](../ej13_revision_deck/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
