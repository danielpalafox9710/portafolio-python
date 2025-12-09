print ("Programa de evaluacion de notas de alumnos") #Imprime titulo

nota_alumno=input("Introduce la nota del alumno: ")		#Declara variable y pide dato para ingresar a variable (Lo que entre al input es string por defecto)


def evaluacion(nota):		#Declara función
	valoracion="aprobado"	#Declara variable valoracion
	if nota<5:				#Condicional
		valoracion="suspenso"	#si es verdadero cambia el valor de evaluacion a suspenso
	return valoracion			#De lo contrario la variable se queda igual como aprobado

#Las variables solo son alcanzables dentro de un ambito "Dentro de if, funcion, etc" Fuera del ambito no llegará

print (evaluacion(int (nota_alumno)))		#Ejecuta con la variable ingresada (Int declara nota_alumno como entero)

