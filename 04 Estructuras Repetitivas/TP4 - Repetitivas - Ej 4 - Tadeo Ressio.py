# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

# Se pide número original para indicarlo fuera del bucle
num1 = float(input("Ingrese un número entero distinto que 0 (esto detendrá el programa): "))
# Se inicializa la suma
suma = 0
# Se comienza el bucle indicando que se frenará si el número ingresado es 0
while num1 != 0:
# Se corrobora que el número sea entero
    if num1 % 1 != 0:
        print("El número no es entero")
# Si es entero se agrega a la suma 
    else: 
        suma += int(num1)
# Se vuelve a pedir un número        
    num1 = float(input("Ingrese otro número entero distinto que 0 (esto detendrá el programa)"))
# Se imprime resultado
print("La suma de los números que ingresó es: ",suma)