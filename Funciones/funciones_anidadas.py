# Uso de funciones dentro de otras funciones

# Definicion de una funcion
def cajero_ATM(cantidad, balance, tipo='deposito'):

    #Creacion de funcion dentro de la funcion
    def deposito(cantidad, balance):
        return balance + cantidad

    #Creacion de funcion dentro de la funcion
    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance-cantidad
        else:
            return None
    
    #Salida de la función madre
    if tipo == 'deposito':
        return deposito(cantidad, balance)
    elif tipo == 'retiro':
        return retiro(cantidad, balance)

# Uso de la función
operacion_1 = cajero_ATM(50, 500, 'deposito')
operacion_2 = cajero_ATM(700, 50, 'retiro')

print(operacion_1)
print(operacion_2)