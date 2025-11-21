#52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por pantalla. El programa preguntará si deseas o no repetir la operación. Con While

var1=int(input("introduce el primer numero"))
var2=int(input("introduce el segundo numero"))
resultado=var1+var2
print(f"el resultado es {resultado} ")
opcion=int(input("Si quieres seguir introdcue el número 1 sino introduce cualquier valor"))
while opcion ==1:
    var1=int(input("introduce el primer numero"))
    var2=int(input("introduce el segundo numero"))
    resultado=var1+var2
    print(f"el resultado es {resultado} ")
    opcion=int(input("Si quieres seguir introdcue el número 1 sino introduce cualquier valor"))
else:
    print("Programa finalizado")

