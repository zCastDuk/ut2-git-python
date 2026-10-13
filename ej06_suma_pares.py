num = int(input("Suma los pares hasta: "))
suma = 0

for i in range(0, num + 1):
    if i % 2 != 0:
        continue
    suma += i

print(f"La suma total es {suma}")