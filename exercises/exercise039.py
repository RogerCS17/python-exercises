"""Verifica si la palabra ingresada es python"""

# Se crea la variable que contendra la pabra "python"
keyword = "python"

# Se ingrsa una palabra por parte del usuario
word_input = input("Ingrese la palabra clave: ")

# Se verifica
if word_input == keyword:
    print(f"Correcto, la palabra clave es {keyword}")
else:
    print(f"Incorrecto, esa no es la palabra clave")
