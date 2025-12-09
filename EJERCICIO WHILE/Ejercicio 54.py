#54. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el mensaje del acumulado es singular o plural.. . Con While
total_suma = 0
contador = 0

while total_suma<50:
    var1=int(input("introduce el primer numero"))
    var2=int(input("introduce el segundo numero"))
    resultado=var1+var2
    total_suma += resultado
    contador += 1
    print(f"el resultado es {resultado} ")
    print(f"suma total es de {total_suma} ")
    print(f"Número de repeticiones: {contador}")
else:
    print("Programa finalizado")
