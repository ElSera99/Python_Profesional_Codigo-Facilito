#Modificación de elementos de las listas

#                   0         1         2       3       4
lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java']
print(lista_cursos)


#Añadir un elemento al final de la lista
#Método .append()
# <NombreDeLaLista>.append(<NuevoElemento>)
lista_cursos.append('MongoDB')
print(lista_cursos)
lista_cursos.append('C#')
print(lista_cursos)


#Añadir un elemento en un índice específico de la lista
# Método .insert()
# <NombreDeLaLista>.append(#Indice, <NuevoElemento>)
lista_cursos.insert(1, 'Rails')
print(lista_cursos)
lista_cursos.insert(0, 'PyGame')
print(lista_cursos)

#Extender listas a partir de otras

#Lista a añadir
lista_cursos2 = ['C', 'C++', 'Docker']

#Visualizar lista original
print(lista_cursos)

#Médodo .extend()
# <NombreDeLaListaAExtender>.extend(<ListaAAñadir>)
lista_cursos.extend(lista_cursos2)

#La lista a añadir no se ve modificada
print(lista_cursos2)

#Lista modificada
print(lista_cursos)

#Eliminar Elementos de una Lista
#Método .remove()
#<NombreDeLaLista>.remove(<ElementoAEliminar>)
lista_cursos.remove('MongoDB')
print(lista_cursos)

#Función del
#Elimina elementos por indice
# del <NombreDeLaLista>[#Indice]
del lista_cursos[0]
print(lista_cursos)

#Funcion .clear()
#Elimina todos los elementos de una lista
#La lista termina sin elementos y con longitud 0
lista_cursos.clear()
print(lista_cursos)


