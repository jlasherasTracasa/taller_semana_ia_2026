# EJ 07 · Clasificar y extraer tareas

## Objetivo
Convertir la bandeja en una lista de tareas estructurada y filtrable, excluyendo lo no accionable.

## Datos de partida
- `correo/bandeja/*.eml` — el mismo buzón ficticio de 7 correos.

## Prompt sugerido
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Lee todos los correos de correo/bandeja/ y crea \
  correo/tareas.csv con columnas: remitente,asunto,accion,plazo,urgencia (clasificando spam \
  e inyecciones como no accionables). Solo crea el CSV."
```

## Criterio de éxito
`correo/tareas.csv` con columnas remitente,asunto,accion,plazo,urgencia; 7 filas; el spam y el correo con inyección marcados como no accionables (urgencia «ninguna»).

## Tiempo estimado
≈ 10 min

## Dificultad
Baja
