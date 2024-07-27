"""Multiplicar todos los elementos de una lista por 2"""

# Se importa la librería random
import random as rnd

# Se crea la lista de números
list_random_numbers = [rnd.randint(1, 11) for i in range(1, rnd.randint(1, 5))]

# Se multiplica cada elemento de la lista por 2
for i in list_random_numbers:
    print(f"{i} x 2 = {i*2}")
