#!/usr/bin/env python
# coding: utf-8

# Ejercicio 8
# Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.

# In[92]:


print("Ingrese una palabra en ingles y su traduccion separados por ':' \n y cada par de palabras separados por ',' ej. nombre:name, edad:age")
diccionario = {} # diccionario para completar
traductor = input("Ingrese las palabras aqui: ")
for i in traductor.split(','): #separa lo ingresado cada ','
    clave, valor = i.split(':') #separa en clave y valor lo que esta entre ':'
    diccionario[clave] = valor #asigna la clave y el valor al diccionario
texto = input("Ingrese un texto a traducir: ")
for i in texto.split():#recorre el texto
    if i in diccionario: #si la palabra del texto esta en el diccionario
        print(diccionario[i], end=' ') #reemplaza la palbra
    else:
        print(i, end=' ')

    


# In[ ]:




