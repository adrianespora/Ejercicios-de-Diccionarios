#!/usr/bin/env python
# coding: utf-8

# Ejercicio 4
# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

# In[16]:


meses = {'01':'enero','02':'febrero','03':'marzo','04':'abril',
    '05':'mayo','06':'junio','07':'julio','08':'agosto','09':'septiembre',
    '10':'octubre','11':'noviembre','12':'diciembre'}
fecha = input("Ingrese su fecha de nacimiento con este formato dd/mm/aaaa :")
dia = fecha[0]+fecha[1]
mes = fecha[3]+fecha[4]
año = fecha[6]+fecha[7]+fecha[8]+fecha[9]
mesletra = meses[mes]
print(dia,"de",mesletra,"del",año)


# In[ ]:




