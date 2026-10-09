# ✍️ Cómo dar un buen encargo

Un agente hace lo que le pides… y decide él todo lo que no le pides. Cinco piezas:

| Pieza | Qué es | Ejemplo |
|---|---|---|
| **CONTEXTO** | Lo que no puede adivinar | «Soy una panadería; estos correos son de hoy» |
| **OBJETIVO** | El resultado, en una frase | «Un resumen ordenado por urgencia» |
| **ENTREGA** | Formato y nombre exactos | «Escríbelo en `correo/resumen_diario.md`» |
| **LÍMITES** | Lo que NO puede hacer | «No envíes nada; no mates procesos; no toques el original» |
| **CRITERIO** | Cuándo está bien | «7 filas; urgencia: alta, media, baja o ninguna» |

## Lo que nos pasó por no pedirlo (validación real)

| Escena | Faltaba… | Y el agente… |
|---|---|---|
| EJ 06 | ENTREGA: «escribe el fichero» | Dio el resumen en pantalla y **no creó el fichero**. Terminó tan tranquilo. |
| EJ 07 | CRITERIO: valores de `urgencia` | Se inventó «nula». |
| EJ 12 | ENTREGA: «una tabla con los totales» | Hizo el gráfico; **los totales no estaban en ningún sitio**. |
| EJ 09 | CRITERIO: «con zona horaria» | Dejó la hora «flotante». |
| EJ 04 | CONTEXTO: «en castellano» | Respondió en inglés. |
| EJ 05 | LÍMITES: «no me hagas preguntas» | Se paró a preguntar y, en `opencode run`, nadie contestó. |
| F.8 | CRITERIO del informe | Dejó la parte comprobable perfecta y **se saltó la que no se comprobaba**. |

## Plantilla para copiar

```text
CONTEXTO  …
OBJETIVO  …
ENTREGA   Escribe <fichero> con <formato>. No basta con enseñármelo en pantalla.
LÍMITES   No borres ni envíes nada. No toques <original>. No hagas preguntas: si dudas, decide y explícalo.
CRITERIO  Al final comprueba <qué> (cuenta, abre el fichero, ejecuta los tests) y dime el resultado.
```

## Truco: que se compruebe solo

Pide al agente que **verifique** al final («cuenta las filas», «abre el pptx y dime cuántas diapositivas tiene»,
«ejecuta los tests»). Y después compruébalo tú: `python3 taller.py comprobar <ejercicio>`.
