edad_usuario = int(input("Ingrese la edad del usuario: "))
saldo_billetera = float(input("cuanto dinero tiene el usuario: "))
tiene_suscripcion_premium = input("Tiene suscripcion premium?: (Si/No) ")
if edad_usuario >= 17 and saldo_billetera >= 60:
    if tiene_suscripcion_premium.lower() == "si": 