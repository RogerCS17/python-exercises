"""Simular un volado o lanzamiento de una moneda"""

# Se importa la librería
import random as rnd

# Se crea un diccionario donde tiene los valores almacenados
dict_coin = {1: "Cara", 2: "Sello"}

# Se pide la usuario que escoge entre cara o sello
print("Juego de cara y sello")
print("1. Cara")
print("2. Sello")
coin = int(input("Que escoge: "))

# Simulación de la moneda3
if coin == 1 or coin == 2:
    if coin == rnd.randint(1, 2):
        print(f"Ganaste. Salió {dict_coin[coin]}")
    else:
        print(f"Perdite. No salió{dict_coin[coin]}")
else:
    print("Debe elegir una opción válida")
