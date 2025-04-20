# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e 
# imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

# Se pide frase o palabra
fraseUsuario = input("Ingrese una serie de caracteres: ")
# Se pasa a mayúsculas para no tener que escribir más casos posibles
fraseUsuario = fraseUsuario.upper()
# Se mide el largo para indicar cuál es la última letra
largoFrase = len(fraseUsuario)

# Se compara la última letra con los caracteres AEIOU. Se indica menos 1 ya que las posiciones comienzan en 0 y el largo comienza en 1
if fraseUsuario[-1] in "AEIOU":
    fraseUsuario = fraseUsuario + "!"
# Se vuelve a indicar con mayúsculas para que sea más ameno a la lectura
fraseUsuario = fraseUsuario.lower() 
print(fraseUsuario)