peso=float(input("introduce tu peso en kg:"))
altura=float(input("introduce tu altura en metros:"))
IMC=peso/altura**2
round(IMC,2)
print("tu IMC es:",IMC)
if IMC>=25:
    print("tienes sobrepeso")

