#25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.
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