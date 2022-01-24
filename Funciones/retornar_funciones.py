# Al definir una función, siempre es necesario retornar un valor. Sin embargo, es posible que una función pueda retornar otra función como su valor de salida}

# Definición de una función principal
def saludar():

    # Definición de una función anidad
    def mostrar_mensaje():
            print('Hola, este es un mensaje')

    # Retorno de valor de función
    return mostrar_mensaje

# Asignación de la variable con función
respuesta = saludar()

# Llamado de la variable como función 
respuesta()