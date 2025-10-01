##Programa que pida el peso y la altura de una persona y calcule su índice de masa corporal (IMC). El IMC se calcula dividiendo el peso en kg entre la altura en metros al cuadrado. Si el IMC es superior o igual a 25, debe mostrar un mensaje indicando que la persona tiene sobrepeso.
peso=float(input("introduce tu peso en kg:"))
altura=float(input("introduce tu altura en metros:"))
IMC=peso/altura**2
round(IMC,2)
print("tu IMC es:",IMC)
if IMC>=25:
    print("tienes sobrepeso")

