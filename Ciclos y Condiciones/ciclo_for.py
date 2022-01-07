# Uso del diclo For
# Se usa un objeto iterable

#Muchas listas, diccionarios o tuplas, tienen su nombre en plural
usuarios = ['usuario1', 'usuario2', 'usuario3', 'usuario4']

# Estructura For
# For <contador> in <coleccion>:
    # Bloque de código

# la variable de contador, sólo existe localmente y momentaneamente mientras se ejecuta el ciclo
for usuario in usuarios:
    print(usuario)

