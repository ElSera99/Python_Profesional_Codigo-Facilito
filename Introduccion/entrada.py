#Obtener valores que el usuario ingresa

#Uso de la función 'input()'
#Dentro de los parentesis, se puede agregar opcionalmente un mensaje que puede ser visible para el usuario, esto ayuda a dar contexto
nombre_completo = input('Ingresa tu nombre completo: ')

print(nombre_completo)

#La función 'input()' siempre regresa un tipo de dato string

edad = input('Ingresa tu edad:') #El tipo de dato almacenado correspondera a un string
#Podemos cambiar de tipo de dato usando la función 'int()', la cual lo cambia a un tipo entero
edad = int(edad)

altura = input('Ingresa tu altura en metros')#El tipo de dato almacenado correspondera a un string
#Podemos cambiar de tipo de dato usando la función 'float()', la cual lo cambia a un tipo de punto flotante
altura = float(altura)

autorizacion = input('¿Autorizas en uso de tus datos?(SI o NO):')
autorizacion = autorizacion == 'SI'
print(autorizacion)