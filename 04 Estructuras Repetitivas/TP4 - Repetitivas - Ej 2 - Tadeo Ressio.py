# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

# Se pide el número
num = int(input("Ingrese un número y le diremos la cantidad de dígitos que contiene: "))
# Se inicializa el contador
cont = 0
# Se evalúa si el número ingresado es 0, el cual es un caso especial
if num == 0:
    cont +=1
# Se invierte el número en caso de que sea negativo
if num < 0:
    num = -num
# Se divide por 10 hasta que el resultado sea menor que 0
while num > 0:
    num //= 10
    cont += 1
# Se imprime resultado
print("La cantidad de dígitos del número ingresado es: ", cont)