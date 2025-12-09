""" Ejemplo for Continue
for letra in "Python":
	if letra=="h":
		continue

	print ("Viendo la letra: " + letra)
"""

#Instrucción "Continue"
nombre="Pildoras informaticas"
contador=0

for i in nombre:

	if i==" ":
		continue

	contador+=1
	
print(contador)


#Instruccion Else
email=input("Introduce un correo: ")

for i in email:

	if i=="@":
		arroba=True

		break;						#El programa sale del ciclo for cuando detecta que hay un arroba

else:								#En caso de que jamas vea un arroba entrara al Else así dando False en la variable arroba
	arroba=False

print(arroba)

