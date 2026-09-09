# Sistema de Monitoreo de Vuelo para un Cohete Suborbital

## Análisis E/P/S (Entradas / Procesos / Salidas)

### 1.1 Variables de entrada

| VARIABLE | TIPO | DESCRIPCIÓN |
| --- | --- | --- |
| Presion_hpa | Float | Presión atmosférica medida por el sensor barométrico (hPa) |
| Aceleracion | Float | Aceleración medida por el acelerómetro (m/s²) |
| Temp_celcius | Float | Temperatura del motor/estructura (°C) |
| Entrada_presion | str | Permite la palabra **"FIN"** para terminar la simulación manualmente |

### 1.2 Procesos

- Convertir presión en altitud, con la fórmula barométrica.
- Comparar altitud_actual vs altitud_previa para saber si el cohete sube o baja.
- Determinar la fase de vuelo (Ascenso / Apogeo-Caída libre / Despliegue de paracaídas).
- Evaluar si la temperatura cruza el límite crítico (Sonar alarma).
- Actualizar acumuladores: altitud máxima, suma de temperaturas + contador (para el promedio), aceleración máxima.
- Detectar el instante del apogeo con una bandera booleana (sólo debe activarse una vez, la primera vez que la altitud baja).
- Repetir segundo a segundo hasta que el cohete aterrice (altitud_actual <= 0) o el operador escriba FIN.

### 1.3 Variables de salida

| VARIABLE | TIPO | DESCRIPCIÓN |
| --- | --- | --- |
| Reporte por segundo | - | Altitud, fase de vuelo, altitud máxima acumulada, estado de la bandera de apogeo, alarma de temperatura si aplica |
| Resumen final | - | Duración total, altitud máxima, temperatura promedio, aceleración máxima, motivo de finalización |
