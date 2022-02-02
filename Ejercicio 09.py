#!/usr/bin/env python
# coding: utf-8

# Ejercicio 9
# Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

# In[1]:


gestor = {}
continuar = 'si'
saldo = 0
cobro = 0
while continuar:
    print("1-Agregar factura, 2-pagar existente o 3-terminar")
    eleccion = input("Elija 1 - 2 o 3: ")
    if eleccion == "1":
        numeroFc = input("Ingrese el Nro de la factura: ")
        costeFc = int(input("Ingrese el valor de la factura: "))
        gestor[numeroFc] = costeFc     
        print(gestor)
        saldo = saldo +costeFc
        print("El saldo de las facturas a pagar es:",saldo)
        print("El importe cobrado a hoy es: ",cobro)
    if eleccion == '2':
    	pagoFc = input("Ingrese el Nro de factura a pagar: ")
    	print("Factura Fc",pagoFc, "pagada")
    	cobro = cobro + gestor[pagoFc]
    	saldo = saldo -gestor[pagoFc]
    	print("El saldo de las facturas a pagar es:",saldo)
    	print("El importe cobrado a hoy es: ",cobro)
    	del gestor[pagoFc]
    	print(gestor)
    elif eleccion == '3':
        print(gestor)
        continuar = input("desea continuar? si/no :") == 'si'


# In[ ]:




