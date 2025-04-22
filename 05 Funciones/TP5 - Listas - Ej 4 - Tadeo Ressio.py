# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla. 
# ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"]

# Se crea lista
animales = ["perro", "gato", "conejo", "pez"]
# Se reemplazan elementos
animales[-1] = "oso"
animales[-3] = "loro"
# Se imprime lista
print(animales)