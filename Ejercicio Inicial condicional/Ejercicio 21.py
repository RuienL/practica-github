import math
a=float(input("Ingrese el valor de a: "))
b=float(input("Ingrese el valor de b: "))
c=float(input("Ingrese el valor de c: "))
discriminante=b**2-4*a*c
if discriminante>0:
    raiz1=(-b+math.sqrt(discriminante))/(2*a)
    raiz2=(-b-math.sqrt(discriminante))/(2*a)
    print("el valor x1 es:",raiz1)
    print("el valor x2 es:",raiz2)
else:
    print("La raíz no puede ser un valor negativo")
