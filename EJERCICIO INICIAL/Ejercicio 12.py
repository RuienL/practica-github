#Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.
lado=float(input("introduce el valor numérico de un lado del trapecio isóceles"))
basemayor=float(input("introduce el valor numérico de un base mayor del trapecio isóceles"))
basemenor=float(input("introduce el valor numérico de un base menor del trapecio isóceles"))
altura=float(input("introduce el valor numérico de una altura del trapecio isóceles"))
area=(basemayor+basemenor)*altura/2
perimetro=basemayor+basemenor+2*lado
print("el área del trapecio isóceles es:",area)
print("el perímetro del trapecio isóceles es:",perimetro)
#Ejercicio 12: Calcular el área y perímetro de un trapecio isóceles
#(se proporcionan la longitud de un lado, la base mayor, la base menor y la altura).
