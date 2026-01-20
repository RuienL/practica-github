#72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y no deben almacenarse en la lista
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