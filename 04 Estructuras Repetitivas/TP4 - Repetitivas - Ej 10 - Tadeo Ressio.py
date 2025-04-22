# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# Se solicita número
num = int(input("Ingrese un número entero: "))
# Se verifica que el número no sea de un solo dígito
while -10 < num < 10:
    num = int(input("El número debe tener más de un dígito. Ingrese otro: "))
# Se inicializa variable para invertir número
numInvertido = 0
# Se verifica si el número es negativo
numNegativo = False
if num < 0:
    numNegativo = True
# Se convierte número a positivo    
    num = -num
# Se invierte número
while num > 0:
    ultimoDigito = num % 10
    numInvertido = numInvertido * 10 + ultimoDigito
    num = num // 10
# Si era negativo se vuelve a asignar
if numNegativo:
    numInvertido = -numInvertido
# Se muestra resultado
print("El número con los dígitos invertidos es:", numInvertido)