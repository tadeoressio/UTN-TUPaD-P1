# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e 
# imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

fraseUsuario = input("Ingrese una serie de caracteres: ")
fraseUsuario = fraseUsuario.upper()
largoFrase = len(fraseUsuario)

if fraseUsuario[-1] in "AEIOU":
    fraseUsuario = fraseUsuario + "!"
fraseUsuario = fraseUsuario.lower() 
print(fraseUsuario)