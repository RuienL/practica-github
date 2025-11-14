#37. Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido.

# Pedir el número de notas
num_notas = int(input("¿Cuántas notas quieres introducir? "))


for i in range(num_notas):
    nota = float(input(f"Introduce la nota {i+1}: "))
    if nota >= 5:
        print("Aprobado")
    else:
        print("Suspendido")
