# Solución · Página personal desde cero

## Prompt exacto usado
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Lee bio_pilar.txt y crea una página personal en un \
  único archivo index.html: HTML5+CSS embebido, responsive, en castellano, sin dependencias \
  externas ni frameworks."
```

## Resultado
`index.html` creado: página única, paleta cálida de panadería, secciones Mi historia / Talleres / Aficiones / Contacto con mailto y tel funcionales, media query móvil.

## Salida real (extracto validado 2026-09-28)
```
Extracto real de la salida de opencode run (validado 2026-09-28, ./):
- Página personal de Pilar Azcona en un único archivo: HTML5 con CSS embebido,
  sin dependencias ni frameworks.
- Responsive (clamp, media query móvil, ancho máximo de contenido) con paleta
  cálida de panadería (marrón, crema, dorado).
- Secciones: cabecera con navegación, Mi historia, Talleres de masa madre,
  Aficiones y pie con contacto (mailto y tel funcionales).

Verificación objetiva:
$ python3 -m http.server 8910 &
$ curl -s -o /dev/null -w "%{http_code}" http://localhost:8910/index.html
200
```

Los artefactos generados (archivos de resultado) están en esta misma carpeta.
