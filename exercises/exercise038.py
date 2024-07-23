"""Determina si un número es divisible entre 5 y 7"""

# Se importa la librería random
import random as rnd

# Se crea la variable
number = rnd.randint(1, 100)

# Se crea la lógica
if number % 35 == 0:
    print(f"El número {number} es divisible entre 5 y 7")
else:
    print(f"El número {number} no es divisible entre 5 y 7")
