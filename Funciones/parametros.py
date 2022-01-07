# Parametros
# Valores de entrada dentro de una función

# Definicion de una función
# def <nombre de la funcion>(<parametros> = <Valor por defecto>):
    # Bloque de código

# Definicion de parámetros de una función
# Los parametros sólo existen en el bloque donde son ejecutados
def suma(n1, n2):
    resultado = n1 + n1
    print(f'suma igual a: {resultado}')

# Creación de variables a asignar afuera de la función
# No necesariamente deben tener el mismo nombre que los parámetros de la función
numero_uno = int(input('Ingresa el primer numero entero:\n'))
numero_dos = int(input('Ingresa el segundo numero entero: \n'))

# Uso de los valores dentro de la función
suma(numero_uno, numero_dos)