# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

# Se pide número original
numUsuario = int(input("Ingrese un número y sumaremos todos los números comprendidos entre el número indicado y 0: "))
# Se inicializa suma
suma = 0
# Se declara una variable para saber si el número es negativo
numNegativo = False

# Se verifica si el número es negativo
if numUsuario < 0:
    numUsuario = -numUsuario
    numNegativo = True
# Se realiza la suma
for i in range(1, numUsuario + 1):
    suma += i
# Si era negativo se aclara debidamente
if numNegativo == True:
    suma = -suma
# Se imprime resultado
print("El resultado es: ",suma)