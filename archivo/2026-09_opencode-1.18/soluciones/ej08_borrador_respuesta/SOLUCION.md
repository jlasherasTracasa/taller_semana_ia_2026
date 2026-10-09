# Solución · Borradores de respuesta

## Prompt exacto usado
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Lee correo/bandeja/01_proveedor_urgente.eml y escribe \
  un borrador de respuesta en correo/borrador_proveedor.md confirmando el pedido mensual para \
  mantener el precio antiguo. Tono profesional en castellano. No envíes nada, solo el borrador."
```

## Resultado
`correo/borrador_proveedor.md`: borrador profesional que confirma el pedido mensual antes del jueves 26 y mantiene los 38 €/saco. No se envió nada.

## Salida real (extracto validado 2026-09-28)
```
Extracto real de correo/borrador_proveedor.md generado por opencode run (validado 2026-09-28):
Estimados señores de Harinas Verde:

Acusamos recibo de su comunicación del día de hoy, relativa a la actualización de precios
de la harina integral a partir del próximo lunes.

Les confirmamos nuestro pedido mensual habitual de harina integral, formulado dentro del
plazo indicado (antes del jueves 26), con el fin de mantener el precio actual de 38 € por saco...

No se envió ningún correo: solo se creó el borrador.
```

Los artefactos generados (archivos de resultado) están en esta misma carpeta.
