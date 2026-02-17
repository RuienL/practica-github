lista=input()
names=lista.split()
a=names[0]
b=names[1]
if a>b:
    print(f"{a} > {b}")
elif a<b:
    print(f"{a} < {b}")
else:
    print(f"{a} = {b}")
