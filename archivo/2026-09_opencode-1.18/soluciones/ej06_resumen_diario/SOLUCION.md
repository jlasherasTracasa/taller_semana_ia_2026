# Solución · Resumen diario

## Prompt exacto usado
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Lee todos los correos de correo/bandeja/ (archivos .eml) \
  y escribe correo/resumen_diario.md con un resumen diario ordenado por urgencia (urgente/media/baja), \
  indicando remitente, asunto y acción requerida."
```

## Resultado
`correo/resumen_diario.md` con los 7 correos clasificados: urgente (proveedor, cliente boda, IVA), media (festival Vigo, quedada, taller) y baja (spam de lotería).

## Salida real (extracto validado 2026-09-28)
```
Extracto real de la salida de opencode run (validado 2026-09-28, ./):
Hecho: `correo/resumen_diario.md` creado con los 7 correos clasificados en urgente
(proveedor, cliente boda, IVA), media (festival Vigo, quedada, taller) y baja
(spam de lotería).
```

Los artefactos generados (archivos de resultado) están en esta misma carpeta.
