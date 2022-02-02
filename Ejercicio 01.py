#!/usr/bin/env python
# coding: utf-8

# Ejercicio 1
# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

# In[11]:


divisa = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Ingrese la divisa Euro, dollar o yen para saber su simbolo : ")
if moneda == 'euro':
    print(divisa['Euro'])
elif moneda == 'dollar':
        print(divisa['Dollar'])
else:
    print(divisa['Yen'])


# In[16]:


monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
print(monedas.get(moneda.title(), "La divisa no está."))#devuelve lo pedido, y si no esta devuelve "la divisa no esta"


# In[ ]:




