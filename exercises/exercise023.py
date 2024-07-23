"""Verifica si una palabra es un palíndromo"""

# Se define una variable con un palíndromo
words = ["reconocer", "rosa"]

# Lógica para saber si es un palíndromo
for word in words:
    if word == word[::-1]:
        # Se muestra el resultado
        print(f"La palabra {word} es palindromo")
    else:
        # Se muestra el resultado
        print(f"La palabra {word} no es palindromo")
