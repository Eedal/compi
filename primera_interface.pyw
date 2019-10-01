from tkinter import *

raiz=Tk()

raiz.title("Ventana de prueba")

#raiz.geometry("850x450")

raiz.resizable(1,1) #Hacer que no sea responsibo

raiz.iconbitmap("icono_pagina.ico")

raiz.config(bg="blue")

miFrame=Frame()


#miFrame.pack(side="right", anchor="n")
miFrame.pack(fill="x", expand="True")

miFrame.config(width="850", height="450")

miFrame.config(bg="red")


raiz.mainloop()