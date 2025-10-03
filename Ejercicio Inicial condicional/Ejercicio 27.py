#27.  Mejora el programa anterior para controlar que el valor introducido es una letra y en caso de introducir un número, aparezca un aviso por pantalla
var1 = (input("Introduce un carácter: "))
if var1.isupper()==True:
    print("El carácter es una letra mayúscula")
if var1.islower()==True:
    print("El carácter es una letra minúscula")
if var1.isdigit()==True:
    print("El carácter es un número")
else:
    print("La letra es mayúscula ¿?")
