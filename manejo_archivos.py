from io import open

archivo_texto=open("archivo.txt","r+")

lista_texto=archivo_texto.readlines();

lista_texto[1]="Esta línea ha sido incluida \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)
archivo_texto.close()
"""

#print(archivo_texto.read(11))

archivo_texto.seek(len(archivo_texto.readline()))

print(archivo_texto.read())
"""

"""
archivo_texto.write("\nsiempre es una buena ocasión para estudiar")

archivo_texto.close()

#Tercera fase del codigo
"""
"""

lineas_texto=archivo_texto.readlines()

archivo_texto.close()

print (lineas_texto[0])
"""
#Segunda fase del programa
"""
texto=archivo_texto.read()

archivo_texto.close()

print (texto)"""

#Primera fase del programa

"""frase="Estupendo dia para estudiar \nEl Miercoles"

archivo_texto.write(frase)

archivo_texto.close()"""

