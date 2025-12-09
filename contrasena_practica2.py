contrasena=input("Introduce una contraseña: ")
espacio=True
longitud=True

for c in contrasena:
	if (c==" "):
		espacio=False


if len(contrasena)<8:
	longitud=False


if (longitud==True and espacio==True):
	print("Contraseña OK...")
else:
	print("Contraseña errónea...")




