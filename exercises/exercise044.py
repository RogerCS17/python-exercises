"""
Genera un número aleatorio entre 1 y 10. Luego, pide al usuario
adivinar el número hasta que lo haga correctamente
"""

# Se importa la librería
import random as rnd

# Se genera un número aleatorio
random_number = rnd.randint(1, 10)

# Se crea la variable en donde se guardará el número ingresado
number = None

# Se crea la lógica
while random_number != number:
    number = int(input("Digite un número: "))

# Se muestra el resultado
print(f"Correcto. El número es {random_number}")
