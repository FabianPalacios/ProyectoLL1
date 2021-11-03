from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class Tabla(object):
    def __init__(self, cadena):
        self.ventana(cadena)
        
    # Metodo que crea una ventana e inserta un panel de trabajo
    def ventana(self,cadena):
        self.view = Tk()
        self.gramatica = cadena
        self.diseño() 

        self.accionarPrim()

        self.view.mainloop()

    #Metodo de diseño de la ventana 
    def diseño(self):
        self.view.title("LISTA")
        
        ancho_ventana = 1000
        alto_ventana = 250
        x_ventana = self.view.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.view.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.view.geometry(posicion)

   
     # Listar
    def accionarPrim(self):
        rows = self.gramatica

        columns = ('#1', '#2', '#3','#4', '#5')
        
        self.treeview = ttk.Treeview(self.view, columns=columns,show='headings')
        self.treeview.pack()

        # Añadimos encabezados
        self.treeview.heading("#1", text="No Terminales")
        self.treeview.heading("#2", text="Terminales")
        self.treeview.heading("#3", text="Gramatica")
        self.treeview.heading("#4", text="Recursión Izquierda")
        self.treeview.heading("#5", text="Prim")

        for i in rows:
            self.treeview.insert("", tk.END,  values = i)

        scrollbar = ttk.Scrollbar(self.view, orient=tk.VERTICAL, command=self.treeview.yview)
        self.treeview.configure(yscroll=scrollbar.set)


