cuenta = float(input("Ingrese el valor de la cuenta: "))
propina = cuenta * 0.15
total = cuenta + propina
individual = total / 4
print(f"La propina es: {propina}")
print(f"El total es: {total}")
print(f"Individualmente, cada uno debe pagar: {individual}")
