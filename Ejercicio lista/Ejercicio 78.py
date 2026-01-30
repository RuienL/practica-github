#78. A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir
lista1=["a","b","D","x","r","X","3","h","w","2","i"]
pregunta="s"


while pregunta=="s":
    for x in lista1:
        if eliminar in lista1:
            lista1.remove(eliminar)
            print(lista1)
            pregunta=input("Desea seguir s/n ")
            
            eliminar=input("Introduce lo que quieres eliminar ")
        if eliminar not in lista1:
            print("No encontrado ")
            eliminar=input("Introduce lo que quieres eliminar ")
            


