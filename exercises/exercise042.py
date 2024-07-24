"""Solicita al usuario ingresar un número N y luego imprime la suma
de todo los números desde 1 hasta N"""

# Se pide al usuario ingresar un número
number = int(input("Digite un número: "))

# Se verifica que sea un número
if type(number) is int:
    # Se crea una lista del número 1 hasta N
    list_number = list(range(1, number + 1))

    # Se suma los elementos
    print(f"La suma de 1 hasta {number} es {sum(list_number)}")

else:
    print(f"{number} no es un número")
