# Una variable creada en un alcance superior al que se encuentra en uso, puede ser modificada mediante la palabra reservada "nonlocal"

e = 'e' # Variable global

# Definicion de la función principal
def funcion_principal():
    a = 'a' #Variable Local
    b = 'b'
    
    # Definicion de la funcion anidada
    def funcion_anidada():
        c = 'c'  #Variable más Local

        #Uso de la variable local de un nivel superior
        nonlocal b

        # Cambio de valor a la variable no local(de nivel superior)
        b = 'Cambio de valor'