import math
radio=float(input("introduce el valor numérico del radio del círculo"))
altura=float(input("introduce el valor numérico de la altura del cilindro"))
area=2*math.pi*radio*altura+2*math.pi*radio**2
volumen=math.pi*radio**2*altura
arearedondeada=round(area,2)
volumenredondeado=round(volumen,2)
print("el área del cilindro es:",arearedondeada)
print("el volumen del cilindro es:",volumenredondeado)

