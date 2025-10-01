#Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.
nota=float(input("introduce la nota: "))
if nota>10 or nota<0:
    print("la nota no es valida")
elif nota>=5:
    print(f"Has aprobado, has sacado un {nota}")
else:
    print(f"Has suspendido, has sacadoun{nota}")
