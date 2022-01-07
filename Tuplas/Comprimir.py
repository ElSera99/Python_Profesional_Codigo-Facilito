#Crear Tuplas a partir de Variables
lista = [1, 2, 3, 4, 5]
tupla = (10, 20, 30, 40, 50)
lista_2 = [100, 200, 300, 400, 500]
tupla_2 = (1000, 2000, 3000, 4000, 5000)

#Funcion zip()
# Crea un objeto de tipo zip
# zip(<NombreDeLaVariableOElemento1>, <NombreDeLaVariableOElemento2>, <NombreDeLaVariableOElemento3>, ... )
resultado = zip(lista, tupla, lista_2, tupla_2)

#Creación de una tupla con subtuplas
resultado = tuple(resultado)

#Los elementos tuplas resultantes son agrupados por indices iguales
print(resultado)

#Si alguna estructura no cuenta con los elementos suficientes o tiene elementos demás, no son tomados en cuenta. La combinación de numeros de elementos deben ser exactas