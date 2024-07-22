"""Calcula el promedio de una lista de números"""

# Se difine la lista con nuestros números
array_numbers = [10, 20, 30, 40, 50]

# Se puede usar las funciones sum y len para resolver el ejercicio
average_array_numbers = sum(array_numbers) / len(array_numbers)

# Se muestra el resultado
print(f"El promedio de los números de la lista es: {average_array_numbers}")

# También se puede resolver de una manera más tradicional
sum_numbers = 0
total_numbers = 0
for number in array_numbers:
    sum_numbers += number
    total_numbers += 1
average_numbers = sum_numbers / total_numbers

# Se muestra el resultado
print(f"El promedio de los números de la lista es: {average_numbers}")
