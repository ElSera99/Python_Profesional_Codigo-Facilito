#Uso de indices
#Para acceder de la lista de derecha a izquierda se asignan los indices como se muestra
#                   0         1         2       3       4
lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java']

#Lectura del primer indice de a lista
primer_curso = lista_cursos[0]
print(primer_curso)

#Lectura del segundo indice de a lista
segundo_curso = lista_cursos[1]
print(segundo_curso)

#Una lista tambien puede ser accedida de izquierda a derecha
#Sus indices cambian donde -1 es el primer elemento empezando de izquierda a derecha
#                   -5         -4         -3       -2       -1
#lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java']

print(lista_cursos[-5])