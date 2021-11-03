from tkinter import *
import tkinter as tk

class ViewRecursionIzq(object):
    # Constructor de la ventana   
    def __init__(self, cadena):
        self.ventana(cadena)
        
    # Metodo que crea una ventana e inserta un panel de trabajo
    def ventana(self,cadena):
        self.view = Tk()
        self.gramatica = cadena
        self.diseño() 
        

        self.textAndInput()
        self.textNoTerminales()

        self.accionarRecursionIzq()

        self.view.mainloop()

    #Metodo de diseño de la ventana 
    def diseño(self):
        self.view.title("Recursión Izquierda")
        
        ancho_ventana = 500
        alto_ventana = 350
        x_ventana = self.view.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.view.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.view.geometry(posicion)
       
    # Area de texto para mostrar la gramatica
    def textAndInput(self):
        label_1 = Label(self.view,text="RECURSIÓN IZQUIERDA").place(x=210, y=10)
        self.textBox=Text(self.view, height=15, width=30)
        self.textBox.place(x=140, y=63)

        
    # Area de texto para los no terminales
    def textNoTerminales(self):               
        label_2 = Label(self.view,text="No Terminales : ").place(x=80, y=33)
        self.textBox1=Text(self.view, height=1, width=30)
        self.textBox1.place(x=180, y=35)


     # Realizar la carga del archivo
    def accionarRecursionIzq(self):
        info = self.gramatica
        
        for i in info:
            self.textBox1.insert("insert",i+" ")
            for j in info.get(i):
                self.textBox.insert("insert",i+" -> "+j+'\n')

       
        self.textBox.configure(state='disabled')
        self.textBox1.configure(state='disabled')


