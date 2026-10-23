# 🔵 F.3 · Comandos: el encargo de todos los lunes en una palabra

> ⚙️ **Cómo funciona un agente** · 🔵 Medio · ⏱ 15 min · 🛠️ solo opencode interactivo · Recomendado para: 📚 💻

> 🎥 **Demo en directo**: lo hace el profesor en el proyector; tú lo miras y lo repites después si quieres.

## 📌 La situación

Cada lunes alguien prepara el mismo informe de ventas. En lugar de copiar y pegar el encargo, se guarda como comando del equipo.

## 🎯 Objetivo

Convertir un encargo recurrente en un **comando** versionado (`.opencode/commands/`) que cualquiera del equipo invoca con `/nombre`, con argumentos opcionales (`$ARGUMENTS`).

## 📦 Lo que tienes en esta carpeta

- `datos/ventas_tienda.csv`: ventas por mes y categoría.
- `.opencode/commands/informe-semanal.md`: el comando, ya escrito. Ábrelo y léelo antes de usarlo.

## 💬 El encargo

Los comandos solo funcionan en el **modo interactivo**. En la terminal, desde la carpeta `alumnos`:
```bash
python taller.py abrir f3
```
Aquí **no hay que pegar ningún encargo**: dentro de opencode escribe `/informe-semanal` y pulsa **Enter dos veces**: al
escribir `/` sale la lista de comandos, el primer Enter elige el comando y el segundo lo envía. El encargo largo ya está guardado en
`.opencode/commands/informe-semanal.md`: ábrelo para verlo. Cuando termine, sal con `Ctrl+C`.

**Tu propio comando.** Crea con cualquier editor el fichero `.opencode/commands/resumen-mes.md` dentro de tu carpeta
de trabajo (`~/taller-agentes/f3_comandos/`; en Windows la carpeta `.opencode` puede estar oculta: actívalo en «Vista →
Elementos ocultos»). Puedes partir de esto:

```text
---
description: Resumen de ventas de un mes por categoría
---
Lee `datos/ventas_tienda.csv` (columnas mes,hogar,textil,bazar). Para el mes $ARGUMENTS, calcula con Python
el importe de cada categoría y el total, y escríbelo en `resumen_$ARGUMENTS.txt`. No inventes cifras.
```

`$ARGUMENTS` se sustituye por lo que escribas detrás del comando. Abre opencode otra vez (`python taller.py abrir f3`:
los comandos se leen al arrancar) y escribe `/resumen-mes junio`, con Enter (si sigue en la caja, Enter otra vez).

## ✅ ¿Lo ha hecho de verdad?

- `informe_semanal.pptx` con exactamente 3 diapositivas.
- Totales que cuadran con el CSV: hogar 29.800 €, textil 18.700 €, bazar 14.000 €, total 62.500 €.
- Tu comando `/resumen-mes junio` escribe `resumen_junio.txt` con 12.800 € en total.

```bash
python taller.py comprobar f3      # el agente no decide si está bien: lo decide el comprobador
```

## 🧪 Lo que pasó al validarlo (11-10-2026)

Validado en **modo interactivo** el 11-10: `/informe-semanal` → 3 diapositivas y totales exactos; `/resumen-mes junio`, escrito como lo haría un alumno → 12.800 €.

Prompt, salida real y ficheros: [`soluciones/f3_comandos/`](../../soluciones/f3_comandos/)

## 🔀 Siguiente paso

- **Quiero una receta que el agente cargue él solo** → [🔵 F.4 · Skills: recetas que el agente carga cuando las necesita](../f4_skills/ENUNCIADO.md)
- **Quiero que lo haga cada lunes sin pedírselo** → [🟣 EJ 21 · Programar una tarea periódica (con tu permiso)](../ej21_programar_cron/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
