import pyttsx3
from tkinter import *

raiz=Tk()
miFrame=Frame(raiz)
miFrame.pack()
operacion=""
resultado=0


#------------------------Pantalla------------------------
numeroPantalla=StringVar()

pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=2, pady=0, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

#------------------------------Pulsaciones teclado-------------------------------
def numeroPulsado(numero):
    #-------lo mio-----------


    global operacion
    if operacion=="suma":
        numeroPantalla.set(numero)
        operacion=""
    else:
        numeroPantalla.set(numeroPantalla.get() + numero)



    #---------------------------
    '''global operacion
    if operacion!="":
        numeroPantalla.set(numero)
        operacion=""
    else:
        numeroPantalla.set(numeroPantalla.get() + numero)'''

#------------------------------Funcion suma-------------------------------------
def suma(numero):
   global operacion
   global resultado
   resultado+=int(numero)
   operacion="suma"
   numeroPantalla.set(resultado)

#-----------------------------Funcion resta-------------------------------------
def resta(numero):
   pass


#------------------------------Funcion el_resultado-----------------------------
def el_resultado():
    global resultado
    numeroPantalla.set(resultado + int(numeroPantalla.get()))
    resultado=0

#-----------------------------Funcion de borrar---------------------------------
def AC(frase):
    numeroPantalla.set("")
    resultado=0
    engine = pyttsx3.init()
    engine.setProperty('volume', 2.0)
    engine.setProperty('rate', 180)
    engine.setProperty('voice', 'spanish')
    engine.say(frase)
    engine.runAndWait()

def CE():
    if(int(len(numeroPantalla.get()))!=0):
        numeroPantalla.set(numeroPantalla.get()[:int(len(numeroPantalla.get()))-1])
#----------------------------------Operaciones-------------------------------------




#--------------------------Fila 1------------------------
botonAC=Button(miFrame, text="AC", width=6, command=lambda:AC(numeroPantalla.get()))
botonAC.grid(row=2, column=1)
botonCE=Button(miFrame, text="CE", width=6, command=lambda:CE())
botonCE.grid(row=2, column=3)


#--------------------------Fila 2------------------------
boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=3, column=1)
boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=3, column=2)
boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=3, column=3)
botonDiv=Button(miFrame, text="/", width=3)
botonDiv.grid(row=3, column=4)

#--------------------------Fila 3------------------------
boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=4, column=1)
boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=4, column=2)
boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=4, column=3)
botonMult=Button(miFrame, text="*", width=3)
botonMult.grid(row=4, column=4)

#--------------------------Fila 4------------------------
boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=5, column=1)
boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=5, column=2)
boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=5, column=3)
botonRest=Button(miFrame, text="-", width=3, command=lambda:resta(numeroPantalla.get()))
botonRest.grid(row=5, column=4)

#--------------------------Fila 5------------------------
boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=6, column=1)
botonComa=Button(miFrame, text=",", width=3, command=lambda:numeroPulsado(","))
botonComa.grid(row=6, column=2)
botonIgual=Button(miFrame, text="=", width=3, command=lambda:el_resultado())
botonIgual.grid(row=6, column=3)
botonSum=Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=6, column=4)







raiz.mainloop()
