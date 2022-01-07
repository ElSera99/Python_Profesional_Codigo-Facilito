#Crear Variables a partir de Tuplas

#Asignar una variable a cada elemento de una tupla
#Declaración de la Tupla
numeros = (1, 2, 3, 4, 5)

#Declaración de Variables y asignación de elementos de la tupla
uno, dos, tres, cuatro, cinco = numeros

print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco)

#Asignacion de multiples elementos a una variable
#Existen más elementos en la tupla que en las variables declaradas
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#Se necesita usar un * antes del nombre de la variable para almacenarlos en una lista
# *<nombreDeLaVariable>
# Si se desean omitir los elementos restantes se usa un "*_"
# * = Indica que se trata de una lista
# _ = Omite valores
uno, dos, tres, cuatro, cinco, *resto_numeros = numeros

print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco)
print(resto_numeros)

#Seleccionar valores intermedios
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#Pueden omitirse valores usando "_" o asignarlos a una lista con "*<nombreDeLaVariable>"
#         _ = Valores Omitidos
uno, _, tres, _, cinco, _, siete,_ ,*resto_numeros = numeros

print(uno)
print(tres)
print(cinco)
print(siete)
print(resto_numeros)

