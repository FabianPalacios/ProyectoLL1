from tkinter import *
import tkinter as tk
import os
import pickle
from tkinter import  messagebox as MessageBox

#LogicaNegocio
from CargarArchivo.CargarArchivo import CargarArchivo
from Controladores.ControlGramatica import ControlGramatica

#Vista
from Vistas.ViewRecursionIzq import ViewRecursionIzq
from Vistas.ViewPrimeros import ViewPrimeros
from Vistas.Tabla import Tabla
from Vistas.ViewSiguientes import ViewSiguientes
from Vistas.ViewConjPrediccion import ViewConjPrediccion

#Acceso Datos
from GramaticaBD import GramaticaBD

class View(object):
    #Instancia de la clase CargarArchivo
    data = CargarArchivo()
    conexion = GramaticaBD()
    

    # Constructor de la ventana
    def __init__(self):
        self.ventana()
        
        
    # Metodo que crea una ventana e inserta un panel de trabajo
    def ventana(self):
        self.view = Tk()
        self.diseño() 
        
        self.con = self.conexion.sql_conexion()
        self.cont = 0
        
        self.definirOpen()
        self.definirList()
        self.textContador()

        self.textAndInput()
        self.textNoTerminales()
        self.textTerminales()

        self.botonesDesativados()
        self.logo()
        self.view.mainloop()

    #Metodo de diseño de la ventana
    def diseño(self):
        self.view.title("Analizador LL(1)")
        self.menuBar = Menu(self.view)
        self.view.config(menu=self.menuBar)

        ancho_ventana = 500
        alto_ventana = 450
        x_ventana = self.view.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.view.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.view.geometry(posicion)
        
        self.panel = Frame(self.view,width=500, height=350).pack()
    
    #Logo y materia
    def logo(self):
        absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
        absolute_image_path = os.path.join(absolute_folder_path, 'logo3.png')
        imagen = PhotoImage(file=absolute_image_path)
        logo = Label(self.panel, image =imagen).place(x=0,y=0)
        label_Materia = Label(self.panel,text="Estructura de lenguajes").place(x=370, y=3)
        
        self.view.mainloop()
        

    # Definiendo las funciones que va a tener el menu Archivos
    def definirOpen(self):
        filemenu = Menu(self.menuBar,tearoff=0)
        self.menuBar.add_cascade(label="Archivo", menu=filemenu)
        filemenu.add_command(label="Abrir", command= self.accionarCargarArchivo)
        filemenu.add_command(label="Guardar", command= self.guardar)
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.view.quit)

    # Definiendo las funciones que va a tener el menu Ver
    def definirList(self):
        listmenu = Menu(self.menuBar,tearoff=0)
        self.menuBar.add_cascade(label="Ver", menu=listmenu)
        listmenu.add_command(label="Listar Gramaticas", command = self.listar)

    # Area de texto para mostrar la gramatica
    def textAndInput(self):
        label_1 = Label(self.panel,text="GRAMATICA").place(x=210, y=10)
        self.textBox = Text(self.panel, height=10, width=30)
        self.textBox.place(x=140, y=100)
        
    # Area de texto para los no terminales
    def textNoTerminales(self):               
        label_2 = Label(self.panel,text="No Terminales : ").place(x=125, y=33)
        self.textBox1 = Text(self.panel, height=1, width=20)
        self.textBox1.place(x=225, y=35)
        
     # Area de texto para los no terminales
    def textTerminales(self):               
        label_3 = Label(self.panel,text="Terminales : ").place(x=125, y=60)
        self.textBox2 = Text(self.panel, height=1, width=20)
        self.textBox2.place(x=225, y=63)

    # Area de texto para contador
    def textContador(self):               
        label_4 = Label(self.panel,text="CONTADOR : ").place(x=205, y=425)
        self.text = tk.StringVar()
        self.text.set("0")
        self.label = tk.Label(self.panel, textvariable=self.text).place(x=285, y=425)


    # Todos los botones desativados
    def botonesDesativados(self):
        boton1 = Button(self.panel, text="Verificar", width=20,height=2, background="SkyBlue2",state=DISABLED).place(x=180,y=270)
        boton2 = Button(self.panel, text="Recursión Izquierda", width=20,height=2, background="SkyBlue2",state=DISABLED).place(x=180,y=320)
        boton3 = Button(self.panel, text="Primeros", width=20,height=2, background="SkyBlue2",state=DISABLED).place(x=15,y=380)
        boton4 = Button(self.panel, text="Siguientes", width=20,height=2, background="SkyBlue2",state=DISABLED).place(x=175,y=380)
        boton5 = Button(self.panel, text="Conjunto Predicción", width=20,height=2, background="SkyBlue2",state=DISABLED).place(x=335,y=380)
    
        
    # Botones verificar
    def botonVerificar(self):
        boton1 = Button(self.panel, text="Verificar", width=20,height=2, background="SkyBlue2",
                        command= self.verificarGramatica).place(x=180,y=270)

    # Boton Recursión Izquierda
    def botonRecursionIzquierda(self):
        boton2 = Button(self.panel, text="Recursión Izquierda", width=20,height=2, background="SkyBlue2",
                        command = self.viewRecursionIzquierda).place(x=180,y=320)
        
    # Boton Prim
    def botonPrimeros(self):
        boton3 = Button(self.panel, text="Primeros", width=20,height=2, background="SkyBlue2",
                        command = self.viewPrim).place(x=15,y=380)
        
    # Boton Siguientes
    def botonSiguientes(self):
        boton4 = Button(self.panel, text="Siguientes", width=20,height=2, background="SkyBlue2",
                        command = self.viewSiguiente).place(x=175,y=380)

    # Boton Conjunto Predicción
    def botonConjuntoPrediccion(self):
        boton5 = Button(self.panel, text="Conjunto Predicción", width=20,height=2, background="SkyBlue2",
                        command = self.viewConjuntoPrediccion).place(x=335,y=380)

    # Realizar la carga del archivo
    def accionarCargarArchivo(self):
        self.textTerminales()
        self.textNoTerminales()
        self.textAndInput()

        self.archivo = self.data.abrirArchivo()

        for i in self.archivo["gramatica"]:
            self.textBox.insert("insert",i + '\n')
       
        for x in self.archivo["noterminales"]:
            self.textBox1.insert("insert",x + " ")

        for j in self.archivo["terminales"]:
            self.textBox2.insert("insert",j + " ")
        
        self.textBox.configure(state='disabled')
        self.textBox1.configure(state='disabled')
        self.textBox2.configure(state='disabled')

        self.botonVerificar()
        
    

    # Verificar si la gramatica es LL1
    def verificarGramatica(self):
        self.controlTotal = ControlGramatica(self.archivo["gramatica"], self.archivo["terminales"])
        respuesta = self.controlTotal.resultado
        
        if(self.controlTotal.verificar() == True):
            info = MessageBox.askquestion("Verificación LL1!", "La gramatica no es LL1, puede presenta recursión Izquierda ¿Desea aplicar recursión izquierda?")
            if (info == "yes"):
                self.botonRecursionIzquierda()
                info1 = MessageBox.askquestion("Verificación LL1!", "La gramatica esta en LL1, ¿Desea aplicar cada uno de los procesos")

                if (info1 == "yes"):
                    self.botonPrimeros()
                    self.botonSiguientes()
                    self.botonConjuntoPrediccion()

                    
                    self.cont += 1
                    self.text.set(self.cont)

                if(respuesta):
                    info2 = MessageBox.showinfo("Verificación","Esta gramática es compatible para un analizador LL1")
                else:
                    info3 = MessageBox.showinfo("Verificación","Esta gramática NO es compatible para un analizador LL1")
                

        else: 
            resultado = MessageBox.askquestion("Verificación LL1", "La gramatica esta en LL1, ¿Desea continuar?")

            if(resultado == "yes"):
                self.botonPrimeros()
                self.botonSiguientes()
                self.botonConjuntoPrediccion()

                if(respuesta):
                    info2 = MessageBox.showinfo("Verificación","Esta gramática es compatible para un analizador LL1")
                else:
                    info3 = MessageBox.showinfo("Verificación","Esta gramática NO es compatible para un analizador LL1")


   # Vista de la ventana recursión Izquierda
    def viewRecursionIzquierda(self):
        ViewRecursionIzq(self.controlTotal.gramRecursionIzq)

    # Vista de la ventana Prim
    def viewPrim(self):
        ViewPrimeros(self.controlTotal.prim)

    # Vista de la ventana Siguientes
    def viewSiguiente(self):
        ViewSiguientes(self.controlTotal.sig)

    # Vista de la ventana Conjunto Prediccion
    def viewConjuntoPrediccion(self):
        ViewConjPrediccion(self.controlTotal.predic)
    
    #  Guardar en la base de datos
    def guardar(self):
        self.controlTotal.guardar()
        info2 = MessageBox.showinfo("Guardar","La información ha sido almacenada correctamente.")
        
    # Vista de la Tabla
    def listar(self):
        rows = self.conexion.sql_fetch(self.con)
        Tabla(rows)



