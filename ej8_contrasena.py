CLAVE = "daw2026"
intentos = 5

while intentos > 0:
    contrasena = input("Contraseña: ")

    if contrasena == CLAVE:
        print("Acceso concedido")
        break

    intentos -= 1
    print(f"Incorrecta. Te quedan {intentos} intentos")
else:
    print("Cuenta bloqueada.")
