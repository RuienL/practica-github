#71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en esta lista no deben almacenarse las letras que se han introducido repetidas
sinduplicados=[]
lista=[]
listabasura=[]
continuar="s"

while continuar=="s":
    letra=input("Introduce una letra ")
    if letra.isnumeric():
        listabasura.append(letra)
        letra=input("Introduce una letra ")
    else:    
        lista.append(letra)
        continuar=input("Desear seguir s/n ")



sinduplicados=list(set(lista))
print(sinduplicados)
    