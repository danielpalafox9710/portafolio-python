from tkinter import *

raiz = Tk()
minombre=StringVar()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1)
cuadroNombre.config(fg="red", justify="center")

#Cuadro de ingreso de información
cuadroPass=Entry(miFrame)
cuadroPass.grid(row=2, column=1)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1)

#Cuadro de texto simple, junto con una barra de scroll configurada
textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=4, column=1, pady=10)
scrollvert=Scrollbar(miFrame, command=textoComentario.yview)
scrollvert.grid(row=4, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollvert.set)

#Etiquetas, es un simple texto puedo a lado de nuestros cuadros de información
nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0,sticky="e" , pady=10)

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=1, column=0,sticky="e" , pady=10)

PassLabel=Label(miFrame, text="Password: ")
PassLabel.grid(row=2, column=0,sticky="e" , pady=10)

PassLabel=Label(miFrame, text="Dirección: ")
PassLabel.grid(row=3, column=0,sticky="e" , pady=10)

comentariosLabel=Label(miFrame, text="Comentarios: ")
comentariosLabel.grid(row=4, column=0,sticky="e" , pady=10)

#Definimos una función para el botón

def codigoBoton ():

	minombre.set("Juan")

#Creamos el botón
botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)

botonEnvio.pack()

raiz.mainloop()