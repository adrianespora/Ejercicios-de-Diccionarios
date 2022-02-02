#!/usr/bin/env python
# coding: utf-8

# El directorio de los clientes de una empresa está organizado en una cadena de texto como la de más abajo, donde cada línea contiene la información del nombre, email, teléfono, nif, y el descuento que se le aplica. Las líneas se separan con el carácter de cambio de línea \n y la primera línea contiene los nombres de los campos con la información contenida en el directorio.
# 
# "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
# 
# Escribir un programa que genere un diccionario con la información del directorio, donde cada elemento corresponda a un cliente y tenga por clave su nif y por valor otro diccionario con el resto de la información del cliente. Los diccionarios con la información de cada cliente tendrán como claves los nombres de los campos y como valores la información de cada cliente correspondientes a los campos. Es decir, un diccionario como el siguiente
# 
# {'01234567L': {'nombre': 'Luis González', 'email': 'luisgonzalez@mail.com', 'teléfono': '656343576', 'descuento': 12.5}, '71476342J': {'nombre': 'Macarena Ramírez', 'email': 'macarena@mail.com', 'teléfono': '692839321', 'descuento': 8.0}, '63823376M': {'nombre': 'Juan José Martínez', 'email': 'juanjo@mail.com', 'teléfono': '664888233', 'descuento': 5.2}, '98376547F': {'nombre': 'Carmen Sánchez', 'email': 'carmen@mail.com', 'teléfono': '667677855', 'descuento': 15.7}}
# 

# In[20]:


## cadena a separar
cadena = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

## Creo una lista con los clientes y su info, que estan separados por "\n"
listado_clientes = cadena.split("\n") 

## Creo un diccionario vacio para llenar
directorio = {}

## guardo el listado de datos nombre, email, telefono, descuento, que estan separados por ";"
datos = listado_clientes[0].split(";")

## recorro el listado de clientes desde la posicion '1' en adelante, porque la posicion '0' es la que tiene los datos.
for i in listado_clientes[1:]: 
    
    ## genero un nuevo diccionario que almacenara los datos de cada cliente
    cliente = {}
    
    ## guardo en una lista los datos separados por ";" que recorre el bucle
    info_cliente = i.split(";")
    
    ## recorro la lista de datos desde la posicion "1" hasta el largo de datos almacenados
    for j in range(1,len(datos)):
        
        ## si el valor recorrido es igual a la palabra "descuento"
        if datos[j] == 'descuento':
            
            ## convertimos el valor en un valor real
            info_cliente[j] = float(info_cliente[j])
            
        ## Asignamos los datos del cliente al diccionario cliente[numero de nif]   
        cliente[datos[j]] = info_cliente[j]
       
    ## Agrego al diccionario el valor de la info que esta que esta en "cliente"
    directorio[info_cliente[0]] = cliente

    ## Imprimimos el directorio    
print(directorio)
    
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




