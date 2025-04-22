# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

# Se crea lista con elementos indicados
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
# Se imprime lista
print(lista_anidada)
# Si se quisiera hacer de a uno los pasos sería de la siguiente manera:
lista_anidada2 = []
lista_anidada2.append(15)
lista_anidada2.append(True)
lista_anidada2.append([25.5, 57.9, 30.6])
lista_anidada2.append(False)
print(lista_anidada2)