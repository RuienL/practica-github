#26. Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.

var1 = (input("Introduce un carácter: "))
if var1.isupper()==True:
    print("El carácter es una letra mayúscula")
if var1.islower()==True:
    print("El carácter es una letra minúscula")
else:
    print("La letra es mayúscula ¿?")


  