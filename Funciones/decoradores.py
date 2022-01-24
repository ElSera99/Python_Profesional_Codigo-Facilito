# Decoradores : En pocas palabras, son funciones que tienen como entrada una función y a su vez retornan otra función

# Tambien sirven para extender funcionalidades a una función que no pueda o se deba ser modificada

# A = Función Principal -> Decorador
# B = Función a decorar
# C = Función decorada

# A(B) -> C

# Definición de función decoradora
def funcion_A(funcion_B):

    def funcion_C():
        # Funcionalidad añadida
        print('Mensaje añadido como decoración 1')

        # Función a decorar
        funcion_B()

        # Funcionalidad añadida 
        print('Mensaje añadido como decoración 2')

    return funcion_C


# Llamado de la función decoradora: Indica que la función siguiente a el llamado será decorada
# @<NOMBRE DE LA FUNCIÓN A DECORAR>
@funcion_A

# Función a decorar
def saludar():
    print('Este es el mensaje de la función sin decorar')


# Uso de la función ya decorada
saludar()


# Otro ejemplo
def funcion_decoradora(funcion_entrada):

    def funcion_anidada(*args, **kwargs):

        resultado = funcion_entrada(*args, **kwargs)
        print('Decorador 1')
        print('Decorador 2')
        return resultado

    return funcion_anidada

@funcion_decoradora
def suma(num1, num2):
    return num1 + num2

resultado = suma(25, 25)
print(resultado)