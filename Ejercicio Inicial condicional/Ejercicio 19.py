# Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales
num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))
if num1>num2:
    print("El",num1, "es mayor")
elif num1<num2:
    print("El",num2, "es mayor")
else:
    print("Los numeros son iguales")