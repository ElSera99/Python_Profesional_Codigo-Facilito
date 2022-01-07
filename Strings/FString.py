#Uso de los Fstrings
#Nos permiten generar nuevos strings a partir de otros mediante interpolación


nombre = 'Serafin'
apellido = 'Tierrafria'

#Se coloca una f antes del string para generar un FString
nombre_completo = f'Ing. {nombre} {apellido} {"Báez"} {50 * 10}'
print(nombre_completo)

