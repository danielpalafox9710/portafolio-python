midiccionario={"Alemania":"Berlin","Francia":"Paris","ReinoUnido":"Londres","España":"Madrid"}
#Declarar diccionario clave:valor


midiccionario["Italia"]="Lisboa" #Agrega elemento al diccionario
print (midiccionario)

midiccionario["Italia"]="Roma" #Corrige el valor a clave Italia

print(midiccionario["Francia"]) #Te muestra el valor de la clave Francia

print (midiccionario) #Te muestra todo el diccionario

del midiccionario["ReinoUnido"] #Elimina un elemento
print (midiccionario)

diccionario={"Mexico":"CDMX", 23:"Jordan", "Mosqueteros":3} #Diccionario con distintos formatos
print (diccionario)

mitupla=["España", "Francia","ReinoUnido","Alemania"] #Agregar tupla a un diccionario
diccionariotupla={mitupla[0]:"Madrid", mitupla[1]:"Paris",mitupla[2]:"Londres",mitupla[3]:"Berlin"}

print (diccionariotupla)
print (diccionariotupla["Francia"])

diccionariotuplas={"23":"Jordan", "Nombre":"Jordan", "Equipo":"Chicago", "anillos":[1991,1992,1993]} #Diccionario con tupla
print(diccionariotuplas)


diccionarios={"23":"Jordan", "Nombre":"Jordan", "Equipo":"Chicago", "anillos":{"temporadas":[1991,1992,1993]}} #Diccionario dentro de diccionario
print(diccionarios["anillos"])	#Imprime los anillos del diccionario

print(diccionarios.keys()) #Devuelve las claves del diccionario
print(diccionarios.values()) #Devuelve los valores del diccionario
print(len(diccionarios)) #Devuelve cuantos valores hay en diccionario



