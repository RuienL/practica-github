# Programa que sume los n primeros números naturales. n Lo introduce el usuario.
n = int(input("Introduce un número entero positivo n: "))
suma_bucle = 0
for i in range(1,n+ 1):
    suma_bucle += i
print(f" La suma de los {n} primeros números naturales es: {suma_bucle}")
