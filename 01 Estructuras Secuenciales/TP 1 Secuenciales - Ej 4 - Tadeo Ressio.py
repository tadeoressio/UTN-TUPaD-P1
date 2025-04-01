# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
radio = float(input("Ingrese el radio de su círculo y calcularemos el área y el perímetro: "))
area = 3.14 * radio * radio
perimetro = 2 * 3.14 * radio
print(f"El área de su círculo es: {area}, y el perímetro es: {perimetro}")