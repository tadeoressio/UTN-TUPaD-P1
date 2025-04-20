# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; 
# en caso contrario deberá mostrar el mensaje “Desaprobado”.

# Se pide que se ingrese la calificación
notaUsuario = int(input("Ingrese su nota: "))

# Se compara con el rango prestablecido
if notaUsuario >= 6:
    print("Aprobado")
else: 
    print("Desaprobado")