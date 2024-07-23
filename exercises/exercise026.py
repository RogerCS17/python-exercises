"""Intercambia los valores de dos variables con asignación múltiple"""

# Se define dos variables
number01 = 10
number02 = 20

# Se meustra el resultado original
print(f"Número 1: {number01} y número 2: {number02}")

# Ahora con asignación múltiple, se intercambia los valores
number01, number02 = number02, number01

# Se muestra el resultado con los valores intercambiados
print(f"Número 1: {number01} y número 2: {number02}")
