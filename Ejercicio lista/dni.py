numerodni=[]
letradni=[]
dni=[]
tabla_letras="TRWAGMYFPDXBNJZSQVHLCKE"
intento=0
error_len=0
continuar="s"
error=[]
dnicorrecto=[]
errores_longitud=0
errores_numero=0
no_existentes=0

while continuar=="s":
    numdni=input("Introduce el DNI ")
    if len(numdni)<8 or len(numdni)>8:
        print("Error la longitud")
        numdni=input("Introduce el DNI ")
        errores_longitud=errores_longitud+1
        intento=intento+1
    elif not numdni.isnumeric():
        print("El DNI tiene que ser numerico")
        numdni=input("Introduce el DNI ")
        errores_numero=errores_numero+1
        intento=intento+1
    else:
        dni=int(numdni)
        resto=dni%23
        if resto<0 or resto>22:
            print("Error: El resto obtenido no es válido")
            intento=intento+1
            no_existentes=no_existentes+1
            error.append(dni)
        else:
            letra=tabla_letras[resto]
            print(f"DNI completo: {dni}-{letra}")
            intento=intento+1
            dnicorrecto.append(dni)
        continuar=input("¿Deseas calcular otro DNI? (s/n):")

if continuar=="n":
    while True:
        print("1. Listar DNI correctos ordenados de menor a mayor")
        print("2. Listar DNI incorrectos ordenados de menor a mayor")
        print("3. Número total de errores")
        print("4. Número total de DNIs correctos")
        print("5. Porcentajes de DNIs")
        print("6. Salir")
        opcion=input("Selecciona una opción (1-6):")
        if opcion=="1":
            dnicorrecto.sort()
            print("DNI correctos ordenados:", dnicorrecto)
        elif opcion=="2":
            error.sort()
            print("DNI incorrectos ordenados:", error)
        elif opcion=="3":
            total_errores = errores_longitud + errores_numero + no_existentes
            print(f"Número total de errores: {total_errores}")
        elif opcion=="4":
            print(f"Número total de DNIs correctos: {len(dnicorrecto)}")
        elif opcion=="5":
            total = len(dnicorrecto) + errores_longitud + errores_numero + no_existentes
            if total > 0:
                porcentaje_correctos = (len(dnicorrecto) / total) * 100
                porcentaje_incorrectos = (no_existentes / total) * 100
                porcentaje_longitud = (errores_longitud / total) * 100
                porcentaje_numero = (errores_numero / total) * 100
                porcentaje_no_existentes = (no_existentes / total) * 100
                print(f"Porcentaje de DNIs correctos: {porcentaje_correctos:.2f}%")
                print(f"Porcentaje de DNIs incorrectos: {porcentaje_incorrectos:.2f}%")
                print(f"Porcentaje de errores de longitud: {porcentaje_longitud:.2f}%")
                print(f"Porcentaje de errores de número: {porcentaje_numero:.2f}%")
                print(f"Porcentaje de no existentes: {porcentaje_no_existentes:.2f}%")
            else:
                print("No hay DNIs para calcular porcentajes")
        elif opcion=="6":
            break
        else:
            print("Opción no válida")

    


        
