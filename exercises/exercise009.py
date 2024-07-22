"""Realiza la potencia de un número"""

# La potencia de un número es la multiplicacion del mismo número "n" tantas veces
# Se define un número
number = 5

# Se muestra el resultado
print(f"El número al cuadrado es: {number * number}")

# También se puede usar la librería math
import math

# El primer argumento es el número y el segundo argumento es la potencia
print(f"El número al cubo es: {math.pow(number, 3)}")

# También se puede hacer esto de una manera tradicional
counter = 1
pow_number = 1
while counter < 6:
    pow_number *= number
    counter += 1

# Se muestra el resultado
print(f"El número potenciado al 5 es: {pow_number}")
