"""Imprimir los números pares del 2 al 10 con ciclo for"""

# Se crea una lista con los números pared del 2 al 10
even_numbers = [i for i in range(1, 11) if i % 2 == 0]

# Se imprime los valores de la lista
for i in even_numbers:
    print(i)
