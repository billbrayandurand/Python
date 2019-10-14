#!/usr/bin/env python
# coding: utf-8

# **Cabecera**

# In[9]:


# -*- coding: utf-8 -*-

# ------------- Cantidad de segundos que has vivido -------------

# Definición de variables
anios = 30
dias_por_anio = 365
horas_por_dia = 24
segundos_por_hora = 60

# Operación
print (anios * dias_por_anio * horas_por_dia * segundos_por_hora)


# **Definición de Variables**

# In[ ]:


anios = 30
diasPorAnio = 365
horasPorDia = 24
segundosPorHora = 60


# **Operación**

# In[10]:


print (anios * dias_por_anio * horas_por_dia * segundos_por_hora)


# **Cadenas** 

# In[8]:


# -*- coding: utf-8 -*-

# --------------- Uso de cadenas ---------------

# Cuando se imprime una palabra sin comillas Python
# la interpreta como una variable, si ésta no existe
# se arroja un error en tiempo de ejecución
#print (Hola)

# Las cadenas se pueden crear con comillas simples
# o con comillas dobles
print ('Curso')
print (" de Python\n")

# --------------- Cadenas y números ---------------
nombre = "Marco"
print ("Hola " + nombre + "! \n")

num_tortugas = 2

# Los números se deben convertir a cadenas o
# se arrojará un error
#print (nombre + " tiene " + num_tortugas + " tortugas \n")

# Los números se convierten a cadena a través
# de la función str()
print (nombre + " tiene " + str(num_tortugas) + " tortugas \n")


# **Subcadenas**

# In[15]:


# -*- coding: utf-8 -*-

# ------------- Cadenas y subcadenas -------------

# Cadena con 22 caracteres
cadena = "parangaricutirimicuaro"


# In[16]:


print (cadena[0])    # Se obtiene el primer carácter
print (cadena[21])   # Se obtiene el último carácter


# In[17]:


# Si se pone un indice negativo, la cuenta
# empieza en el �ltimo elemento de la cadena
print (cadena[-2])   # último carácter


# In[18]:


# Si se quiere acceder a un elemento fuera de rango
# de la cadena, se obtiene el error
# IndexError: string index out of range
#print (cadena[22])   # Carácter fuera de rango

print (cadena[5:13])  # imprime garicuti


# In[19]:


print (cadena[5:])    # imprime garicutirimicuaro


# In[20]:


print (cadena[:5])    # imprime param


# In[21]:


print (cadena[:])     # imprime la cadena completa


# In[22]:


# -*- coding: utf-8 -*-

# ------------- Búsquedas en cadenas -------------

# Cadena original
cadena = "Amor y deseo son dos cosas diferentes; que no todo lo que se ama se desea, ni todo lo que se desea se ama. (Don Quijote)"

# Busca la cadena "ama"
print (cadena.find("ama"))


# In[33]:


#Imprimie  la subcadena
print (cadena[cadena.find("ama"):])


# In[24]:


# Busca la siguiente coincidencia de "ama"
print (cadena[cadena.find("ama") + 1:].find("ama"))


# In[25]:


# Imprime la cadena a partir de la segunda coincidencia
print (cadena[61 + 1 + 40:])


# In[26]:


# Busca "corazon" en la cadena
print (cadena.find("corazon"))


# In[27]:


# Busca a partir de un indice
print (cadena.find("todo", 62))


# In[28]:


# Imprime a partir de un �ndice y hasta el final
print (cadena[78:])


# In[ ]:




