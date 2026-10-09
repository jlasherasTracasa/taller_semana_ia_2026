# Solución · Agenda de evento desde un CSV

## Prompt exacto usado
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Lee programa.csv y crea agenda.html: página de una \
  sola columna, diseño festivo, responsive y sin dependencias externas."
```

## Resultado
`agenda.html` creado: 6 eventos del CSV agrupados mañana/tarde, tarjetas con hora en círculo, etiquetas coloreadas por tipo, responsive sin dependencias.

## Salida real (extracto validado 2026-09-28)
```
Extracto real de la salida de opencode run (validado 2026-09-28, ./):
Wrote file successfully.
Creado `agenda.html` con los 6 eventos del CSV. Una sola columna, estilo festivo
(banderines, tarjetas con sombras de color, hora en círculo rojo), etiquetas coloreadas
por tipo de actividad y totalmente responsive sin ninguna dependencia externa.

Verificación objetiva:
$ curl -s -o /dev/null -w "%{http_code}" http://localhost:8910/agenda.html
200
```

Los artefactos generados (archivos de resultado) están en esta misma carpeta.
