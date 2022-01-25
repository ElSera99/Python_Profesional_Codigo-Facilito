# Atributos de clase: Son aquellos atributos que pertenecen a una clase y sólo a esa clase

# Creación de una clase
class Usuario:
    # Atributos de clase: Variables dentro de la clase
    username = 'Fulanito Cosme'
    email = 'fakeemail@example.com'
print(Usuario.username)


# Cambio de un atributo de clase
Usuario.username = 'User1'
Usuario.email = 'info@example.com'
print(Usuario.username)
