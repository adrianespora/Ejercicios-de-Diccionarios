#!/usr/bin/env python
# coding: utf-8

# ##Ejercicio 7
# ##Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato
# 
# ##Lista de la compra	
# ##Artículo 1	Precio
# ##Artículo 2	Precio
# ##Artículo 3	Precio
# ##…	…
# ##Total	Coste

# In[1]:


compra = {}## Diccionario vacio
continuar = 'si'
while continuar: #si hay que continuar arranca el bucle
	articulo = input("Que articulo va a llevar?: ")## guarda el producto en articulo
	precio = input("Cuanto cuesta el articulo?: ")##guarda el valor asignado al articulo
	compra[articulo] = precio## almacena en el diccionario el articulo y su precio
	continuar = input("Tiene mas productos? si/no: ") == 'si' ## Pregunta para ver si seguimos el bucle o termina
print("\nLista de compras: \n")
total = 0
for x in compra:##recorre el diccionario
	print(x,"		" ,compra.get(x),"$")## imprime el articulo del diccionario y con compra.get(x) imprimimos el valor del articulo
	suma = float(compra.get(x)) ##almacena en suma el valor float de la compra
	total = total + suma
print("\nTotal		",total,"$")


# In[ ]:




