#Una estructura de Datos

#Formados por una llave y un valor asociado
# <NombreDelDiccionario> = { 'Lave': Elemento(s), 'Lave': Elemento(s), 'Lave': Elemento(s) ... 'Lave': Elemento(s)}

#Creación de un diccionario vacio
elementos = {}

#Crear un elemento dentro de un diccionario
# <Diccionario>[Llave] = ElementoRelacionado
elementos['nombre']  = 'Serafin'
elementos[(1, 2, 3)]  = 'La llave es una tupla'

print(elementos)
print(len(elementos))

#Modificar el valor de una llave
# <Diccionario>[Llave] = ElementoRelacionado
# Si la llave no existe es creada, pero si ya existe sólo se actualiza su elemento relacionado
elementos['nombre']  = 'Lucky'

print(elementos)
print(len(elementos))

#Los diccionarios no permiten llaves duplicadas, y su valor será el último asignado