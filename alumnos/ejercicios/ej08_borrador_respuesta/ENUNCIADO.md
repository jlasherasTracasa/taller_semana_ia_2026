# EJ 08 · Borradores de respuesta

## Objetivo
Redactar una respuesta profesional manteniendo una cifra concreta del correo original (38 €/saco).

## Datos de partida
- `correo/bandeja/01_proveedor_urgente.eml` — aviso de subida de precios con plazo del jueves 26.

## Prompt sugerido
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Lee correo/bandeja/01_proveedor_urgente.eml y escribe \
  un borrador de respuesta en correo/borrador_proveedor.md confirmando el pedido mensual para \
  mantener el precio antiguo. Tono profesional en castellano. No envíes nada, solo el borrador."
```

## Criterio de éxito
`correo/borrador_proveedor.md`: borrador profesional en castellano que confirma el pedido antes del jueves 26 y menciona los 38 €/saco. Nada se envía: el agente solo redacta.

## Tiempo estimado
≈ 10 min

## Dificultad
Baja
