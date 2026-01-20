#73. Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se repiten y cuales no
lista1=["casa","mesa","sal","sol","agua"]
lista2=["casa","luz","tres","tren","sol","pan"]
repetidas = [item for item in lista1 if item in lista2]
norepetidas = [item for item in lista1 if item not in lista2]

print(repetidas)
print(norepetidas)