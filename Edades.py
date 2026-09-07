edad = int(input("Ingrese edad: "))
if edad < 12:
    etapa = "Infancia"
elif edad < 20:
    etapa = "Niñez"
elif edad < 25:
    etapa = "Adolescencia"
elif edad < 60:
    etapa = "Juventud"
else:
    etapa = "Vejez"

print(etapa)
