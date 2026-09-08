n = int(input("Ingrese el valor: "))
factorial = 1
contador = 1
while contador <= n:
    factorial = contador * factorial
    contador = contador + 1
print(f"{n}! = {factorial}")