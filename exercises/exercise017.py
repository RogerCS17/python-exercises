"""Extrae una subcadena de una cadena dada"""

# Se define la cadena de texto
word = "Hay golpes en la vida, yo no sé"
searched_word = "golpes"

# Se separa la cadena en subcadenas
array_word = word.split(" ")

# Se verifica si la subcadena se encuentra
if searched_word in array_word:
    # Se muestra el resultado
    print(f"La subcadena extraída es: {searched_word}")
else:
    # Se muestra el resultado
    print(f"No se encontró la subcadena: {searched_word}")
