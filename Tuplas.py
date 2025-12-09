mitupla=("Juan", 4,11,1997)	#Se crea tupla (No es necesario utilizar paréntesis pero sí recomendado)
tuplaunitaria=("Juan",)

milista=list(mitupla)	#Se almacena una lista a partir de la tupla
#La diferencia es que una es con corchetes y la tupla con paréntesis
nombre, dia, mes, anio=mitupla #Declaras las variables con los datos de la tupla en automatico

print ("Juan" in mitupla)	#Ver si Juan se encuentra en la tupla
print (mitupla.count(13))	#Cuantas veces se encuentra el 13 dentro de la tupla
print(len(mitupla))

print(nombre) #imprime la variable nombre que sería Juan dentro de la tupla

print (mitupla[2])	#Imprime el dato de la tupla en posicion 2
print(milista)






