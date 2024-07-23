"""Pide un caracter y determina si es una vocal"""

# Se define la lista de vocales
list_vocal = ["a", "e", "i", "o", "u"]

# Se pide al usuario que introduzca una letra
vocal = input("Ingrese una vocal: ")

# Se crea la lógica
if vocal.lower() in list_vocal:
    print(f"La letra {vocal} si es una vocal")
else:
    print(f"La letra {vocal} no es una vocal")
