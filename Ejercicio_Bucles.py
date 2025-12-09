numero=int(input("Introduce un número: "))

print("Tu numero es: ",numero)

while True:
	numero2=int(input("Introduce un número mayor al que me proporcionaste: "))


	if numero2>numero:
		print("El numero es correcto.")
		numero=numero2

	else:
		print("El numero es menor o igual, el programa ha finalizado...")

		break	
		


