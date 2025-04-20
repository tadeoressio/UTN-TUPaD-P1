# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
#   Periodo del año                                                - Estación en el hemisferio norte - Estación en el hemisferio sur
#   Desde el 21 de diciembre hasta el 20 de marzo (incluidos)      - Inviero                         - Verano
#   Desde el 21 de marzo hasta el 20 de junio (incluidos)          - Primavera                       - Otoño
#   Desde el 21 de junio hasta el 20 de septiembre (incluidos)     - Verano                          - Invierno
#   Desde el 21 de septiembre hasta el 20 de diciembre (incluidos) - Otoño                           - Primavera
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
# El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

# Se solicita el hemisferio comparándolo con números
hemisferio = int(input("Indique en qué hemisferio se encuentra\n1: Norte\n2: Sur\nOpción elegida: "))
# Se pide mes comparando con números. Podría no haberse escrito toda la lista pero el usuario podría haber escrito con letras
mes = int(input("Indique el mes en el que se encuentra\n1: Enero\n2: Febrero\n3: Marzo\n4: Abril\n5: Mayo\n6: Junio\n7: Julio\n8: Agosto\n9: Septiembre\n10: Octubre\n11: Noviembre\n12: Diciembre\nOpción elegida: "))
# Se pide día sólo con número sin relacionar con una categoría
dia = int(input("Ingrese el día en el que se encuentra\nOpción elegida: "))

# Se comparan los casos para la selección de hemisferio norte
if hemisferio == 1:
# Se utilizan paréntesis para separar la conjunción de la disyunción
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
# Se comparan los casos para la selección de hemisferio sur
elif hemisferio == 2:
# Se utilizan paréntesis para separar la conjunción de la disyunción
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
print(f"La estación del año es: {estacion}")