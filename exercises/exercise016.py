"""Calcula 2 elevado a la 4° potencia sin utilizar el operador **"""

# Se define las variables
number = 2
pow = 4

# Bucle while para hallar la potencia
counter = 1
result = 1
while counter < pow + 1:
    result *= number
    counter += 1

# Se muestra el resultado
print(f"El número {number} elevado a la {pow} potencia es: {result}")
