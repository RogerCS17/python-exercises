"""Verificar si un número es positivo, negativo o cero"""

# Se importa la libreria
import random as rnd

# Se define la variable
number = rnd.randint(-10, 10)

# Se define la lógica
match (number):
    case number if number < 0:
        print(f"El número {number} es negativo")
    case number if number > 0:
        print(f"El número {number} es positivo")
    case number if number == 0:
        print(f"El número {number} es cero")
    case _:
        print("Ingrese un número")
