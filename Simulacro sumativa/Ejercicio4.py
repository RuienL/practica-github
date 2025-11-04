print("escoja opción 1 al 4")
print("Opción|Tarifa|Precio€kWh|Descuento")
print("1|Tarifa noctuna|0.158|5%")
print("2|Tarifa Plana|0.192|0%")
print("3|Tarifa solar|0.143|8%")
print("1|Tarifa ecológico|0.170|10%")
opcion=int(input("Elija una opción: "))
if opcion>4 or opcion<1:
    print("Opción no válida")
elif opcion==1:
    consumo=float(input("Introduzca el consumo en kWh: "))
    precio=0.158*consumo
    descuento=precio*0.05
    total=precio-descuento
    print(f"el precio a pagar es de {round(precio,2)}€")
    print(f"el precio con descuento a pagar es de {round(total,2)}€")
elif opcion==2:
    consumo=float(input("Introduzca el consumo en kWh: "))
    precio=0.192*consumo
    descuento=precio*0
    total=precio-descuento
    print(f"el precio a pagar es de {round(precio,2)}€")
    print(f"el precio con descuento a pagar es de {round(total,2)}€")    
elif opcion==3:
    consumo=float(input("Introduzca el consumo en kWh: "))
    precio=0.143*consumo
    descuento=precio*0.08
    total=precio-descuento
    print(f"el precio a pagar es de {round(precio,2)}€")
    print(f"el precio con descuento a pagar es de {round(total,2)}€")
elif opcion==4:
    consumo=float(input("Introduzca el consumo en kWh: "))
    precio=0.170*consumo
    descuento=precio*0.10
    total=precio-descuento
    print(f"el precio a pagar es de {round(precio,2)}€")
    print(f"el precio con descuento a pagar es de {round(total,2)}€")


