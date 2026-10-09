# EJ 19 · Certificados y cartas personalizadas en PDF

## Objetivo
Generar en lote un documento personalizado por persona a partir de una lista.

## Datos de partida
- `nombres.csv` — lista de alumnas y alumnos con su curso y horas de asistencia.

## Prompt sugerido
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Lee nombres.csv y genera un certificado_asistencia_NOMBRE.pdf para cada persona, con una plantilla sobria (reportlab o fpdf2): nombre, curso y horas. Verifica al final que hay un PDF por fila del CSV."
```

## Criterio de éxito
Un PDF por fila del CSV, cada uno con el nombre correcto y ninguno repetido. Si falta reportlab/fpdf2, el agente crea antes su propio entorno virtual (como en el EJ 11).

## Tiempo estimado
≈ 30 min

## Dificultad
Media-alta
