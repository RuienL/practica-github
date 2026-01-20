#69. Realiza un programa que permita introducir una cantidad exacta de números, cada número se irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números ordenados de menor a mayor.
cantidad=int(input("Introduce la cantidad deseada"))
milista=[]
for i in range(cantidad):
    var=int(input("Introduce un numero"))
    milista.append(var)
    
milista.sort()
print(milista)