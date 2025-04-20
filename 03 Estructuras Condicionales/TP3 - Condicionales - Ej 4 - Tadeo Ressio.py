# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.

# Pedimos edad al usuario 
edadUsuario = int(input("Ingrese su edad: "))

# Se compara la edad con los rangos prestablecidos
if edadUsuario < 12:
    print("Niño/a")
# Se compara en una sola sentencia para hacerlo más simple
elif 12 <= edadUsuario < 18:
    print("Adolescente")
elif 18 <= edadUsuario < 30:
    print("Adulto/a joven")
elif edadUsuario >= 30:
    print("Adulto/a")