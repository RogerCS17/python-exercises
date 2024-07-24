"""Imprime la tabla de multiplicar de un número ingresado por el usuario"""

# Se pide al usuario ingresa un número
number = int(input("Digite un número: "))

# Se crea la lógica
for i in range(1, 13):
    # Se muestra el resultado
    print(f"{number} x {i} = {number * i}")
