#61. A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es superior o igual a 40
num=int(input("Introduce un número "))
i=1
while num*i<=40:
    print(f"{num} * {i} = {num*i}")
    i+=1