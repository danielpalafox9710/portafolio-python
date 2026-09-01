from tkinter import *

raiz=Tk()

raiz.title("Ventana de pruebas")

#w ancho h alto
#raiz.resizable(0,0) Era solo el ejemplo

raiz.iconbitmap("Icono.ico")

#raiz.geometry("650x350")

raiz.config(bg="Blue")

miFrame=Frame()

miFrame.pack(side="left", anchor="n")

miFrame.config(bg="red")

miFrame.config(width="650",height="350")

miFrame.config(bd=35)

miFrame.config(relief="sunken")

miFrame.config(cursor="pirate")

raiz.mainloop()




