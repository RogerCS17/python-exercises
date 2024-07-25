"""Hacer un menú de opciones que incluya la opción de salir del programa"""

# Se crea la lógica
# Mientras es True, se verá el menú hasta que se salga del programa
while True:
    # Menú
    print("MENÚ")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Opción 4")
    print("5. Opción 5")
    print("0. SALIR")
    opc = input("Ingrese su opción")
    # Estructura de control
    match opc:
        case "1":
            print("Hola 1")
        case "2":
            print("Hola 2")
        case "3":
            print("Hola 3")
        case "4":
            print("Hola 4")
        case "5":
            print("Hola 5")
        case "0":
            print("Saliendo del programa")
            exit()
        case _:
            print("Digite una opción válida")
