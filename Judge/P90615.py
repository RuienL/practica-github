valores=input()
lista=valores.split()
a=int(lista[0])
b=int(lista[1])
c=int(lista[2])

if a>b and a>c:
    print(a)
    
if b>a and b>c:
    print(b)
if c>a and c>b:
    print(c)

if a == b and a>c:
    print(a)

if a == c and a>b:
    print(a)

if a == b and a == c:
    print(a)

if b == c and b>a:
    print(b)

