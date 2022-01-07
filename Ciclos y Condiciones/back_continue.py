# Modificacion de ciclos y condicionales
# Break: Detiene la ejecución de un bloque de código de forma inmediata
# Continue: Omite la ejecución de un bloque de código de forma inmediata

titulo_curso = "Curso profesional de Python"

#Uso de break
for caracter in titulo_curso:
    if caracter == 'P':
        break

    print(caracter)

#Uso de continue
for caracter in titulo_curso:
    if caracter == ' ':
        continue

    print(caracter)