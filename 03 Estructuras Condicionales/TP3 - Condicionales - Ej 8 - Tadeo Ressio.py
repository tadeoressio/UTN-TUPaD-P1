# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#   1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#   2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#   3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#   El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. 
# Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# Se pide nombre al usuario
nombreUsuario = input("Ingrese su nombre: ")
# Se pide que seleccione una categoría indicándolo con números. Todo se escribe en una línea pero hay saltos en la consola
categoria = int(input("Indique la opción que desea:\n1 = Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO\n2 = Si quiere su nombre en minúsculas. Por ejemplo: pedro\n3 = Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro\n¿Qué opción desea?: "))

# Según la categoría elegida se ejecutan los métodos correspondientes
if categoria == 1:
    nombreUsuario = nombreUsuario.upper()
elif categoria == 2:
    nombreUsuario = nombreUsuario.lower()
elif categoria == 3:
    nombreUsuario = nombreUsuario.title()
print(nombreUsuario)