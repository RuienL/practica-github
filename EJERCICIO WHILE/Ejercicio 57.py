#57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa debe controlar si el usuario introduce un número no comprendido entre 1 y 5
import random
num_random=random.randint(1,5)
num=int(input("Introduce 1-5 "))
if num>5 or num<0:
    print("Introduzca un numero correcto")
    num=int(input("Introduce 1-5 "))
while num<5.1 and num>0:
        if num==num_random:
            print("Acertado")
            break
        else: 
            num=int(input("Introduce 1-5 "))
