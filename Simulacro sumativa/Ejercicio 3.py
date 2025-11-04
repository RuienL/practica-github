import math
mensaje=input("Si desea en Mayúsuculas escriba mayúsculas, si desea en minúsculas escriba minúsculas: ")
radio=int(input("Introduce el radio de una circunferencia: "))
altura=int(input("Introduce la altura del cilindro: "))
Volumen = math.pi * radio ** 2 * altura
redondeo=round(Volumen,3)
if mensaje=="mayúsculas":
    print(f"EL VOLUMEN DEL CILINDRO ES: {redondeo}")
elif mensaje=="minúsculas":
    print(f"el volumen del cilindro es: {redondeo}")
elif mensaje!="Mayúsculas" or mensaje!="minúsculas":
    print("Error, formato no válido")

