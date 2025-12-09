"""
for i in range(5,50,3):		#Primer numero asigna el número a empezar, segundo el número a terminar y tercero el número de conteo
	print (f"Valor de la variable {i}")	#Para unir textos con variables usar f y variable con {}

"""
valido=False
email=input("Introduce tu email: ")

for i in range(len(email)):

	if email[i]=="@":
		valido=True

if valido:

	print("Email es correcto")

else:

	print("Email incorrecto")		




