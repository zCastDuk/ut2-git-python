import random

secreto = random.randint(1, 20)
intentos = 0

while True:
    numero = int(input("Adivina el número (1-20): "))
    intentos += 1

    if numero == secreto:
        print(f"¡Acertaste en {intentos} intentos!")
        break
    elif secreto > numero:
        print("Es mayor")
    else:
        print("Es menor")