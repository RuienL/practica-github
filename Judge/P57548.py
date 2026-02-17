valores=input()
lista=valores.split()

num1=int(lista[0])

num3=0


if len(lista)==1:
    valores1=input()
    lista1=valores1.split()
    num1=int(lista[0])
    num3=int(lista1[0])
    result=num1+num3
    print(result)
else:
    num2=int(lista[1])
    result=num1+num2
    print(result)