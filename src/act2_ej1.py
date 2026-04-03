#Calcular e imprimir cantidad total de líneas,
# cantidad total de palabras,
# promedio de palabras por línea
# y todas las líneas cuya cantidad de palabras esté por encima del promedio.



cant_lineas = 1
lista_palabras = text.split()
cant_palabras = len(lista_palabras)
promedio = 1
lineas_maximas = 1

print(f"La cantidad total de líneas es: {cant_lineas}")
print(f"La cantidad total de palabras es: {cant_palabras}")
print(f"El promedio de palabras por renglón es: {promedio}")
print(f"La cantidad de renglones con más palabras que el promedio es: {lineas_maximas}")
print(dir(text))