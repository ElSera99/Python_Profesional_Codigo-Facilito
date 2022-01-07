#Tipos de datos en python

#String: Usado para almacenar caracteres y cadenas de caracteres
titulo_curso = 'Curso Profesional de Python'
print(titulo_curso)

nombre_completo = "Eddie 'Venom' Brock"
print(nombre_completo)

#Se usa comillas simples si el texto contiene comillas dobles dentro
#Se usa comillas dobles cuando el texto contiene comillas simples dentro


#Puedes usar triples comillas dobes o triples comillas simples para almacenar mensajes con saltos de linea
mensaje = '''Te encuentras
en el curso profesional de python
de código facilito
'''
print(mensaje)

#Int: Usado para crear numeros enteros
numero_uno = -10
print(numero_uno)

#Float: Usado para crear numeros reales(con puntos decimales)
numero_dos= -2.14
print(numero_dos)

#Bool: Sólo puede almacenar valor False o True
valor = False
print(valor)

#Puedes saber el tipo de dato de una variable mediante la función 'type()'
tipo = type(valor)
print(tipo)