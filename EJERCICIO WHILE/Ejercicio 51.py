#51. A partir del programa anterior, modifica el código para que sea el usuario quién introduzca el número de veces que desea que repita la frase Buenos días. Con While

contador=int(input("introduce el n de veces"))
while contador>0:
    for i in range(contador):
        print("buenos dias")
        contador=contador-1