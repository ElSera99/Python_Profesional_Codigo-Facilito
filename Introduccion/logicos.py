#Operadores Relacionales: Nos permiten comprar tipos de datos bool
#and, or y not

#and: Todas las comparaciones deben de ser verdaderas para obtener un verdadero
resultado_final_and = True and True and 10 > 1
print(resultado_final_and)

#or: Al menos una de las comparaciones debe ser verdadera para obtener un verdadero
resultado_final_or = True or False or 1>10
print(resultado_final_or)

#not: cambia el valor por su contrario
resultado_final_not = not True
print(resultado_final_not)

#Se puden combinar operadores por medio de operadores
resultado_final = True and (False or 10 > 1)
print(resultado_final)