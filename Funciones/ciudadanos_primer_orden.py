# Las funciones son ciudadanos de primera clase o ciudadanos de primer orden
# Las funciones pueden ser asgingnadas a variables, pueden ser utilizadas como argunmentos, o pueden retornar otras funciones

# Ejemplo
# Definicion de funcion
def centigrados_a_farhenheit(grados):
    return grados * 1.8 + 32

# Uso de la funcion
print(centigrados_a_farhenheit(20))

# Uso de la función bajo demanda
# No se sabe cuando se va a utilizar la funcion y se almacena en una variable por si acaso es utilizada
# <Variable> = <NombreDeLaFuncion>
# NO SE USAN LOS PARÉNTESIS EN EL NOMBRE DE LA FUNCION
mi_funcion = centigrados_a_farhenheit

# Uso de la función bajo demanda
print(mi_funcion(20))