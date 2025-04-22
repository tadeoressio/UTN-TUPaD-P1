# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# Se inicializan variables
num = 0
contPar = 0
contImpar = 0
contNeg = 0
contPos = 0
# Se piden números
for i in range (1,101):
    num = int(input("Ingrese un número"))
# Se verifica si el número es 0
    if num == 0:
        continue
# Se verifica si es par o impar    
    if num % 2 == 0:
        contPar += 1
    else:
        contImpar +=1
# Se verifica si es positivo o negativo    
    if num < 0:
        contNeg += 1
    elif num > 0:
        contPos += 1
print("La cantidad de números pares que ingresó fue de: ",contPar)
print("La cantidad de números impares que ingresó fue de: ",contImpar)
print("La cantidad de números positivos que ingresó fue de: ",contPos)
print("La cantidad de números negativos que ingresó fue de: ",contNeg)