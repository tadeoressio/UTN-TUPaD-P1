# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 
# Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜E𝑛K𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎EnMts ** 2)
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
print(f"Su masa corporal es de: {peso / (altura * altura)}")