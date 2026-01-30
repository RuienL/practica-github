#76. A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo

lista1=["a","b","D","x","r","X","3","h","w","2","i"]
listanum=[]
listaletra=[]
listamay=[]
listamin=[]
# a. Cantidad total de valores
cantidad_total = len(lista1)

for x in lista1:
    if x.isnumeric():
        listanum.append(int(x))
    if x.isalpha():
            listaletra.append(x)

listaletra.sort()
listanum.sort()

orden=int(input("Pulse 1 para mostrar normal,2 al revés "))
if orden==1:
    print(listanum)
    print(listaletra)
else:
    print(listanum[::-1])
    print(listaletra[::-1])

