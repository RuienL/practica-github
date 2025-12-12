#60. Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. Utiliza únicamente el while
num = int(input("Introduce un número"))
i = 1
while i <= 10:
    print(f"{num} * {i} = {num * i}")
    i += 1
