#59. Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe mostrarse por pantalla un mensaje y el número de intentos
import random
num_aleatorio=random.randint(1,1000)
num=int(input("Introudce un numero "))
intento=0
while num>=1 and num<=1000:
    if num==num_aleatorio:
        intento=intento+1
        print("Acertado")
        print(f"{intento} intentos")
    elif num>num_aleatorio:
        print("Es menor")
        intento=intento+1
        num=int(input("Introudce un numero "))
    elif num<num_aleatorio:
        print("Es mayor")
        intento=intento+1
        num=int(input("Introudce un numero "))
