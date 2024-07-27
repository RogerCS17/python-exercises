"""Pide al usuario e imprime una tabla de división desde ese número hasta 1"""

# Se pide al usuario ingresa un número
number = int(input("Digite un número: "))

# Se verifica que sea un número
if type(number) == int:
    for i in range(number, 0, -1):
        print(f"{number} entre {i} es {number/i}")
else:
    print("Debe digitar un número válido")
