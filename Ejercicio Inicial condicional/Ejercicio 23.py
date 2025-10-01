#23.  Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.
nota=float(input("introduce la nota: "))
if nota>10 or nota<0:
    print("la nota no es valida")
elif nota>=5 and nota<7:
    print(f"Suficiente, has sacado un {nota}")
elif nota>=7 and nota<8.5:
    print(f"Notable, has sacado un {nota}")
elif nota>=8.5 and nota<=10:
    print(f"Excelente, has sacado un {nota}")
else:
    print(f"Has suspendido, has sacadoun{nota}")