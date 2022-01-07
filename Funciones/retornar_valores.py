# Las funciones pueden devolver un valor sin imprimir en pantalla.
# Este valor devuelto puede ser almacenado en una variable
# Es posible devolver varios valores al mismo tiempo

# Definición de la función
def suma(n1, n2):
    resultado = n1 + n1
    # Retorno del valor
    # return <valor>
    return resultado, ', La función retorna 2 valores'

numero_uno = int(input('Ingresa el primer numero entero:\n'))
numero_dos = int(input('Ingresa el segundo numero entero: \n'))

# Una función con multiples valores de salida, devuelve una tupla con todos los valores
# Esta tupla puede ser descomrpimida asignando diferentes variables a los valores de la tupla
resultado, mensaje = suma(numero_uno, numero_dos)
print('El resultado es:', resultado, mensaje)