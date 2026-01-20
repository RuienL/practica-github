#74. A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de entre las 2 listas.
lista1=["casa","mesa","sal","sol","agua"]
lista2=["casa","luz","tres","tren","sol","pan"]
repetidas=[]
norepetidas=[]
for item in lista1:
    if item in lista2:
        repetidas.append(item)
        
for item in lista2:
    if item not in lista1:
        norepetidas.append(item)

for item in lista1:
    if item not in lista2:
        norepetidas.append(item)

print(repetidas)
print(norepetidas)