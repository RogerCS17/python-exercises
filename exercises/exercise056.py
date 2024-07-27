"""Listar los 10 números y calcular el cuadrado de cada uno e imprimirlos"""

# Se crea la lista de números
list_numbers = list(range(1, 11))

# Se halla el cuadrado para cada número
list_square_numbers = [i**2 for i in list_numbers]

# Ahora se usa zip para asociar cada número con su cuadrado
for i in list(zip(list_numbers, list_square_numbers)):
    print(i)
