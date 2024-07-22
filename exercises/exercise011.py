"""Calcula el área de un rectángulo"""

# Se importa la librería
import random as rnd

# Se define las variables
base = rnd.randint(1, 10)
height = rnd.randint(1, 10)

# Se calcula el área
area = base * height

# Se muestra el resultado
print(f"Base: {base}, Altura: {height} y el área del rectángulo es: {area:.2f}")
