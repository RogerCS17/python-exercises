"""Imprimir los elementos de una lista dada"""

# Se importa la librería
import random as rnd

# Se crea una lista de números aleatorios
random_numbers = [rnd.randint(0, 20) for i in range(0, rnd.randint(1, 10))]

# Se muestra los elementos de la lista
for i in random_numbers:
    print(i)
