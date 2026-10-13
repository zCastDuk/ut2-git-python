
menu = "\n1. Saludar \n2. Despedirse \n3. Salir"
print(menu)

op = input("Introduce una opción del menú: ")
match op:

    case "1":
        print("Hola")
        
    case "2":
        print("Adiós")
        
    case "3":
        print("Saliendo...")
        
    case _:
        print("Opción no válida")
        

