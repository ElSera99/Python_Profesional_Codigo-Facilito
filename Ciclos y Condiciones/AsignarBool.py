#Asignar valores mediante OR
#El operador lógico or asinará el primer valor verdadero con el cual se tope

variable = 'Cody'  or 'CodigoFacilito'
print(variable)

variable = ''  or 'CodigoFacilito'
print(variable)

variable = ''  or 0 or [] or True
print(variable)

#Puede omitirse una condición usando el operador or
listado = [1]
nombre = 'Cody'

#Condicional normal 
if listado:
    variable = listado
else:
    variable = nombre
print(variable)

#Uso de operador lógico or en lugar de condicional
variable = listado or nombre
print(variable)

print