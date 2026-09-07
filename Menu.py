print("1. Platos fuertes\n2. Bebidas\n3. Postres\n4. Salir")
opcion = int(input("Ingrese la opcion: "))

while True:
    if opcion == 1: 
        print("Platos fuertes")
        print("1. Pollo a la plancha\n2. Carne asada\n3. Filete de salmon\n4. Pasta")
        plato = input("Elija su Plato fuerte: ")
        print("\n\n")
    elif opcion == 2:
        print("Bebidas")
        print("1. Agua\n2. Gaseosa\n3. Limonada\n4. Michelada")
        plato = input("Elija su Bebida: ")
        print("\n\n")
    elif opcion == 3:
        print("Postres")
        print("1. Tiramisu\n2. Flan de caramelo\n3. Pie de limon\n4. Helado")
        plato = input("Elija su Postre: ")
        print("\n\n")
    elif opcion == 4:
        print("Saliendo...!")
    else:
        print("Ocion no valida - Reintentar")

    print("1. Platos fuertes\n2. Bebidas\n3. Postres\n4. Salir")
    opcion = int(input("Ingrese la opcion: "))