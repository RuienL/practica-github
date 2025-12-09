#55. Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While
total_suma = 0
contador = 0

while total_suma < 50:
    var1=int(input("introduce el primer numero"))
    var2=int(input("introduce el segundo numero"))
    resultado=var1+var2
    total_suma += resultado
    contador += 1
    print(f"el resultado es {resultado} ")
    print(f"suma total es de {total_suma} ")
    print(f"Número de repeticiones: {contador}")
    if total_suma % 2 == 0:
        print("Progrmama finalizado")
        break
else:
    print("Programa finalizado")
