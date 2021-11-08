"""
Autores:    Fabian Palacios 
            Angie Camelo
Proyecto: Analizador LL1
Clase en el que se realizan los procesos de análisis de la grámatica.
"""

from Controladores.RecursionIzquierda import RecursionIzquierda
from Controladores.Primeros import Primeros
from Controladores.Siguientes import Siguientes
from Controladores.ConjuntoPrediccion import ConjuntoPrediccion

from GramaticaBD import GramaticaBD

class ControlGramatica(object):
    """description of class"""

    conexion = GramaticaBD()

    def __init__(self, cadena,terminales):
        self. gramatica = cadena
        self.gramLimpia = self.leerGramatica()
        self.noTerminales = list(self.gramLimpia.keys())
        self.terminales = terminales

        #Instancia de la clase RecursionIzquierda
        self.RecursionIzq = RecursionIzquierda(self.gramLimpia)
        self.gramRecursionIzq = self.RecursionIzq.gramRecursionIzq

        #Instancia de la clase Primeros
        self.primeros = Primeros(self.gramRecursionIzq)
        self.prim = self.primeros.prim

        #Instancia de la clase Siguientes
        self.siguientes = Siguientes(self.gramRecursionIzq)
        self.sig = self.siguientes.sig

        #Instancia de la clase ConjuntoPrediccion
        self.conjuntoPrediccion =  ConjuntoPrediccion(self.gramRecursionIzq)
        self.predic = self.conjuntoPrediccion.predic
        self.resultado = self.conjuntoPrediccion.resultado
       
        self.con = self.conexion.sql_conexion()
        self.conexion.sql_table(self.con)


    # Verifica si hay recursión Izquierda
    def verificar(self):
        if (len(self.gramRecursionIzq) > len(self.gramLimpia)):
            return True
        return False

    #Captura la lista de gramatica y la convierte en un diccionario por
    #gramatica
    def leerGramatica(self):
        #Recibe la lista de gramaticas
        lista = self.gramatica
        gramaticas = dict({})
        for i in lista:
            #Separa por palabra ['E','->','AT/@']
            palabras = i.split()
            #Separa por | = ['T','@']
            produciones = palabras[2].split('|')
            #Arma el diccionario
            gramaticas[palabras[0]] = produciones
        return gramaticas


    def guardar(self):
        entities = (str(self.noTerminales),str(self.terminales), str(self.gramLimpia), str(self.gramRecursionIzq),str(self.prim),str(self.sig),str(self.predic))
        self.conexion.sql_insert(self.con, entities)

