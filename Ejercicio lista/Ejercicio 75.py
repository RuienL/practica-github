#75. Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por
#pantalla los siguientes resultados:
#a. Cantidad total de valores
#b. Cantidad de números
#c. Cantidad de letras
#d. Cantidad de mayúsculas
#e. Suma de los valores numéricos
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
        listanum1=len(listanum)
    if x.isalpha():
        listaletra.append(x)
        listaletra1=len(listaletra)
    if x.isupper():
        listamay.append(x)
        listamay1=len(listamay)
    if x.islower():
        listamin.append(x)
        listamin1=len(listamin)

suma=sum(listanum)

print(f"a. Cantidad total de valores: {cantidad_total}")
print(f"a. Cantidad total de numeros: {listanum1}")
print(f"a. Cantidad total de letras: {listaletra1}")
print(f"a. Cantidad total de mayuscula: {listamay1}")
print(f"a. Cantidad total de suma: {suma}")




    





