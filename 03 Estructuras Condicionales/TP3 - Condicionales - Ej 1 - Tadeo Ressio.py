# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# Se pide que usuario ingrese su edad
edadUsuario = int(input("Ingrese su edad: "))

#Se compara con 18. Normalmente a los 18 ya se es mayor de edad pero mantuve lo solicitado por la consigna
if edadUsuario > 18:
    print("Es mayor de edad")