#38. A partir del programa anterior, establece los rangos para que el usuario no pueda introducir notas inferiores a 0 y superiores a 10

num_notas=int(input("Introduce el número de notas"))

for i in range(num_notas):
    nota=float(input(f"Introduce la nota{i+1}"))
    if nota >=5 and nota<=10:
        print("Aprobado")
    elif nota <5 and nota>0:
        print("susupendido")
    else: 
        print("Introduzca una nota válida")

