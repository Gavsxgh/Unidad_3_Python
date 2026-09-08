inicio
    tiempo = 0
    altitud_previa = 0
    altitud_maxima = 0
    apogeo_detectado = falso
    suma_temp = 0
    cont_temp = 0
    acel_maxima = 0
    aterrizo = falso

    mientras verdadero
        pedir presion (o "FIN" para salir)
        si el dato es "FIN" entonces
            salir del bucle
        fin si
        pedir aceleracion
        pedir temperatura

        altitud_actual = calcular_altitud(presion)

        si altitud_actual > altitud_maxima entonces
            altitud_maxima = altitud_actual
        fin si

        si apogeo_detectado es falso y altitud_actual < altitud_previa entonces
            apogeo_detectado = verdadero
            mostrar "aqui fue el apogeo"
        fin si

        estado = determinar_estado_vuelo(altitud_actual, altitud_previa, aceleracion)
        alarma = evaluar_alerta_temperatura(temperatura)

        suma_temp = suma_temp + temperatura
        cont_temp = cont_temp + 1
        si aceleracion > acel_maxima entonces
            acel_maxima = aceleracion
        fin si

        mostrar altitud, estado, altitud_maxima, apogeo_detectado
        si alarma es verdadero entonces
            mostrar "alarma temperatura"
        fin si

        si altitud_actual <= 0 y tiempo > 0 entonces
            aterrizo = verdadero
            salir del bucle
        fin si

        altitud_previa = altitud_actual
        tiempo = tiempo + 1
    fin mientras

    si cont_temp > 0 entonces
        promedio_temp = suma_temp / cont_temp
    sino
        promedio_temp = 0
    fin si

    mostrar resumen (tiempo, altitud_maxima, promedio_temp, acel_maxima, aterrizo)

    fin

    ---
## Diagrama de flujo
![Caso 1](./Imagenes/RETO.png)
