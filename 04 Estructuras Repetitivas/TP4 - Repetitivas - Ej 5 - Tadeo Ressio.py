# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# Se importa librería para crear números aleatorios
import random
# Se crea contador
cont = 1
# Se crea un número aleatorio
numCorrecto = random.randint(0, 9)
# Se pide al usuario que intente adivinar
numUsuario = int(input("Adivine un número aleatorio entre el 0 y el 9: "))
# Se corrobora que el número sea entero
 
while numUsuario != numCorrecto:
    numUsuario = int(input("Su número fue incorrecto, ingrese otro: "))
    cont += 1
print("El número ingresado (",int(numUsuario),") es correcto, y la cantidad de intentos que le tomó adivinar fueron: ",cont)