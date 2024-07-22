"""Realiza una multiplicación de dos números y muestra su resultado"""

# Se importa la librería
import random as rnd

# Variables a multiplicar
number01 = rnd.randint(1, 10)
number02 = rnd.randint(1, 10)

# Resultado
result = number01 * number02

# Se muestra el resultado
print(f"El resultado de la multiplicación de {number01} y {number02} es: {result}")
