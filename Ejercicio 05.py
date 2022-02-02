#!/usr/bin/env python
# coding: utf-8

# Ejercicio 5
# Escribir un programa que almacene el diccionario con los créditos de 
# las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} 
# y después muestre por pantalla los créditos de cada asignatura en el formato 
# <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las 
# asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar 
# también el número total de créditos del curso.
# 

# In[1]:


creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total = 0
for i in creditos:
	print("La asignatura",i, "tiene",creditos[i], "creditos")
	total = total+creditos[i]
print("El curso tiene un total de",total,"creditos")


# In[ ]:




