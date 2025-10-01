##Programa que pida el valor del diámetro de un círculo y muestre por pantalla el área y el perímetro del mismo. Usa la constante pi del módulo math.
import math
diametro=float(input("introduce el valor numérico del diámetro del círculo"))
radio=diametro/2
area=math.pi*radio**2
perimetro=2*math.pi*radio
arearedondeada=round(area,2)
perimetroredondeada=round(perimetro,2)
print("el área del círculo es:",arearedondeada)
print("el perímetro del círculo es:",perimetroredondeada)
