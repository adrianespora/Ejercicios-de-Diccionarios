#!/usr/bin/env python
# coding: utf-8

# Ejercicio 3
# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
# 
# Fruta	Precio
# Plátano	1.35
# Manzana	0.80
# Pera	0.85
# Naranja	0.70

# In[45]:


frutas = {'platano':1.35,'manzana':0.80,'pera':0.85,'naranja':0.70}
fruta = input("Que fruta quiere?: ")
if fruta in frutas:
    kilos = float(input("Cuantos kilos quiere?: "))
    precio = frutas[fruta]*kilos
    print("El precio de la fruta elegida y esos kilos es: ", precio, "$")
else:
    print("Esa fruta no esta disponible")


# In[ ]:





# In[ ]:




