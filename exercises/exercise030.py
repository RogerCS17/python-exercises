"""Elimina duplicados de una lista"""

# Se define la lista
array = [1, 2, 3, 3, 2, 5, 5, 5, 5, 6]

# Se muestra la lista
print(f"Lista original: {array}")

# Para eliminar los duplicados, se convierte a un conjunto
array_without_duplicate = list(set(array))

# Se muestra el resultado
print(
    f"Lista sin duplicados: {array_without_duplicate} y es de tipo {type(array_without_duplicate)}"
)
