#Uso de Indices

lista = [5,11, 0 ,9, 11, 100, 55, 9, 6, 7, 55, 66, 3, 2, 22, 12, 17, 16, 14, 25]
print(lista)

#Es importante comprobar que el elemento existe en la lista para evitar errores
existeElElemento = 100 in lista
print(existeElElemento)

#Conocer el indice de un elemento
#Método .index()
# <NombreDeLaLista>.index(<Elemento>)
indice = lista.index(100)
print(indice)

"""
Este método encuentra el indice del primer elemento coincidente,
Es decir, no tomará en cuenta los indices aquellos elementos que se repitan despues del primero que coincida

En caso de que no se encuentre el elemento, se obtendrá como resultado un error

"""