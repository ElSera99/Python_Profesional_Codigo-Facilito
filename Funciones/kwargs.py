# Otra forma de ingresar diferentes parámetros a las funciones es mediante "**"
# De esta forma se realiza la entrada de un parámetro de tipo diccionario

# def <nombreDeLaFuncion> (**kwargs)

def usuarios(**kwargs):
    print(kwargs)
    print(type(kwargs))

# En este caso los parámetros son las llaves y sus valores asignados son sus valores correspondientes en la nomenclatura de un diccionario
usuarios(serafin=[10, 10, 9, 8, 7], Agustin=[10, 10, 10, 10, 10] )

#se pueden 