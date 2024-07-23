"""Calcula el IMC e interpretarlo"""

# Se crea las variables
weight = float(input("Ingrese su peso: "))
height = float(input("Ingrese su altura: "))

# Se calcula el IMC
imc = weight / (height * height)

# Se verifica para cada caso
match imc:
    case imc if imc < 18.5:
        print(f"Su IMC es {imc} que significa: Bajo peso")
    case imc if imc > 18.5:
        print(f"Su IMC es {imc} que significa: Normal")
    case imc if imc > 25.0:
        print(f"Su IMC es {imc} que significa: Sobrepeso")
    case imc if imc > 30.0:
        print(f"Su IMC es {imc} que significa: Obesidad")
    case _:
        print("Ingrese valores válidos")
