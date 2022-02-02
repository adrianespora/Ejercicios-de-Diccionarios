#!/usr/bin/env python
# coding: utf-8

# Ejercicio 6
# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

# In[1]:


persona = {}
continuar = 'si'
while continuar:
    dato1 = input("Ingrese que dato quiere almacenar: ")
    dato2 = input(dato1 + ':')
    persona[dato1] = dato2
    print(persona)
    continuar = input("Desea almacenar mas datos? si/no: ") == 'si'
    


# In[ ]:




