#!/usr/bin/env python
# coding: utf-8

# Ejercicio 2
# 
# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
# 

# In[18]:


diccionario = {'nombre':'','edad':'','direccion' :'', 'telefono' : ''}
diccionario['nombre'] = input("Ingrese su nombre: ")
diccionario['edad'] = input("Ingrese su edad: ")
diccionario['direccion'] = input("Ingrese su direccion: ")
diccionario['telefono'] = input("Ingrese su numero de telefono: ")
print(diccionario['nombre'],"tiene",diccionario['edad'],"años, vive en" ,diccionario['direccion'],"y su numero de telefono es" ,diccionario['telefono'])


# In[ ]:




