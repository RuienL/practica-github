def validar_password(password):
    # Verificar longitud
    if not (6 <= len(password) <= 8):
        return False

    # Inicializar contadores
    num_1_5 = 0
    num_6_9 = 0
    minusculas = 0
    mayusculas = 0
    simbolos = 0
    simbolos_validos = {'*', '_', '@', '&', '/', '#'}

    for char in password:
        if char.isdigit():
            if '1' <= char <= '5':
                num_1_5 += 1
            elif '6' <= char <= '9':
                num_6_9 += 1
        elif char.islower():
            minusculas += 1
        elif char.isupper():
            mayusculas += 1
        elif char in simbolos_validos:
            simbolos += 1

    # Verificar condiciones
    if num_1_5 >= 2 and num_6_9 >= 1 and minusculas >= 2 and mayusculas >= 1 and simbolos >= 2:
        return True
    return False

# Programa principal
password = input("Introduce la contraseña: ")
if validar_password(password):
    print("Contraseña válida")
