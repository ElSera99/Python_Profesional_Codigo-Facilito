#Uso de una condición intermedia en las vertientes de código
#Condicional ELIF

"""
if (CONDICION): #Representa la vertiente donde SI se cumple la condición
    CODIGO
elif (CONDICION): #Representa la vertiente de una condición alterna a la primera que SI se cumple
    CODIGO
else: #Representa la vertiente donde NO se cumple NINGUNA de las condiciones
    CODIGO
"""
#Pueden agregarse tantos ELIF como sea necesario
#Las condiciones siempre se evaluan de manera descendente
# ELIF siempre va despues de una condicipon IF y antes de un ELSE

calificacion = 8

if calificacion == 10:
    print('Felicidades, aprobaste la materia con calificacion perfecta')
elif calificacion == 9 or calificacion == 8:
    print('Felicidades, aprobaste la materia con calificacion buena')
elif calificacion == 7 or calificacion == 6:
    print('Aprobaste la materia')
else:
    print('Reprobaste la materia')