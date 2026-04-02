class persona():
	def __init__(self,nombre, edad, lugar): #Indica la clase padre
		
		self.nombre=nombre
		self.edad=edad
		self.lugar=lugar

	def descripcion(self):

		print("Nombre: ", self.nombre, "\nEdad: ", self.edad, "\nLugar: ", self.lugar)

class empleado(persona):
	def __init__(self, salario, antiguedad,nombre_empleado,edad_empleado,residencia_empleado):

		super().__init__(nombre_empleado, edad_empleado,residencia_empleado) #Super indica que va y busca la función padre

		self.salario=salario
		self.antiguedad=antiguedad

	def descripcion(self):

		super().descripcion() #significa que va a buscar la funcion descrpcion en la clase padre

		print ("Salario: ",self.salario,"\nAntigüedad: ", self.antiguedad)

manuel=empleado(1500, 15, "Manuel",55,"Mexico")

manuel.descripcion()

print(isinstance(manuel, persona))





