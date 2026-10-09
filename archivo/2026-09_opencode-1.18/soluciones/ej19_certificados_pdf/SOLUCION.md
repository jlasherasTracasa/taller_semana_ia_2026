# Solución · EJ 19 · Certificados y cartas personalizadas en PDF

## Prompt exacto usado
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Lee nombres.csv y genera un certificado_asistencia_NOMBRE.pdf para cada persona, con una plantilla sobria (reportlab o fpdf2): nombre, curso y horas. Verifica al final que hay un PDF por fila del CSV."
```

## Resultado
`generar_certificados.py` (reportlab; plantilla A4 apaisada sobria: doble marco, nombre destacado, curso y horas) y 5 PDFs, uno por fila del CSV, con verificación 1:1.

## Salida real (extracto validado 2026-09-28)
```
Verificación: el CSV tiene 5 filas y se generaron 5 PDFs, uno por persona:
- certificado_asistencia_amparo_lecumberri.pdf
- certificado_asistencia_felix_bergoa.pdf
- certificado_asistencia_nieves_izco.pdf
- certificado_asistencia_purificacion_aranguren.pdf
- certificado_asistencia_teodoro_sanz.pdf
Después el agente abrió cada PDF con pypdf y comprobó nombre, curso y horas: «TODOS CORRECTOS».
```

Los artefactos generados están en esta misma carpeta.
