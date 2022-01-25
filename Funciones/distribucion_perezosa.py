# Distribución perezosa: Obtener objetos bajo demanda, es decir como sean necesarios 

# Definición de una función generadora
from tkinter.tix import Tree


def pares():

    # Generar numeros pares
    for numero in range(0, 100, 2):
        yield numero
        print('Ejecución reanudada')
    
generador = pares()

# Funcion next()
# Funcion usada para pasar de elementos en un generador en orden de ejecución
print(next(generador))
print(next(generador))
print(next(generador))
print('Intermedio de ejecución')
print(next(generador))
print(next(generador))
print(next(generador))

# Al no tener más elementos en la iteración se generará un error
# Estos pueden ser validados con 'try' y 'except'

generador = pares()

while True:
    # Ejecutar código
    try:
        par = next(generador)
        print(par)
    # Al presentarse un error
    except StopIteration:
        print('El generador finalizó')
    break