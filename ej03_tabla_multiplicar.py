numero = int(input("¿Qué tabla quieres ver?: "))

for i in range(0, 11, 1):
    print( f"{numero:2} x {i:2} = {numero * i:3}")

