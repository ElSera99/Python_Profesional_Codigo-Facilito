# Range and Enumerate
# Range: Nos permite crear una colección de numeros

# Funcion Range
# Range(<Valor Inicial>,<Valor Final>, <Salto>)
# Tiene como valor inicial 0 por defecto
# El valor inicial es inclusivo
# El valor final es exclusivo
rango = range(4,21,2)
for valor in rango:
    print(valor)

# Funcion Enumerate
# Nos permite enumerar los elementos de una colección y les asocia un índice
# Arroja dos resultados: indice, valor
# enumerate(<coleccion>, <Inicio de Indice>)
# El numero de inicio de indice es 0 por defecto
numeros = [10, 20, 30, 40, 50]

for indice, valor in enumerate(numeros):
    print(indice, valor)