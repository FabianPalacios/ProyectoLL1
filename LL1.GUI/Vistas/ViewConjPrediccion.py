"""
Autores:    Fabian Palacios 
            Angie Camelo
Proyecto: Analizador LL1
Vista para la organización de los conjuntos producción.
"""
from tkinter import *
import tkinter as tk

class ViewConjPrediccion(object):
    # Constructor de la ventana
    def __init__(self, cadena):
        self.ventana(cadena)
        
    # Metodo que crea una ventana e inserta un panel de trabajo
    def ventana(self,cadena):
        self.view = Tk()
        self.gramatica = cadena
        self.diseño() 
        
        self.textAndInput()

        self.accionarConjPrediccion()

        self.view.mainloop()

    #Metodo de diseño de la ventana
    def diseño(self):
        self.view.title("Conjunto Predicción")
        
        ancho_ventana = 500
        alto_ventana = 350
        x_ventana = self.view.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.view.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.view.geometry(posicion)
       
    # Area de texto para mostrar la gramatica
    def textAndInput(self):
        label_1 = Label(self.view,text="CONJUNTO PREDICCIÓN").place(x=210, y=10)
        self.textBox = Text(self.view, height=15, width=57)
        self.textBox.place(x=20, y=35)

     # Realizar la carga del archivo
    def accionarConjPrediccion(self):
        info = self.gramatica
        
        for i in info:
           self.textBox.insert("insert","CP(" + i + ")" + " = " + str(info.get(i)) + '\n')

        self.textBox.configure(state='disabled')



