#39. Programa que pida n números y que, tras introducir el último número, debe aparecer por pantalla el número total de positivos, negativos y número de 0.
num=int(input("Introduce la cantidad de números a introducir"))
postivo=0
negativo=0
cero=0
for i in range(num):
    varnum=int(input(f"introduce el número {i+1} "))
    if varnum>0:
       postivo=postivo+1
    elif varnum<0:
        negativo=negativo+1
    else:
        cero=cero+1
print(f"la cantidad es postivo es de {postivo}, negativos {negativo} y ceros son {cero}")
    
