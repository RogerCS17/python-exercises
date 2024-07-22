"""Crea una cadena de texto y muestra su longitud"""

# Variable de cadena de texto
word = "Roger"

# Con la función len, Se puede hallar su longitud
print(f"La longitud de la cadena de texto es: {len(word)}")

# Se puede contar también iterando sobre la cadena
# Contador
counter = 0
for char in word:
    counter += 1

# Se muestra el resultado
print(f"La longitud de la cadena de texto es: {counter}")
