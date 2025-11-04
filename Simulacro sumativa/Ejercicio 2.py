var1=float(input("Introduce un número: "))
var2=float(input("Introduce otro número: "))
var3=float(input("Introduce otro número más: "))
palabra1=input("Introduce una palabra: ")
palabra_minus=palabra1.lower()
print(f"{palabra_minus}")
suma=var1+var2+var3
round(suma,3)
print(f"{suma}")
media=suma/3
round(media,3)
print(f"{media}")
producto=var1*var2*var3
round(producto,3)
print(f"{producto}")
if suma>producto:
    print("La suma es mayor que el producto?:True")
else:
    print("La suma es mayor que el producto?:False")