"""
	def evaluaEdad(edad):
	if edad<0:
		raise TypeError("No se permiten edades negativas")

	if edad<20:
		return "Eres muy joven"
	elif edad<40:
		return "Eres Joven"
	elif edad<65:
		return "Eres maduro"
	elif edad<100:
		return "Cuidate"

print (evaluaEdad(-1))
"""

import math

def calcula(num1):

	if num1<0:
		raise ValueError("No puede ser negativo")
	else:
		return math.sqrt(num1)

op1=(int(input("Introduce un número: ")))
try:
	print (calcula(op1))
except ValueError as ErrorDeNumeroNegativo:
	print("ErrorDeNumeroNegativo")
	
print("Programa terminado")

