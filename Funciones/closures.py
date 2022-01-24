# Closures: Una función que puede generar de forma dinámica de otra función, esta nueva función puede acceder a las variables locales aunque estas ya hayan sido usadas

# Declarar función closure
def saludar(username):
    
    # Variable local
    mensaje = f'Hola {username}'

    # Esta función hace uso de otras variables y se queda con su ultimo valor asignado
    def mostrar_mensaje():
        print(mensaje)

    return mostrar_mensaje


# Uso de la función
# Valor asignado
username = 'Cody'
# Ejecucción de la función
respuesta = saludar(username)

# Nuevo valor asignado -> NO VALIDO
username = 'Serafin'

respuesta()