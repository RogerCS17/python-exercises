"""Genera una lista de números del 1 al 100"""

# Se crea una lista vacía
list_empty = []

# Con un ciclo for se puede crear lso elementos
for number in range(1, 101):
    list_empty.append(number)

# Se muestra el resultado
print(f"{list_empty}")

# También Se puede hacer con comprensión de listas
comprehension_list_empty = [x for x in range(1, 101)]

# Se muestra el resultado
print(f"{comprehension_list_empty}")

# También otra manera es castear el range() a una lista
list_range = list(range(1, 101))
print(f"{list_range}")
