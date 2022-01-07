#Obtener elementos de un diccionario

diccionario = {'a': 1, 'b': 2, 'c':3, 'd':4}

#Obtener un valor
# <NombreDeLaVariable> = <Diccionario>[Llave]
#Sólo se pueden obtener valores de llaves que existan
valor = diccionario['a']
print(valor)

#Es necesario veriicar que la llave exista
print('z' in diccionario)

#Obtener el valor de una llave de forma segura
#Método .get()
# <NombreDelDiccionario>.get(Llave, 'Mensaje de Error')
# Por defecto regresa un valor 'none' si no existe, un valor 'none' representa la ausencia de un valor
valor = diccionario.get('z', 'La llave no existe en el dicionario')
print(valor)

#Obtener el valor de una llave y si no existe, se crea la llave con su valor
#Método .setdefault()
# <NombreDelDiccionario>.setdefault(llave, ValorAAñadir)
valor = diccionario.setdefault('e', 5)
print(valor)
print(diccionario)
