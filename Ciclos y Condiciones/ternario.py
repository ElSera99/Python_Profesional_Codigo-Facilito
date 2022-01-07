#Uso del operador ternario para condicionales
#Cuando las condiciones son reducidas, se puede utilizar el operador ternario

calificacion = 10
color = None

#Condicional tradicional
if calificacion >= 7:
    color = 'Verde'
else:
    color = 'Rojo'

print(calificacion, color)

#Alternativa con operador ternario
#En este caso el uso de ELSE es obligatorio
color = 'Verde' if calificacion >= 7 else 'Rojo'
print(calificacion, color)
