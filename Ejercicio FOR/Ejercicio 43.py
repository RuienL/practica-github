# Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima por pantalla cada letra
palabra=input("introduce una palabra")
for i in range(palabra):
    print("posición",i+1,palabra[i])