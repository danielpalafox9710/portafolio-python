import pickle

#leer
fichero=open("lista_nombres","rb")

lista=pickle.load(fichero)

print(lista)


"""
Crear
lista_nombres=["Pedro", "Anda","Maria","Isabel"]

fichero_binario=open("lista_nombres","wb")

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

del(fichero_binario)

"""
