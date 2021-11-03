"""
Autores:    Fabian Palacios 
            Angie Camelo
Proyecto: Analizador LL1
Clase en el que se realizan los procesos de análisis de la grámatica.
"""
import random

class RecursionIzquierda:

    def __init__(self, cadena):
        self.gramLimpia = cadena
        self.noterminales = list(self.gramLimpia.keys())
        self.gramRecursionIzq = self.recursionIzq()


    #Metodo para aplicar recursión izquierda 
    def recursionIzq(self):
        gram = self.gramLimpia
        dic = dict({})
        lista = []
        listaprima = []
        for i in gram.keys():
            lista = []
            listaprima = []
            #crear letra
            aux = self.letras()
            for j in gram.get(i):
                #E --> E*T 
                if(i == j[0]):

                    for x in gram.get(i):
                        if (i != x[0]):
                           
                            if(self.buscar(lista, x+aux) == False):
                                lista.append(x+aux)
                        else:
                            if(self.buscar(listaprima, x[1:]+aux) == False):
                                listaprima.append(x[1:]+aux)
            
            listaprima.append("@")
            dic[i] = lista
            if(listaprima[0] != "@"):
                dic[aux] = listaprima

        #Si no presentan recursión lista va estar vacio y debemos agregar esa producción
        for z in dic.keys():
            if (dic.get(z) == []):
                dic.update({z :gram.get(z)})
        
        return dic

    #Metodo para buscar un valor en una lista
    def buscar(self,lista, busco):
        for i in range(len(lista)):
            if (lista[i] == busco):
                return True
                break
        return False

    def letras(self):
        bandera = True
        while bandera:
          aux = chr(random.randrange(65, 90,1))
          if (self.buscar(self.noterminales, aux) == False):
              self.noterminales.append(aux)
              bandera = False
              return aux



