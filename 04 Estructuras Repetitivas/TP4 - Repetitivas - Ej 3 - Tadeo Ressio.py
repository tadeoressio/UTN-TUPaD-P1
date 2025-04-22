# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

# Mensaje antes de todo para generar salto de línea
print("Ingrese dos números")
# Se escriben por separado para generar saltos de línea
num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
# Esta variable se usará para intercambiar valores
num3 = 0
# Esta variable almacenará la suma entre los números indicados
suma = 0
# Se ordenan los números para que num1 sea el menor siempre
if num1 > num2:
    num3 = num2
    num2 = num1
    num1 = num3
# Se suma 1 a num1 para que se excluya el valor inicial
num1 += 1
# Se realiza la suma 
for i in range (num1, num2):
    suma += i
# Se imprime resultado
print("La suma de los números entre los indicados, excluyendo sus extremos, es: ",suma)