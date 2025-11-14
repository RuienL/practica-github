#40. Crea un programa que cuente todos los números pares hasta el número 50
numpar=0
numimpar=0
lista=50
for i in range(1,51):
    if (i)%2==0:
        numpar=numpar+1
    else:
        numimpar=numimpar+1
print(f"Los pares son{numpar}")        
print(f"Los impares son{numimpar}")   