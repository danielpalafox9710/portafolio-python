numero=int(input("Introduce un número positivo: "))
lista=[numero]

while True:

	if numero>=0:

		numero2=int(input("Dame otro número positivo: "))
		numero=numero2
		lista.append(numero2)
	else:
		print("Ingresaste un número en negativo...")
		print("La suma de tus números positivos es: ")	
		lista.pop()
		suma=sum(lista)
		print(suma)
		break


