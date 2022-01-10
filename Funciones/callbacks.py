# Se trata de funciones que son utilizadas como argumentos para otras funciones

# Creacion de una funcion
promedio = lambda *args : sum(args)/len(args)

# Creacion de OTRA funcion
aprobatorio = lambda calificacion : calificacion >= 7

# Creacion de una función que recibe como parámetros otras funciones
                    #Primera funcion, #Segunda Funcion -> Este es un callback
def mostrar_mensaje(func_promedio, func_aprobatorio, *args):
    promedio = func_promedio(*args)

    if func_aprobatorio(promedio):
        print(f'Felicidades, aprobaste la materia con {promedio}')
    else:
        print(f'No aprobaste la materia, eres un burro')

# Uso de la función y el callback
mostrar_mensaje(promedio, aprobatorio, 7, 7, 5, 9, 10)

# Creacion de otra función para usar dentro de la función que recibe funciones
alto_promedio = lambda calificacion : calificacion >= 9

# Uso de la función y el callback
mostrar_mensaje(promedio, alto_promedio, 7, 7, 5, 9, 10)

