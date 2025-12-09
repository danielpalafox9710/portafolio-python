milista=["Maria","Pepe","Marta","Antonia",5]	#Declarar lista (las listas puede tener varios tipo de datos

milista4=["Maria","Pepe","Marta","Antonia",5]*3 #declara la lista 3 veces

print (milista4[:])

milista.remove("Pepe")	#Remueve algún dato de la lista

milista.append("Sandra")	#Agregar dato a la lista al final

milista.pop()	#Elimina el último dato de la lista

milista2=["Sandra", "Lucia"]

milista3=milista+milista2	#Une la lista 1 y dos

print (milista3[:])

milista.insert(2,"Sofia")	#Agregar dato a la posicion 2 de la lista

milista.extend(["Edgar","Alfonso"])	#Agregar varios datos a la lista

print(milista[:])	#Imprime lista

print (milista[:3]) #Imprime hasta la posicion 3 de la lista

print (milista[3:])	#Imprime desde la posicion 3 de la lista

print(milista.index("Antonia"))	#Devuelve la posicion de Antonia en la lista (Siempre devuelve el primer elemento)

print ("Pepe" in milista)	#imprime false o true depende de si está el dato en la lista
print ("Jose" in milista)	#imprime false o true depende de si está el dato en la lista




