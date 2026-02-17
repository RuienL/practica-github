#73. Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se repiten y cuales no
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

print(repetidas)
print(norepetidas)