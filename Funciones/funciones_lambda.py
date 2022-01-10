# Funciones anonimas, son exprsadas en una sola linea de codigo, sin nombre y realizan tareas sencillas

# Creación de una función lambda
# <VARIABLE> = lambda <Parametro1>,<Parametro2>,<Parametro3>,<ParametroN> : <Operacion de retorno o bloque de codigo>
# Una función lambda siempre debe tener una operación o cuerpo de retorno
funcion_grados = lambda grados : grados * 1.8 +32

# Uso de la funcion lambda
print(funcion_grados(20))


# Creacion de una funcion lamba sin parametros
sin_parametros = lambda : True
print(sin_parametros())

# Creacion de una función lambda con parametros por defecto
parametros_default = lambda p1=10, p2=20, p3=30 : p1 + p2 + p3
print(parametros_default())

# Creacion de una función lambda con *args o **kwargs
asterisco = lambda *kargs, **kwargs : len(kargs) + len(kwargs)
print(asterisco(10,20,20, kwargs=[10,20,30]))
