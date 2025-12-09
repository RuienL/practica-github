inicio=int(input("introduce num1: "))
fin=int(input("introduce num2: "))
incremento=int(input("introduce el incremento: "))

valores = []

for i in range(inicio, fin, incremento):
    if i % 4 == 0:
        continue
    if i % 6 == 0:
        valores.append(f"*{i}*")
    else:
        valores.append(str(i))

print(", ".join(valores))
