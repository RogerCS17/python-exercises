"""Imprimir la suma de los números pares del 1 al 10 usando for"""

# Se crea la lista de números
list_numbers = [i for i in range(1, 11) if i % 2 == 0]

# Se crea la lógica
# Se inicia una variable acumulador
acc = 0

# Se recorre los valores de la lista y se van sumando
for i in list_numbers:
    acc += i

# Se muestra el resultado
print(f"La suma es: {acc}")
