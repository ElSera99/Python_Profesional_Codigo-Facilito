# Una variable creada en un alcance superior al que se encuentra en uso, puede ser modificada mediante la palabra reservada "nonlocal"

e = 'e' # Variable global

# Definicion de la función principal
def funcion_principal():
    a = 'a' # Variable Local
    b = 'b' # Variable Local
    
    # Definicion de la funcion anidada
    def funcion_anidada():
        c = 'c'  #Variable más Local

        #Uso de la variable local de un nivel superior para su modificación
        nonlocal b
        # Cambio de valor a la variable no local(de nivel superior)
        b = 'Cambio de valor' 

        print(a)
        print(b)
        print(c)
        print(e)

    funcion_anidada()
    # print(c) - Error, c es una variable local que no puede ser usada fuera de su bloque


funcion_principal()