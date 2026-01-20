milista=[1,2,3,4,5,6]
milistapor2=[]
maximo=max(milista)
minimo=min(milista)
suma=sum(milista)

print(milista)
print("maximo",maximo)
print("minimo",minimo)
print("suma,",suma)

for x in range (len(milista)): #metodo 1
    calculo=milista[x]*2
    milistapor2.append(calculo)

for x in milista:               #metodo 2
    milistapor2.append(x*2)