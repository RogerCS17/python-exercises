"""Verificar si un número es par o impar utilizando if y mod"""

# Se importa la libreria
import random as rnd

# Se define la variable
number = rnd.randint(1, 10)

# Se define la lógica
if number % 2 == 0:
    print(f"El número {number} es par")
else:
    print(f"El número {number} es impar")
