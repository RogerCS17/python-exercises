"""Mostrar los números del 1 al 100, pero reemplazado los múltiplos de 3
por "Fizz" y los múltiplos de 5 por "Buzz" """

# Se crea una lista con los números del 1 al 100
list_numbers = list(range(1, 101))

# Bucle para reemplazar los valores
for index, element in enumerate(list_numbers):
    if element % 15 == 0:
        list_numbers[index] = "FizzBuzz"
    elif element % 3 == 0:
        list_numbers[index] = "Fizz"
    elif element % 5 == 0:
        list_numbers[index] = "Buzz"

# Se muestra la lista
print(list_numbers)
