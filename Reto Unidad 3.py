# Sistema de Monitoreo de Vuelo para un Cohete Suborbital
# Reto de programacion - Unidad 3

# Constantes de cada elemento
ALTURA_PARACAIDAS = 500.0
DESACELERACION_PARACAIDAS = -15.0
TEMP_LIMITE = 95.0


# funcion 1: calcular la altitud a partir de la presion
def calcular_altitud(presion_hpa):
    altitud = 44330 * (1 - (presion_hpa / 1013.25) ** 0.1903)
    return altitud

# import random
# =random.uniform()
# funcion 2: determina fase de vuelo del cohete
def determinar_estado_vuelo(altitud_actual, altitud_previa, aceleracion):
    if altitud_actual > altitud_previa:
        estado = "Ascenso"
    else:
        # si baja mucho o si frena mal, ya abrio el paracaidas
        if altitud_actual <= ALTURA_PARACAIDAS or aceleracion <= DESACELERACION_PARACAIDAS:
            estado = "Despliegue de Paracaidas"
        else:
            estado = "Apogeo / Caida libre"
    return estado


# funcion 3: revisa si la temperatura esta muy alta
def evaluar_alerta_temperatura(temp_celsius):
    if temp_celsius >= TEMP_LIMITE:
        return True
    else:
        return False


def Flujo_vuelo():
    tiempo = 0
    altitud_previa = 0.0
    altitud_maxima = 0.0
    apogeo_detectado = False

    suma_temp = 0.0
    cont_temp = 0
    acel_maxima = 0.0

    aterrizo = False

    print("MONITOR DE VUELO DEL COHETE")
    print("Escriba FIN en la presion para terminar")

    while True:
        dato = input("t=" + str(tiempo) + "s Presion (hPa) o FIN: ")

        if dato == "FIN" or dato == "fin":
            break

        # Por si se escribe mal el num.
        try:
            presion = float(dato)
        except:
            print("eso no es un numero, intente otra vez")
            continue

        aceleracion = float(input("Aceleracion (m/s2): "))
        temperatura = float(input("Temperatura (C): "))

        altitud_actual = calcular_altitud(presion)

        # altitud mas alta que ha llegado
        if altitud_actual > altitud_maxima:
            altitud_maxima = altitud_actual

        # se detecto el apogeo solo la primera vez que empieza a bajar
        if apogeo_detectado == False and altitud_actual < altitud_previa:
            apogeo_detectado = True
            print("AQUI FUE EL APOGEO")

        estado = determinar_estado_vuelo(altitud_actual, altitud_previa, aceleracion)
        alarma = evaluar_alerta_temperatura(temperatura)

        #  promedio de temperatura
        suma_temp = suma_temp + temperatura
        cont_temp = cont_temp + 1

        if aceleracion > acel_maxima:
            acel_maxima = aceleracion

        print("Altitud: " + str(round(altitud_actual, 2)) + " m")
        print("Fase: " + estado)
        print("Altitud maxima: " + str(round(altitud_maxima, 2)) + " m")
        print("Apogeo detectado: " + str(apogeo_detectado))
        if alarma == True:
            print("ALARMA! temperatura muy alta")

        # si ya toco el suelo se acaba la simulacion
        if altitud_actual <= 0 and tiempo > 0:
            aterrizo = True
            tiempo = tiempo + 1
            break

        altitud_previa = altitud_actual
        tiempo = tiempo + 1

    # calculo el promedio al final, sin guardar todos los datos
    if cont_temp > 0:
        promedio_temp = suma_temp / cont_temp
    else:
        promedio_temp = 0.0

    print("")
    print("RESUMEN FINAL")
    print("Tiempo total: " + str(tiempo) + " s")
    print("Altitud maxima: " + str(round(altitud_maxima, 2)) + " m")
    print("Temperatura promedio: " + str(round(promedio_temp, 2)) + " C")
    print("Aceleracion maxima: " + str(round(acel_maxima, 2)) + " m/s2")
    if aterrizo == True:
        print("El cohete aterrizo")
    else:
        print("El operador termino la simulacion")


Flujo_vuelo()