#28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza 
var1 = (input("Introduce un carácter: "))
if var1.isupper()==True:
    print("El carácter es una letra mayúscula")
if var1.islower()==True:
    print("El carácter es una letra minúscula")
if var1.isdigit()==True:
    print("El carácter es un número")
elif not var1.isalnum():
    print("El carácter es un símbolo")
