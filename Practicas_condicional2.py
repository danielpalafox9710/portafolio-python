def practica():
	print("Programa de becas")

	distancia=int(input("Introduce distancia a la escuela en km: "))
	print (distancia)
	numero_hermanos=int(input("Introduce el número de hermanos en el centro: "))
	print(numero_hermanos)
	salario=int(input("Introduce salario anual bruto: "))
	print (salario)



	if distancia>40 and numero_hermanos>2 or salario<=20000:

		print ("Tienes derecho a beca")

	else:

		print("No tienes derecho a beca")
##Primera función------------------------------------------------------------------------------------------
def practica2():
	print("Asignaturas optativas año 2025")
	print("Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")

	Asignatura=input("Escribe la asignatura escodida: ").lower()


	if Asignatura in("informatica grafica","pruebas de software","usabilidad y accesibilidad"):

		print("Asignatura elegida es " + Asignatura.capitalize())

	else:

		print("La asignatura escogida no está contemplada")
##Segunda función---------------------------------------------------------------------------------------
#Main:

practica()
practica2()