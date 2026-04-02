'''nombreUsuario=input("Introduce tu nombre de usuario")

print ("El nombre es: ", nombreUsuario.capitalize())	#Se aplica despues de la variable con un punto

print ("El nombre es: ", nombreUsuario)
'''

edad=input("Introduce la edad: ")

while (edad.isdigit()==False):
	print ("Por favor introduce un valor númerico")

	edad=input("Introduce la edad: ")



if (int(edad)<18):

	print ("No puede pasar")

else:
	print("Puede pasar")


