#Tuplas VS Listas

#Lista
cursos = ['Python', 'Flask', 'Django', 'Rails', 'MongoDB']
print(cursos)
#Tupla
niveles = ('Basico', 'Intermedio', 'Avanzado')
print(niveles)

"""
Tuplas Vs Listas

Cuando no se tiene idea de la cantidad de elementos a almacenar o estos elementos pueden variar, se usa una lista

Cuando sabemos que los elementos no cambiaran y queremos que se mantengan así durante todo el programa, se usa una tupla

Pueden generarse tuplas a partir de listas y listas a partir de tuplas

"""

#Crear una tupla
#Funcion tuple()
#tuple(<NombreDeLaLista>)
cursos_tupla = tuple(cursos)
print(cursos_tupla)

#Crear una lista
#Funcion list()
#list(<NombreDeLaLista>)
lista_niveles = list(niveles)
print(lista_niveles)