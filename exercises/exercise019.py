"""Cuenta las ocurrencias de un carácter expecífico en una cadena"""

# Se define la cadena de texto
word = "Pienso, luego existo"
char = "o"

# Con el método count Se puede hallar las ocurrencias del carácter
print(
    f"El carácter '{char}' en la cadena '{word}' esta presente: {word.count(char)} veces"
)
