from tkinter import *

root=Tk()
root.title("Ejemplo")

playa=IntVar()
montana=IntVar()
rural=IntVar()

def opcionesViaje():
	
	opcionEscogida=""

	if(playa.get()==1):
		opcionEscogida+="Playa "

	if(montana.get()==1):
		opcionEscogida+="Montana "
	if(rural.get()==1):
		opcionEscogida+="Rural "

	textoFinal.config(text=opcionEscogida)

#foto=PhotoImage(file="C:/Users/jonathan.palafox/Documents/Codigos Python+/Codigos Sublime/Practica/images.jpg")
#Label(root, image=foto).pack()

Checkbutton(root, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root, text="Montaña",variable=montana, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root, text="Rural",variable=rural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(root)
textoFinal.pack()

root.mainloop()