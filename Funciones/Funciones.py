# Funciones
# Nos permiten crear secciones de código que pueden ser ejecutadas de forma independiente o repetitiva

# Definicion de una función
# def <nombre de la funcion>(<parametros>):
    # Bloque de código
def suma():
    numero_uno = int(input('Ingresa el primer numero entero:\n'))
    numero_dos = int(input('Ingresa el segundo numero entero: \n'))

    resultado = numero_uno + numero_dos
    print(f'suma igual a: {resultado}')

# Llamado de la función
suma()
suma()
suma()