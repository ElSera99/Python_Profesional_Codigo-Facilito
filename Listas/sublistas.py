#Creación de sublistas con porciones de listas

#                   0         1         2       3       4
lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java']
print(lista_cursos)


#Selección de varios elementos mediante "lista[:]"
# <nombreDeLaLista> [Inicio: Final]
# El indice final es exclusivo, es decir, como final se toma un elemento antes del especificado
sub_lista = lista_cursos[0:3]
print(sub_lista)

#Obtener todos los elementos de la lista
#Pueden obtenerse todos al poner un numero mayor al total de indices
sub_lista1 = lista_cursos[1:100]
print(sub_lista1)

#Al excluir el indice de inicio o final, se reconoce como si se tomara e primero o el ultimo
#Puede obtenerse excluyendo el numero final
sub_lista2 = lista_cursos[1:]
print(sub_lista2)
#A su vez, esto funciona para el inicio
sub_lista3 = lista_cursos[:4]
print(sub_lista3)


#Es posible crear sublistas con saltos, es decir tomando cada dos,tres, cuatro... elementos según convenga
# <NombreDeLaLista>[Inicio:Final:Salto]
sub_lista_saltos = lista_cursos[1:5:2]
print(sub_lista_saltos)

#Sublista con saltos de todos los elementos
sub_lista_saltos1 = lista_cursos[::2]
print(sub_lista_saltos1)

#Sublista con saltos negativos de todos los elementos
#Esta sublista comenzará de izquierda a derecha
sub_lista_saltos2 = lista_cursos[::-1]
print(sub_lista_saltos2)


