# Solución · EJ 05 · Auditoría responsive/accesible

## Prompt exacto usado
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Audita web_centro_mayores.html: contraste de color, tamaño de fuente, media queries, atributo lang y navegación por teclado. Entrega primero la lista de incidencias y después la página corregida como web_corregida.html."
```

## Resultado
Lista de **5 incidencias** y `web_corregida.html` con `lang="es"`, texto `#333` y enlaces `#0055cc` sobre blanco (todos
por encima de 4,5:1), letra de 16 px, `<meta viewport>` y `@media (max-width: 600px)` con tabla fluida, el `div`
clicable convertido en enlace real, `alt` en el logo y estilos de foco visibles. También corrigió tildes
(«Miércoles», «información»).

## Salida real (extracto validado 2026-09-28)
```
1. Contraste de color: texto #4d4d4d sobre #7a2c8f ≈ 1,7:1 (mínimo WCAG AA: 4,5:1); enlaces #8fa y #9aa ilegibles.
2. Tamaño de fuente: 9px en el cuerpo y 8px en el enlace.
3. Media queries: ninguna @media; anchos fijos (table{width:900px}); falta <meta name="viewport">.
4. Atributo lang: <html> sin idioma; además, texto sin tildes.
5. Navegación por teclado: <div onclick=…> no recibe foco; enlace «leer mas» con href="#".
```

## Cómo comprobarlo tú
Abre las dos páginas en el navegador, estrecha la ventana y recorre la corregida solo con el tabulador.
