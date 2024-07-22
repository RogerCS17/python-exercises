"""Convierte un número decimal a un número entero"""
# Se importa la librería
import random as rnd

# Se define la variable decimal
decimal_number = rnd.random()

# Se convierte a entero con la función round()
print(f"Número original: {decimal_number}")
print(f"El número decimal {decimal_number} a entero es: {round(decimal_number)}")
