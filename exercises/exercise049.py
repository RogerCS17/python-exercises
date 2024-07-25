"""Simular el lanzamiento de un dado hasta obtener un 6"""

# Se importa la librería
import random as rnd

# Contexto del juego
print("Juego de Dado")
print("Debe jugar hasta que le salga un 6")
print("Presione Enter para jugar")
input()

# Se genera un número aleatorio
die = rnd.randint(1, 6)

# Contador para saber en que intento le salió el número 6
counter = 1

# Bucle que termina cuando sale el número 6
while die != 6:
    counter += 1
    print(f"Salió el número {die}. Presione enter para tirar de nuevo")
    input()
    die = rnd.randint(1, 6)

# Resultado
print(f"Felicidades. Has ganado en el intento número {counter}")
