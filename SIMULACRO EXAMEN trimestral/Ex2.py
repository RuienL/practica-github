positivos=0
negativo=0
mayorque100=0
for i in range(7):
    num=int(input("introduce un numero"))
    if num>100:
        mayorque100=mayorque100+1
    if num < 0:
        negativo=negativo+num
    elif num>0 and num:
        positivos=positivos+num 
print(f"suma de positivos: {positivos}")
print(f"suma de negativo: {negativo}")
print(f"mayores que 100: {mayorque100}")