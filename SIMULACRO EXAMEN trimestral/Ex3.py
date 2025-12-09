
cifras=int(input("introduce la cantidad de cifras"))
num=input("introduce un número")

if cifras != len(num):
    print("longitud incorrecta")
else:
    producto = 1
    for digit in num:
        producto *= int(digit)
    
    producto_str = str(producto)
    count_pares = sum(1 for d in producto_str if int(d) % 2 == 0)
    
    print(f"Cantidad de cifras pares en el producto: {count_pares}")
    