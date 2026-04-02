correo=input("Introduce un correo electronico: ")



while (correo.count('@')!=1) or (correo.find('@')==0) or (correo.find('@')==len(correo)-1):
	print("El correo es invalido...")
	correo=input("Introduce un correo electronico valido: ")


print("La dirección de correo es valida...")








