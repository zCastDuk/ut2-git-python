
CLAVE = "daw2026"
intentos = 5

while intentos > 0:
    contrasena = input("Contraseña: ")

    if len(contrasena) < 6 or not any(c.isdigit() for c in contrasena):
        print("La contraseña debe tener al menos 6 caracteres y un número.")
        continue

    if contrasena == CLAVE:
        print("Acceso concedido")
        break

    intentos -= 1
    print(f"Incorrecta. Te quedan {intentos} intentos")
else:
    print("Cuenta bloqueada.")
