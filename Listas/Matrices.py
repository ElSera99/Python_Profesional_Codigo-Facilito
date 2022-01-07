#Creación de Matrices
#Pueden ser interpretadas como listas que contienen listas

#Cada lista representa una fila
fila_a = [10, 20]
fila_b = [30, 40]

Matriz = [fila_a, fila_b]
print(Matriz)

#Imprimir los elementos de una matriz
#Matriz[#NumeroDeFila][#IndiceDentroDeLaFila]
print(Matriz[0][0])
print(Matriz[1][0])
print(Matriz[0][1])
print(Matriz[1][1])


#Matriz con más dimensiones
fila_a = [1, 2, 3, 4]
fila_b = [5, 6, 7, 8]
fila_c = [9, 10, 11, 12]
fila_d = [13, 14, 15, 16]

Matriz = [fila_a, fila_b, fila_c, fila_d]
print(Matriz)


print(Matriz[1][0]) #5
print(Matriz[2][2]) #11
print(Matriz[3][3]) #16
