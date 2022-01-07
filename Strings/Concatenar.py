#Generar nuevas cadenas de texto a partir de otras

#Cadenas de texto originales
nombre = 'Serafin'
apellido = 'Tierrafría'

#Uso del '+'
nombre_completo = 'Ing. ' + nombre + ' ' + apellido + '.'
print(nombre_completo)

#Uso de %s
#El uso de %s sustituye a una variable que tiene que ser nombrada despues, estas son sustituidas en el orden en el que se presentan
#' %s  %s  %s'%(variable1, variable2, variable3)
nombre_completo = 'Ing. %s %s %s.' %(nombre, apellido, 'Báez')
print(nombre_completo)

#Método .format()
#Usa placeholders {} para esperar el contenido de la variable a usar
# '{} {} {}'.format(Variable1, Variable2, Variable3)
nombre_completo = 'Ing. {} {} {}.'.format(nombre, apellido, 'Báez')
print(nombre_completo)

# Puede nombrarse a los parámetros para una mejor manipulacion por nombre de parametros
nombre_completo = 'Ing. {apellido} {segundo_apellido} {nombre}.'.format(
    nombre = nombre,
    apellido = apellido,
    segundo_apellido = 'Báez'
)

print(nombre_completo)