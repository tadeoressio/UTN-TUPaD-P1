# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. 
# (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

# Se inicializa variable
suma = 0
# Se piden números
for i in range(1, 101):
    num = int(input("Ingrese un número entre 100 e indicaremos el promedio de los mismo"))
# Se hace la suma
    suma += num
# Se calcula promedio
promedio = suma / 100
# Se muestra resultado
print("La media de los 100 números ingresados es: ",promedio)