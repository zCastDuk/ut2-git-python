num = int(input("¿Qué tabla quieres ver?: "))

for i in range(0, 11, 1):
    print( f"{num:2} x {i:2} = {num * i:3}")

