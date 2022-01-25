# Atributos de instancia: Son aquellos que pertenecen a un objeto y sólo pueden usarse con ese objeto

# Creación de una clase con atributos
class Usuario:
    username = 'Fulanito Cosme'
    email = ''

# Visuzalización de los atributos de un objeto: .__dict__

# Creación de un objeto de instancia de clase
user1 = Usuario()
print(user1.username) #Atributo no existe dentro del objeto, busca dentro de la clase
print(user1.__dict__) #Ver los atributos dentro del objeto
print(user1.adress) #Atributo no existente