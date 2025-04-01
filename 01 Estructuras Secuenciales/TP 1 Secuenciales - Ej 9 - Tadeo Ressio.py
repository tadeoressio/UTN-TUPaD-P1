# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. 
# Tener en cuenta la siguiente equivalencia: 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎E𝑛𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = (9/5).𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎E𝑛𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
celsius = float(input("Ingrese una temperatura en Celsius y mostraremos el equivalente en Fahrenheit: "))
print(f"La temperatura {celsius} en Farnheit, es de: {int((9/5) * celsius + 32)}")