#A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10
num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))
if num2<0 or num2>10 or num1<0 or num1>10:
    print("Uno de los numeros esta fuera de rango")
if num1>num2:
    print("El",num1, "es mayor")
if num1<num2:
    print("El",num2, "es mayor")
else:
    print("Los numeros son iguales")
