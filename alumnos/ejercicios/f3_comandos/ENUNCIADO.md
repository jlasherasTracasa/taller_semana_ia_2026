# 🔵 F.3 · Comandos: el encargo de todos los lunes en una palabra

> ⚙️ **Puerta F · La sala de máquinas** · 🔵 Medio · ⏱ 15 min · 🛠️ `opencode` interactivo · Recomendado para: 📚 💻

## 📖 La escena

La tienda pide el mismo informe cada semana. En vez de copiar el encargo, lo guardas como comando: `/informe-semanal`.

## 🎯 Objetivo

Convertir un encargo recurrente en un **comando** versionado (`.opencode/commands/`) que cualquiera del equipo invoca con `/nombre`, con argumentos opcionales (`$ARGUMENTS`).

## 📦 Lo que tienes en esta carpeta

- `datos/ventas_tienda.csv`: ventas por mes y categoría.
- `.opencode/commands/informe-semanal.md`: el comando, ya escrito. Ábrelo y léelo antes de usarlo.

## 💬 El encargo

Los comandos solo funcionan en el **modo interactivo**:
```bash
opencode
> /informe-semanal
```
Después crea tú un segundo comando, `.opencode/commands/resumen-mes.md`, que reciba el mes como argumento
(`/resumen-mes junio`) y escriba `resumen_<mes>.txt` con el total de ese mes por categoría.

## ✅ ¿Lo ha hecho de verdad?

- `informe_semanal.pptx` con exactamente 3 diapositivas.
- Totales que cuadran con el CSV: hogar 29.800 €, textil 18.700 €, bazar 14.000 €, total 62.500 €.
- Tu comando `/resumen-mes junio` escribe `resumen_junio.txt` con 12.800 € en total.

```bash
python3 taller.py comprobar f3      # el agente no puede darte el sello: solo el comprobador
```

## 🧪 Lo que pasó al validarlo (09-10-2026)

El cuerpo del comando genera las 3 diapositivas con los totales exactos. El comando original decía que el CSV tenía columnas `mes,categoria,importe` (falso): corregido. En opencode 2.x `run --command` ya no existe: los comandos se usan con `/nombre` en modo interactivo.

Prompt, salida real y ficheros: [`soluciones/f3_comandos/`](../../soluciones/f3_comandos/)

## 🔀 ¿Y ahora qué?

- **Quiero una receta que el agente cargue él solo** → [🔵 F.4 · Skills: recetas que el agente carga cuando las necesita](../f4_skills/ENUNCIADO.md)
- **Quiero que lo haga cada lunes sin pedírselo** → [🟣 EJ 21 · Que se ejecute solo (con tu permiso)](../ej21_programar_cron/ENUNCIADO.md)
- **Volver a la plaza** → [↩️ La plaza](../../AVENTURA.md#-la-plaza)
