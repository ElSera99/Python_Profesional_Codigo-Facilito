# Generadores: Función especial que retorna objetos iterables sin que la función finalice
# yield = palabra reservada que suspende de forma momentanea la ejecución de la función

# Definición de una función generadora
def pares():

    # Generar numeros pares
    for numero in range(0, 100, 2):
        # Regresar un numero, pero termina la ejecución 
        #return numero
        #print('Este mensaje no se podrá ver con return')

        # yield <VALOR DE RETORNO>
        # yield detiene momentaneamente la ejecución de la función, antes de retornar un objeto. Una vez sea retornado, la función se reanudará
        yield numero
        print('Este mensaje si es visible con yield')
    


for par in pares():
    print(par)