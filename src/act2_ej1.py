#Calcular e imprimir cantidad total de líneas,
# cantidad total de palabras,
# promedio de palabras por línea
# y todas las líneas cuya cantidad de palabras esté por encima del promedio.

text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way 
to do it.
Although that way may not be obvious at first unless you're 
Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good 
idea.
Namespaces are one honking great idea -- let's do more of 
those!"""

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