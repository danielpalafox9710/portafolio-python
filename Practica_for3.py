###################### Variables generales
contrasena=input("Escribe un correo valido: ")
arroba=True
punto=True
####################### Funcion Arroba
def arroba1():
	conteo=0
	for i in contrasena:
		if i=="@":
			conteo+=1

	if conteo==1:
		return True
	else:
		return False
####################### Funcion Punto
def punto1():
	conteo=0
	for i in contrasena:
		if i==".":
			conteo+=1

	if conteo>=1:
		return True
	else:
		return False

###################### Codigo base
if (punto1()==True and arroba1()==True):
	print("El correo:",contrasena,"es correcto...")
else:
	print("El correo:",contrasena,"es incorrecto...")





