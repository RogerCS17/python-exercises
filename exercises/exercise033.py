"""
Determina si un año es bisiesto
Regla de negocio
- Divisible por 4
- No divisible por 100
- Divisible por 400
"""

# Se define la variable
year = 1900

# Se crea la lógica
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"El año {year} es bisiesto")
else:
    print(f"El año {year} no es bisiesto")
