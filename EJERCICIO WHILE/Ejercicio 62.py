#62. Realiza un programa que pida dos números por teclado y presente por pantalla qué números hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo.
num1 = int(input("Introduce número 1 "))
num2 = int(input("Introduce número 2 "))


# Determinar el rango
if num1 > num2:
    start = num2
    end = num1
else:
    start = num1
    end = num2

pares = ""
impares = ""

for i in range(start, end + 1):
    if i % 2 == 0:
        if pares:
            pares += ", "
        pares += str(i)
    else:
        if impares:
            impares += ", "
        impares += str(i)

print("Números pares en el rango:", pares)
print("Números impares en el rango:", impares)
