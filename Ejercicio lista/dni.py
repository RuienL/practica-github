numerodni=[]
letradni=[]
dni=[]
intento=0
error_len=0


numdni=input("Introduce el DNI ")
if len(numdni)<8 or len(numdni)>8:
    print("Error la longitud")
    numdni=input("Introduce el DNI ")
    error_len=error_len+1
    intento=intento+1
if len(numdni)==8:
    for x in numdni:
        if x.isnumeric():
            numerodni.append(int(x))
        
