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
