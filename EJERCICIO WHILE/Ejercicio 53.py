#53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las sumas y el número de repeticiones. Con While
total_suma = 0
contador = 0
var1=int(input("introduce el primer numero"))
var2=int(input("introduce el segundo numero"))
resultado=var1+var2
total_suma += resultado
contador += 1
print(f"el resultado es {resultado} ")
opcion=int(input("Si quieres seguir introdcue el número 1 sino introduce cualquier valor"))
while opcion ==1:
    var1=int(input("introduce el primer numero"))
    var2=int(input("introduce el segundo numero"))
    resultado=var1+var2
    total_suma += resultado
    contador += 1
    print(f"el resultado es {resultado} ")
    opcion=int(input("Si quieres seguir introdcue el número 1 sino introduce cualquier valor"))
else:
    print("Programa finalizado")
    print(f"Total de las sumas: {total_suma}")
    print(f"Número de repeticiones: {contador}")
