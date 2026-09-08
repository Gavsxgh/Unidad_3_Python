promedio = float(input("Ingrese el valor de su promedio: "))
Nvl_socioeconómico = int(input("Ingrese su nivel socioeconomico: "))
if promedio >= 9.0 or (promedio > 8.0 and Nvl_socioeconómico == 1):
    print ("Aplica para la beca")
else:
    print ("No aplica para la beca")
