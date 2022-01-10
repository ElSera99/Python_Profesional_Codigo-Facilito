# Uso de variables dentro de una función o fuera de una funcion

# Creacion de una variable con alcance global
# Puede ser utilizada en cualquier bloque de código
animal = 'Leon'

# Definicion de funcion
def imprimir_animal():
    
    # Variable con alcance local
    # Sólo puede ser usada dentro de este bloque de codigo
    # Despues de su ejecución, las variables locales son destruidas
    animal = 'Ballena'

    print(animal)

# Uso de la función con variable local
imprimir_animal()

# Uso de la variable global
print(animal)

# Modificar una variable global
# Esta puede ser modificada dentro de una función o un bloque de código, mediante la palabra reservada "global"

# Definicion de funcion
def imprimir_animal_global():
    # Se indica el uso de una variable global
    global animal
    
    # Modificacion de la variable global
    animal = 'Ballena'
    #Uso de la variable global dentro del bloque de código
    print(animal)

# Uso de la variable global modificada
imprimir_animal_global()