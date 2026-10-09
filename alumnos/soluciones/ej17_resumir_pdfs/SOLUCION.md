# Solución · EJ 17 · Resumir todos los PDF de una carpeta

## Prompt exacto usado
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Lee los PDF de apuntes/ uno a uno con pdfplumber y crea resumen_apuntes.md: tabla Markdown con título, tema y tres puntos clave de cada documento."
```

## Resultado
`resumen_apuntes.md` con la tabla solicitada (título, tema y tres puntos clave por cada uno de los 3 PDFs), extraída del texto real de los documentos.

## Salida real (extracto validado 2026-09-28)
```
Trabajamos atención, lenguaje y orientación con juegos de mesa y asociaciones.
--- page 2 ---
Sesiones 1 a 4
Presentación, atención selectiva con tarjetas, listas de la compra encadenadas...

← Write resumen_apuntes.md
Wrote file successfully.

Hecho. Leí los 3 PDF de apuntes/ con pdfplumber y creé resumen_apuntes.md
con la tabla (título, tema y tres puntos clave por documento).
```

El artefacto generado está en esta misma carpeta.
