#Operaciones ejecutadas sobre listas

#Listas con un solo tipo de valor
lista = [5,11, 0 ,9, 11, 100, 55, 9, 6, 7, 55, 66, 3, 2, 22, 12, 17, 16, 14, 25]
print(lista)


#Ordenar listas

#Método .sort()
# <NombreDeLaLista>.sort()
"""
Parametros: 

reverse = True --> Ordena de mayor a menor
"""
#Mayor a menor
lista.sort()
print(lista)

#Menor a mayor
lista.sort(reverse = True)
print(lista)

#Obtener el elemento mayor de una lista
#Función max()
# max(<Nombre de a lista>)
maxNum = max(lista)
print(maxNum)

#Obtener el elemento menor de una lista
#Función min()
# min(<Nombre de a lista>)
minNum = min(lista)
print(minNum)


#Saber si un elemento se encuentra o no  en la lista
#Uso de in
# <Elemento> in <NombreDeLaLista>

#Pregunta: Este elemento está en la lista
estaEnLaLista = 300 in lista
print(estaEnLaLista)

#Pregunta: Este elemento no está en la lista
noEstaEnLaLista = 300 not in lista
print(noEstaEnLaLista)


