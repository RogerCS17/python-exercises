"""Verificar si una cadena  es mayor o igual a 10 caracteres"""

# Se define la variable
word = "Roger"

# Con la función len() se puede saber la longitud de la cadena
if len(word) > 10:
    print(f"La palabra {word} tiene más de 10 caracteres")
else:
    print(f"La palabra {word} tiene menos de 10 caracteres")
