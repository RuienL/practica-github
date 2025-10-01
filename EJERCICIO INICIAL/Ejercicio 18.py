##Programa que pida el número de menores de 18 años y el número de mayores de 18 años, y calcule el precio total de las entradas (los menores de 18 años pagan la mitad y los mayores de 18 años pagan el 90% del precio total).
precio=12
menor=int(input("introduce el número de los menores de 18 años:"))
mayor=int(input("intrtodcue el número de los mayores de 18 años:"))
precio_menor=precio*0.5, 
round(precio_menor,3)
precio_mayor=precio*0.9
round(precio_mayor,3)
total_menor=menor*precio_menor
total_mayor=mayor*precio_mayor
print("el precio total de cine de",menor,"menores de 18 años es:",total_menor)
print("el precio total de cine de",mayor,"mayores de 18 años es:",total_mayor)