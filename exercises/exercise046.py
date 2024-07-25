"""Solicita al usuario ingresar un número y cuenta cuantos dígitos tiene"""

# Se pide al usuario ingrsar un número
try:
    # Se verifica si es un número
    number = int(input("Digite un número: "))
    print(f"La cantidad de digitos de el número es: {len(str(number))}")

except Exception as e:
    print(f"Debe digitar un número, error: {e}")
