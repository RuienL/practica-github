nombre=input("Introduce tu nombre: ")
nombre_mayus=nombre.upper()
edad=int(input("Introduce tu edad: "))
año_actual=2025
futuro=año_actual+(100-edad)
if edad<0 or edad> 100:
    print("Edad incorrecta")
else:
    print(f"Hola,{nombre_mayus} cumplirás 100 años en el año {futuro}")
