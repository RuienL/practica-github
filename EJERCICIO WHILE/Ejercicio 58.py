#58. Modifica el programa anterior para que tengas 3 intentos. Utiliza while
import random
num_random=random.randint(1,5)
oprtunidad=3
num=int(input("Introduce 1-5 "))
while num>5 or num<0:
    oprtunidad=oprtunidad-1
    if oprtunidad==0:
        print("has agotado las 3 oprtunidades")
        break 
    else:print("Introduzca un numero correcto")
    num=int(input("Introduce 1-5 "))
while num<5.1 and num>0:
        oprtunidad=oprtunidad-1
        if oprtunidad==0:
            print("has agotado las 3 oprtunidades")
            break
        if num==num_random:
            print("Acertado")
            break
        else: 
            num=int(input("Introduce 1-5 "))
