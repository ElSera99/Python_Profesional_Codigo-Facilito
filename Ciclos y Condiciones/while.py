#Uso del ciclo While
#Permite ejecutar varias veces un bloque de código hasta que una condición deje de cumplirse
#Es usado siempre y cuando no se sepan las iteraciones necesarias

#Variable de control
numero = 1234
contador_digitos = 0

#Estructura WHILE
# while condicion:
    # Bloque de código
# else:                 <--- Es opcional

while numero >= 1:
    #contador_digitos = contador_digitos + 1
    contador_digitos += 1
    numero = numero / 10
else:
    print(contador_digitos)

print(contador_digitos)