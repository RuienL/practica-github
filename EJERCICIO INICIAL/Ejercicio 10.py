##Programa que pida dos números y realice la división mostrando el cociente y el resto de la división. Además, si el resto es 0 debe mostrar un mensaje indicando que el número es par, en caso contrario debe mostrar un mensaje indicando que el número es impar.
num1=float(input("introduce el primer número"))
num2=float(input("introduce el primer número"))
coeficiente=num1/num2
resto=num1%num2
print("el coeficiente es",coeficiente)
print("el resto es",resto)
if resto==0:
    print("el número es par")
else:
    print("el número es impar")
