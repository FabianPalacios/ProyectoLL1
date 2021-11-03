"""
Autores:    Fabian Palacios 
            Angie Camelo
Proyecto: Analizador LL1
Clase en el que se realizan los procesos de análisis de la grámatica.
"""
from Controladores.Primeros import Primeros
from Controladores.Siguientes  import Siguientes


class ConjuntoPrediccion:
    def __init__(self, gramRecursionIzq):
        self.gramRecursionIzq = gramRecursionIzq
        self.noTerminales = list(self.gramRecursionIzq.keys())
        
        #Instancia de la clase Primeros
        self.primeros = Primeros(self.gramRecursionIzq)

        #Instancia de la clase Siguientes
        self.siguientes =  Siguientes(self.gramRecursionIzq)

        self.predic = self.conjPrediccion()
        self.resultado = self.conjPrediccionResp()




    # Método para organizar los conjuntos predicción.
    def conjPrediccion(self):
        #Se crea un diccionario donde ingresarán los conjuntos predicción.
        dic_CPrediccion = dict({})
        #Se llama la función que devuelve la grámatica posterior al proceso de
        #recursión izquierda.
        producciones = self.gramRecursionIzq
        #Se obtienen los noterminales.
        noTerm = self.noTerminales
        #Se realiza un for si i pertenece a las llaves de las producciones de
        #la grámatica.
        for i in producciones.keys():
            #Agregar al diccionario [i] = lo que retorma el método de
            #procesoconjuntoPrediccion por cada llave.
            dic_CPrediccion[i] = self.procesoconjuntoPrediccionV(i,producciones, noTerm)
        #Retornamos el diccionario organizado con el conjunto predicción de
        #cada producción.
        return dic_CPrediccion

    #Método para hallar la intersección de los conjuntos predicción y verificar
    #si es LL1 o no.
    def conjPrediccionResp(self):
        #Booleano para saber si es LL1 o no.
        esLL1 = True
        #Se llama la función que devuelve la grámatica posterior al proceso de
        #recursión izquierda.
        producciones = self.gramRecursionIzq
        #Se obtienen los noterminales.
        noTerm = self.noTerminales
        for noTerminal in noTerm:
            lista = []
            for produccion in producciones:
                if(produccion[0] == noTerminal):
                    for cp in self.procesoconjuntoPrediccion(produccion[0],producciones,noTerm):
                        #Si esta prediccion ya esta en la lista es por que hay
                        #intersección
                        #si no es asi, la agrega a la lista
                        if(cp in lista):
                            esLL1 = False
                        lista.append(cp)
        #Retornamos si es LL1 o no.
        return esLL1

    #Método para hallar el conjunto predicción de cada producción.  Recibe la
    #llave,las producciones de la grámatica y los no terminales.
    def procesoconjuntoPrediccionV(self, var_nt, product, noterm):
        #Se realiza una referencia a las funciones de producciones y no
        #terminales.
        gra = product
        noTerminales = noterm
        #Se crea una conjunto para guardar el conjunto predicción.
        conjPrediccion_ = set()
        
        for var in gra:
            if(var_nt == var):
               for prod in gra[var]:
                   #Tomamos el primer caracter de la producción.
                    x = prod[0]
                    #Caso 1 : Si x es @, se añaden los sig(var).
                    if(x == '@'):
                        conjPrediccion_ = conjPrediccion_ | self.siguientes.procesoSiguientes(var,gra,noTerminales) 
                    #Caso 2 : Si x pertenece a los no terminales, se añaden los
                    #Prim(x).
                    elif(x in noterm):
                        conjPrediccion_ = conjPrediccion_ | self.primeros.procesoPrimeros(prod,gra,noTerminales)
                    #Caso 3 : x es un terminal, se añade este terminal.
                    else:
                        lis = []
                        for i in noTerminales:
                            if(prod.find(i) > 0):
                                lis.append(prod.find(i))
                        
                        if (len(lis) == 0):
                            aux = 0
                        else:
                            aux = min(lis)


                        #Si el numero de la lista es mayor a cero se toma de la palabra hasta encontrar ese no terminal si no completa la palabra
                        if aux > 0:
                            conjPrediccion_ = conjPrediccion_ |{prod[:aux]}
                        else:
                            conjPrediccion_ = conjPrediccion_|{prod}
        #Se retorna el conjunto.
        return conjPrediccion_

    #Método para hallar el conjunto predicción de cada producción.  Recibe la
    #llave, las producciones de la grámatica y los no terminales.
    def procesoconjuntoPrediccion(self, var_nt, product, noterm):
        #Se realiza una referencia a las funciones de producciones y no
        #terminales.
        gra = product
        noTerminales = noterm
        #Inicializamos una lista en la que verificaremos la intersección.
        procesoconjuntoPrediccion = []
        
        for var in gra:
            if(var_nt == var):
               for prod in gra[var]:
                   #Tomamos el primer caracter de la producción.
                    x = prod[0]
                    #Caso 1 : Si x es @, se añaden los sig(var).
                    if(x == '@'):
                        procesoconjuntoPrediccion.extend(self.siguientes.procesoSiguientes(var,gra,noTerminales) )
                    #Caso 2 : Si x pertenece a los no terminales, se añaden los
                    #Prim(x).
                    elif(x in noterm):
                        procesoconjuntoPrediccion.extend(self.primeros.procesoPrimeros(prod,gra,noTerminales))
                    #Caso 3 : x es un terminal, se añade este terminal.
                    else:
                        lis = []
                        for i in noTerminales:
                            if(prod.find(i) > 0):
                                lis.append(prod.find(i))

                        if (len(lis) == 0):
                            aux = 0
                        else:
                            aux = min(lis)

                        #Si el numero de la lista es mayor a cero se toma de la palabra hasta encontrar ese no terminal si no completa la palabra
                        if aux > 0:
                            procesoconjuntoPrediccion.append(prod[:aux])
                        else:
                            procesoconjuntoPrediccion.append(prod)

        #Se retorna la lista.
        return procesoconjuntoPrediccion


