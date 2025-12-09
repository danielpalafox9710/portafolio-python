salario_presidente=int(input("Introduce salario presidente: "))
print ("Salario presidente: " + str(salario_presidente))

salario_director=int(input("Introduce salario director: "))
print ("Salario director: " + str(salario_director))

salario_jefe=int(input("Introduce salario jefe: "))
print ("Salario jefe: " + str(salario_jefe))

salario_administrativo=int(input("Introduce salario administrativo: "))
print ("Salario administrativo: " + str(salario_administrativo))

if salario_administrativo<salario_jefe<salario_director<salario_presidente:	#Se puede concatenar
	print ("Todo funciona correctamente.")									#Distintos operadores en un solo if
else:
	print("Algo falla en la empresa")






