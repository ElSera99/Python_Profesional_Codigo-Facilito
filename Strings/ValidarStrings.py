#Buscar Strings dentro de otros Strings

titulo_curso = 'Curso Profesional de Python: Uso de Python en VSCODE'

#Método .count()
# <NombreDeLaVariable>.count('StringABuscar')
# Regresa el numero de veces que se encuentra el string buscado
contador = titulo_curso.count('o')
print(contador)

#Uso de in
#Uso de la palabra reservada 'in'
#Es sensible al uso de mayusculas o minusculas
#Regresa un valor booleano
print('python' in titulo_curso.lower())

#Validar si una cadena de texto comienza con un valor específico
# Método .startswith()
# <VariableARevisar>.starswith('ValorARevisar')
#Regresa un valor booleano
print(titulo_curso.startswith('Curso'))

#Validar si una cadena de texto termina con un valor específico
# Método .endswith()
# <VariableARevisar>.endswith('ValorARevisar')
#Regresa un valor booleano
print(titulo_curso.endswith('VSCODE'))