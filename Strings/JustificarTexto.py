#Justificar Textos

mensaje = "Hola Mundo!"

#Estos métodos generan un nuevo string sin modificar al original
#Método .ljust()
#<NombreDeLaVariable>.ljust(#CantidadDeEspaciosAAñadirALaAlineacion)
mensaje = mensaje.ljust(10)
print(mensaje, '.')

#Método .rjust()
#<NombreDeLaVariable>.rjust(#CantidadDeEspaciosAAñadirALaAlineacion)
mensaje = mensaje.rjust(10)
print(mensaje, '.')

#Método .center()
#<NombreDeLaVariable>.center(#CantidadDeEspaciosAAñadirALaAlineacion)
mensaje = mensaje.center(10)
print(mensaje, '.')