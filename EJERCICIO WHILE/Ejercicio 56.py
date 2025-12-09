#56. Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la realización de un pedido, si quiere gestionar otro. El establecimiento contempla los siguientes descuentos: Si el total a pagar es entre 20 y 30 euros, se aplica un descuento del 5% Si el total a pagar es superior a 30 euros, se aplica un descuento del 15% Una vez se finaliza la introducción de todos los pedidos de un cliente, debe aparecer por pantalla: • El número de pedidos realizados • Total a pagar. • Total con IVA (10%) • Total con el descuento aplicado.
print("MENU")
print("1. Bocadillo de calamares- 9 €")
print("2. Bocadillo de chistorra - 4.5€")
print("3. Bikini de jamón - 2.5 €")
print()
print("ACOMPAÑAMIENTO")
print("1. Patatas finas - 1.5 €")
print("2. Patatas gruesas - 1.75 €")
print("1. Patatas finas - 1.5 €")
print()
print("BEBIDAS")
print("1. Coca cola - 2 €")
print("2. Acuarius - 1.5 €")
print("3. Agua - 1 €")
num_pedidos=1
total_pagar=0
seguir="s"
while seguir=="s":
    opcion1=int(input("Introudzca la opción preferida 1 "))
    if opcion1==1:
        total_pagar=total_pagar+9
    if opcion1==2:
        total_pagar=total_pagar+4.5
    if opcion1==3:
        total_pagar=total_pagar+2.5
    opcion2=int(input("Introudzca la opción preferida 2 "))
    if opcion2==1:
        total_pagar=total_pagar+1.5
    if opcion2==2:
        total_pagar=total_pagar+1.75
    if opcion2==3:
        total_pagar=total_pagar+1.5
    opcion3=int(input("Introudzca la opción preferida 3 "))
    if opcion3==1:
        total_pagar=total_pagar+2
    if opcion3==2:
        total_pagar=total_pagar+1.5
    if opcion3==3:
        total_pagar=total_pagar+1
    seguir=input("desea continuar?")
    total_pagar_iva=total_pagar*1.10
    total_descontado5=total_pagar_iva*0.95
    total_descontado15=total_pagar_iva*0.85
    if seguir=="n":
        print(f"Número de pedidos {num_pedidos}")
        print(f"Número precio {round(total_pagar,2)}")
        print(f"Número precio con IVA {round(total_pagar_iva,2)}")
        if total_pagar_iva>=20 and total_pagar_iva<=30:
            print(f"precio total descontado 5% {round(total_descontado5,2)}")
        if total_pagar_iva>30:
            print(f"precio total descontado 15% {round(total_descontado15,2)}")
    else:
        seguir=="s"
        num_pedidos=num_pedidos+1

    
    
    