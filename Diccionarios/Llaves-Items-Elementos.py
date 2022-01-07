#Conocer las llaves y valores dentro de un diccionario

diccionario = {'a': 1, 'b': 2, 'c':3, 'd':4}

#Obtener las llaves de un diccionario
#Método .keys()
# <NombreDelDiccionario>.keys()
#Regresa un objeto con las llaves que existen en el diccionario
llaves = diccionario.keys()
print(tuple(llaves))

#Obtener los valores de un diccionario
#Método .values()
# <NombreDelDiccionario>.values()
#Regresa un objeto con los valores que existen en el diccionario
valores = diccionario.values()
print(tuple(valores))

#Obtener las llaves y sus elementos correspondientes
#Método .items()
#Regresa un objeto con tuplas de las llaves y elementos que existen en el diccionario
elementos = diccionario.items()
print(tuple(elementos))