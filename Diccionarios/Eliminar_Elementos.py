#Eliminar elementos de un diccionario

diccionario = {'a': 1, 'b': 2, 'c':3, 'd':4}
print(diccionario)

#Antes de eliminar un elemento de un diccionario, es necesario asegurarnos de que el elemento si exista
print('z' in diccionario)

#Uso de la palabra 'del'
# del <NombreDelDiccionario>[Llave]
#Elimina la llave y su valor correspondiente
del diccionario['a']
print(diccionario)

#Extraer un elemento del diccionario
#Método .pop()
# <NombreDelDiccionario>.pop(llave)
#Crea un objeto que contiene el valor de la llave seleccionada eliminando el elemento del diccionario
valor = diccionario.pop('b')
print(valor)
print(diccionario)

#Eliminar todos los elementos del diccionario
# Método .clear()
# <NombreDelDiccionario>.clear()
#Elimina todos los elementos del diccionario dejando un diccionario vacio
diccionario.clear()
print(diccionario)
