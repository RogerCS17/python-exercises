"""Combia dos pares de listas usando la función zip()"""

# Se define dos listas
array = [1, 2, 3, 4, 5]
array_even = [x * 2 for x in array]

# Se muestra las listas originales
print(f"Lista: {array}")
print(f"Lista par: {array_even}")

# Para combinar 2 lista, Sse usa la función zip()
print(f"La combinación de estas lista es: {list(zip(array,array_even))}")
