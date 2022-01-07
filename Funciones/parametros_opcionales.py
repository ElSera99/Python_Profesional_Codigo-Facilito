# Parametros
# Los parametros pueden tener valores por defecto, es decir, pueden ser o no ingresados por el usuario

# def <nombre de la función>(<parametro>=<valor por defecto>)
# Para asignar un valor por defecto a un parámetro, se usa inmediatamente el signo igual y se escribe el valor deseado
# <parametro>=<valor>
# Los parámetros que tienen valores por defecto, siempre tienen que ser colocados a la derecha en el orden de asignación
def area_circulo(radio, pi=3.1416):
    return pi * (radio ** 2)

# Uso de la función sin el segundo parámetro
resultado = area_circulo(10)
print(resultado)

# Uso de la función reasignando el segundo parámetro
# Asignación de valor al parámetro por nombre, en este método se puede no respetar las posiciones
resultado = area_circulo(pi=3.141592, radio=10)
print(resultado)