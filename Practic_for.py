
#for estaciones in ["primavera","verano","otoño","invierno"]:	#Declarar for y número determinado de veces que entrara for al print
#	print (estaciones)	#Imprime el bucle for lo que vale i


contador=0
miEmail=input("Introduce tu dirección email: ")

for i in miEmail: #Declarar for
	if (i=="@" or i=="."):				#Doble igual compara un igual da valor
		contador=contador+1				#Incrementa contador en 1

if contador==2:						#Si solo pones la variable verifica solo si es verdadero
	print("Email es correcto")
else:
	print("Email es incorrecto")



