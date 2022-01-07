#Algunas veces necesitaremos que dependiendo de varios criterios, se ejecuten bloques de codigo

#Condicional IF
"""
if (CONDICION): #Representa la vertiente donde SI se cumple la condición
    CODIGO
else: #Representa la vertiente donde NO se cumple la condición
    CODIGO
"""
resultado = 50

if resultado > 10 and resultado < 20:
    print('La variable es mayor que 10')
else:
    print('La condición no se cumplió')

#El uso del condicional ELSE puede ser opcional