# Las funciones pueden recibir n cantidad de argumentos si así lo requieren

# Uso del * para indicar que se trata de una lista
# Al hacer esto indicamos que todos los argumentos utilizados seran usados para generar una tupla

# Definición de la función con parámetro tipo tupla
def promedio(*listado):
    return sum(listado)/len(listado)


# Si se trata de un parametro tipo tupla, este por convensión, siempre tendra el nombre de "*args"
def promedio(*args):
    return sum(args)/len(args)

# Uso de la función con multiples parametros de entrada
resultado = promedio(10, 10, 10, 5, 7, 10, 9, 8, 6, 7, 10, 9)
print(resultado)

#El uso de *args no nos limita para usar otros parámetros
def combinacion(p1, p2, *args, p4 = 500):
    print(p1)
    print(p2)
    print(args)
    print(p4)

combinacion(10, 20, 30, 40, 50, 60, 70, 80, 90, 100, p4 = 1000)

# Al crear dos funciones de forma continua, estas deben estar separadas por dos saltos de linea
