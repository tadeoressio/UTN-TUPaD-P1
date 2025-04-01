# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos = float(input("Ingrese la cantidad de segundos y le diremos a cuántas horas equivale"))
horas = (segundos / 60) / 60
print(f"La cantidad de horas que corresponden a {segundos} segundos, es de: {horas}")