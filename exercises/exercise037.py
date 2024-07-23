"""Calcula el máximo de tres número"""

# Se importa la librería random
import random as rnd

# Se define una lista vacía
list_number = []

# Se agrega números aleatorios a la lista
for number in range(1, 4):
    list_number.append(rnd.randint(1, 20))

# Se calcula el máximo de los 3 números
print(f"El número máximo de los números {list_number} es {max(list_number)}")
