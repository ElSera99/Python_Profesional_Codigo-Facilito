#Creación y manipulación de cadenas de texto

#Cadena de texto en una variable
lenguajes = 'Python Ruby Java Rust C++ C'
lenguajesGuion = 'Python-Ruby-Java-Rust-C++-C'

#Dividir texto en elementos de una lista
# Método .split()
# <NombreDeLaVariable>.split('<CaracterCriterioDeDivision>') : Usa el espacio por default como caracter de división
# Este método divide el texto en elementos de una lista segun el argumento de la función
listado_lenguajes = lenguajes.split()
print(listado_lenguajes)

listado_lenguajes_guion = lenguajesGuion.split('-')
print(listado_lenguajes_guion)

#Puedes seleccionar elementos específicos de la coincidencia, es decir, dividir en cierto numero de coincidencias
listado_lenguajes_delimitado = lenguajesGuion.split('-', 3) #Divide en 3 elementos

#Unir elementos de una lista en un texto
lenguajes = ['Python', 'Ruby', 'Java']
#Método ' '.join()
# 'CaracterDeUnion'.join('<CaracterCriterioDeUnion>') : Usa el espacio por default como caracter de criterio de union
lenguajes_string = ' '.join(lenguajes)
print(lenguajes_string)