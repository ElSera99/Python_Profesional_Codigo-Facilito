# Es importante siempre documentar la función mediante docstring
# Se puede acceder al docstring de una función mediante el atributo .__doc__
# El docstring siempre irá en triples comillas dobles 

# Ejemplo de documentación
def suma(num1, num2):

    # Ejemplo de documentación:

    """
    La función suma dos números enteros.

    Argumentos:
    numero_1(int)
    numero_2(int)

    Se retorna la suma de los parámetros.

    TODO:
        *
    """

    return num1 + num2

# Acceder al docstring mediante el atributo
print(suma.__doc__)
print(help(suma))