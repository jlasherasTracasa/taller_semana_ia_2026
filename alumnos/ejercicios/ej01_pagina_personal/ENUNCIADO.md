# EJ 01 · Página personal desde cero

## Objetivo
Convertir un texto en bruto (una bio) en una página web personal terminada, en un solo archivo HTML.

## Datos de partida
- `bio_pilar.txt` — biografía en texto plano de Pilar Azcona (panadera).

## Prompt sugerido
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Lee bio_pilar.txt y crea una página personal en un \
  único archivo index.html: HTML5+CSS embebido, responsive, en castellano, sin dependencias \
  externas ni frameworks."
```

## Criterio de éxito
`index.html` único (sin `<link>` ni `<script src>` externos), responsive, en castellano, con contacto funcional (mailto/tel). Ábrelo en el navegador y estrecha la ventana: nada debe cortarse.

## Tiempo estimado
≈ 10 min

## Dificultad
Baja
