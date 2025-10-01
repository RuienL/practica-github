##Programa que pida un número y muestre su raíz cuadrada y la raíz cuadrada dividida entre 2 (entero).
import math #importar libreria de mates
numero=float(input("Introduce un número: ")) 
raiz=math.sqrt(numero)
divison_entera=int(raiz//2)
print("La raíz cuadrada es:",raiz)
print("La raíz cuadrada dividida entre 2 (entero):",(divison_entera))