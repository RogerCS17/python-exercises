"""Solicita al usuario ingresa un número e imprime el factorial
de ese número"""

# Se importa la librería
import math

# Se solicita un número al usuario
number = int(input("Digite un número: "))

# Se verifica que sea un número
if type(number) is int:
    # Solución tradicional o clásica
    classic_factorial = 1
    for i in range(1, number + 1):
        classic_factorial *= i
    print(f"El factorial de manhera clásica es: {classic_factorial}")

    # Solución con math
    factorial = math.factorial(number)
    print(f"El factorial de {number} es {factorial}")
else:
    print(f"{number} no es un número")
