# Puede probarse el comportamiento de una función con ayuda de los docstring y comentarios

import doctest


def suma(num1, num2):

    # Ejemplo de documentación:

    """
    La función suma dos números enteros.

    Argumentos:
    numero_1(int)
    numero_2(int)

    Se retorna la suma de los parámetros.

    Testeo de la función: Simulación en consola y resultado esperado

    >>> suma(10, 40)
    50

    >>> suma(100, 400)
    500

    """

    return num1 + num2

# Estas funciones pueden ser testeadas mediante el comando en consola
# python -m doctest <NOMBRE DEL ARCHIVO>
# En caso de ser exitoso, no presentará ningún mensaje
# En caso de falla, se presentará el mensaje de falla

def resta(num1, num2):
    """
    >>> resta(100, 200)
    -100

    """

    return num1 - num2