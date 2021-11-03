"""
Autores:    Fabian Palacios 
            Angie Camelo
Proyecto: Analizador LL1
Clase en el que se realizan los procesos de análisis de la grámatica.
"""

class Primeros:
    
    def __init__(self, cadena):
        self.gramRecursionIzq = cadena
        self.noterminales = list(self.gramRecursionIzq.keys())
        self.prim = self.primeros()
        

    #Se le pasa el diccionares que retorna el metodo de recursionIzq,
    #Se crea un diccionario el cual va almacenar lo que le retorna el metodo procesoPrimeros
    #El metodo procesoPrimeros va a recibir como paramentro cada clave del diccionario de recursionIzq, producciones y no terminales
    def primeros(self):
        dic_Primeros=dict({})
        produciones = self.gramRecursionIzq
        noTerm = self.noterminales
        for i in produciones.keys():
            #Agregar al diccionario [i] = más lo que retorma 
            dic_Primeros[i]=self.procesoPrimeros(i, produciones, noTerm)
        return dic_Primeros


    #Metodo procesoPrimetos es un metodo recursivo que recive inicialmente las clave de la gramatica,
    #las produciones, noTerminales. entra la clave y verifica que haga parte de los noterminales,
    #si hace parte de los no terminales saca las respectivas producciones de esa gramatica y se las pasa al metodo
    #con el fin de ir verificando parte por parte hasta encontrar los no terminales de cada producción 
    def procesoPrimeros(self,seq, product, noterm):
        gra = product
        noTerminales =  noterm
        primeros_=set()
        for i in seq:
            flag=0
            if i in noTerminales:
                
                for j in gra[i]:
                    primeros_ = primeros_ | self.procesoPrimeros(j, gra, noTerminales)
                    if '@' in self.procesoPrimeros(j, gra, noTerminales):
                        flag = 1
                if flag == 0:
                    break
            else:
                lis = []
                for x in noTerminales:
                    if(seq.find(x) > 0):
                        lis.append(seq.find(x))

          
                if (len(lis) == 0):
                    aux = 0
                else:
                    aux = min(lis)

                #Si el numero de la lista es mayor a cero se toma de la palabra hasta encontrar ese no terminal si no completa la palabra
                if aux > 0:
                    primeros_=primeros_|{seq[:aux]}
                    break
                else:
                    primeros_ =primeros_|{seq}
                    break
        return primeros_


