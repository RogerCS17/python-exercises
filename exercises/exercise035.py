"""Comprueba si un número está en el rango del 1 al 100"""

# Se importa la librería random
import random as rnd

# Se define la variable
number = rnd.randint(-50, 150)

# Se crea la lógica
if number in range(1, 101):
    print(f"El número {number} se encuentra entre el 1 y 100")
else:
    print(f"El número {number} no se encuentra entre el 1 y 100")
