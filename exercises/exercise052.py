"""Sumar los números del 1 al 10 con for"""

# Se establece la lista de números
list_numbers = list(range(1, 11))

# Se desarrolla la lógica
# Se establece un resultado en 0
result = 0
for i in list_numbers:
    result += i

# Se muestra el resultado
print(f"La suma es: {result}")
