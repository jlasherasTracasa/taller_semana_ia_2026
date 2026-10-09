# EJ 17 · Resumir todos los PDF de una carpeta

## Objetivo
Obtener un resumen estructurado de un conjunto de documentos PDF de golpe.

## Datos de partida
- `apuntes/guia_gimnasia.pdf`, `apuntes/programa_memoria.pdf` y `apuntes/normas_excursiones.pdf` — documentos ficticios de un centro cívico.

## Prompt sugerido
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Lee los PDF de apuntes/ uno a uno con pdfplumber y crea resumen_apuntes.md: tabla Markdown con título, tema y tres puntos clave de cada documento."
```

## Criterio de éxito
Tabla que cubre los tres PDFs, con puntos clave tomados del texto real (no inventados) y verificables abriendo los originales.

## Tiempo estimado
≈ 20 min

## Dificultad
Media
