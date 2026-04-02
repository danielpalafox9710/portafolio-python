class Coche():		##Clase
	def __init__(self):				##Definición de clase
		self.largoChasis=250
		self.anchoChasis=120
		self.__ruedas=4
		self.enmarcha=False

	def arrancar(self,arrancamos):		##Metodo
		self.enmarcha=arrancamos

		if (self.enmarcha):
			chequeo=self.__chequeo_interno()

		if(self.enmarcha and chequeo):
			return "El coche esta en enmarcha"

		elif(self.enmarcha and chequeo==False):
			return "Algo ha ido mal en el chequeo. No podemos arrancar"

		else:
			return "El coche está parado"

	def estado(self):				##Metodo
		print("Ruedas: " , self.__ruedas , "Chasis: " , self.largoChasis)


	def __chequeo_interno(self):				##Metodo
		print ("Realizando chequeo interno...")
		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"


		if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):

			return True

		else:
			return False


miCoche=Coche()	#Instanciar una clase
print(miCoche.arrancar(True))
miCoche.estado()


print ("-------------A continuacion creamos el segundo objeto----------------")

miCoche2=Coche() #Instancia de una clase
print(miCoche2.arrancar(False))
##miCoche2.__ruedas=2 							Esta linea la usamos para verificar que el dato esté encapsulado
miCoche2.estado()


