#!/usr/bin/env python
# coding: utf-8

# Ejercicio 10
# Escribir un programa que permita gestionar la base de datos de clientes
# de una empresa. Los clientes se guardarán en un diccionario en el que la
# clave de cada cliente será su DNI, y el valor será otro diccionario con
# los datos del cliente (nombre, dirección, teléfono, correo, preferente),
# donde preferente tendrá el valor True si se trata de un cliente preferente.
# El programa debe preguntar al usuario por una opción del siguiente menú:
# (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (
#  4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar.
# En función de la opción elegida el programa tendrá que hacer lo siguiente:
# 
# 1-Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
# 2-Preguntar por el DNI del cliente y eliminar sus datos de la base de datos.
# 3-Preguntar por el DNI del cliente y mostrar sus datos.
# 4-Mostrar lista de todos los clientes de la base datos con su DNI y nombre.
# 5-Mostrar la lista de clientes preferentes de la base de datos con su DNI y nombre.
# 6-Terminar el programa.

# In[28]:


base_datos = {}
opcion = '' #asignamos ala variable opcion un valor vacio para que no sea igual a una opcion
while opcion != 6:
    print(f"\nOpciones a elegir:\n 1- Añadir cliente\n 2- Eliminar cliente\n 3- Mostrar cliente\n 4- Listar clientes\n 5- Listar clientes preferentes\n 6- Terminar")
    opcion = int(input("\nElija una opcion: "))
    print("\n")
    if opcion == 1:
        DNI = input("Ingrese el DNI(sin puntos ni comas): ")
        nombre = input("Ingrese el nombre: ")
        direccion = input("Ingrese la direccion: ")
        telefono = input("Ingrese un telefono: ")
        correo = input("Ingrese un correo electronico: ")
        vip = input("Es cliente preferente (si/no): ")
        cliente = {'nombre':nombre,'direccion':direccion,'telefono':telefono,'correo':correo,'preferente':vip=="si"}
        base_datos[DNI] = cliente
    if opcion == 2:
        borrar = input("\nIngrese el DNI del cliente a eliminar: ")
        del base_datos[borrar] ## borra de la base de datos la clave con el dni solicitado
        print(f"El cliente {base_datos[borrar]}") ## imprime el cliente que se elimino
    if opcion == 3:
        datos_cliente = input("\nIngrese el DNI del cliente para ver sus datos: ")
        for clave in base_datos: #recorre clave por clave de la base de datos
            if clave == datos_cliente: ## si la clave es igual al DNI ingresado 
                print(clave, valor['nombre']) ## imprime la clave y el valor solicitado
    if opcion == 4:
        print(f"\n {base_datos}")
    if opcion == 5:
        print('\nLista de clientes preferentes')
        for clave, valor in base_datos.items(): ## recorre los valores en los items de la base de datos
            if valor['preferente']: #cuando el valor es "si" 
                print(f"\n{clave, valor['nombre']}") ##imprime la clave y el valor
            


# In[ ]:




