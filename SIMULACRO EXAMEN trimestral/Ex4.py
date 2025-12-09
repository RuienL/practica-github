valor=100
numero=int(input("introduce un numero"))
while valor>50<150:
    print(f"{valor}")
    numero=int(input("introduce un numero"))
    if numero%2==0:
        valor=valor/2
        print(f"{valor}")
    elif numero%2!=0:
        valor=valor+numero
        print(f"{valor}")
    elif numero%3==0:
        valor=valor-5
        print(f"{valor}")

