"""
Autores:    Fabian Palacios 
            Angie Camelo
Proyecto: Analizador LL1
Clase en el que se realizan los procesos de análisis de la grámatica.
"""

from Controladores.Primeros import Primeros


class Siguientes:
    
     def __init__(self, gramRecursionIzq):
        self.gramRecursionIzq = gramRecursionIzq
        self.noTerminales = list(self.gramRecursionIzq.keys())
        
        #Instancia de la clase Primeros
        self.primeros = Primeros(self.gramRecursionIzq)

        self.sig = self.siguientes()


        

        #Método para organizar los siguientes.
     def siguientes(self):
        #Se crea un diccionario donde ingresarán los siguientes.
        dic_Siguientes = dict({})
        #Se llama la función que devuelve la grámatica posterior al proceso de
        #recursión izquierda.
        produciones = self.gramRecursionIzq
        #Se obtienen los noterminales.
        noTerm = self.noTerminales
        #Se realiza un for si i pertenece a las llaves de las producciones de
        #la grámatica.
        for i in produciones.keys():
            #Agregar al diccionario [i] = lo que retorma el método
            #procesoSiguientes por cada llave.
            dic_Siguientes[i] = self.procesoSiguientes(i, produciones, noTerm)
        #Retornamos el diccionario organizado con los siguientes de cada
        #producción.
        return dic_Siguientes
    
    
        #Método para hallar los siguientes de cada producción.  Recibe la llave,
        #las producciones de la grámatica y los no terminales.
     def procesoSiguientes(self,  var_nt, product, noterm):
        #Se realiza una referencia a las funciones de producciones y no
        #terminales.
        gra = product
        noTerminales = noterm
        #Se crea una conjunto para guardar los siguientes.
        siguientes_ = set()
        #Se inicializa la variable con la primer llave de la primer producción.
        start_var = (list(gra.keys())[0])  

        #Caso 1.  Si x es la prod.  inicial agregar $ a los Sig(x)
        if var_nt == start_var:
            siguientes_ = siguientes_ | {'$'}
        #Recorremos las producciones.
        for x in gra:
            for prod in gra[x]:
                #Si la producción es diferente @.
                if prod != '@':
                    #Verificamos que i este en el rango del tamaño de
                    #caracteres de la producción.
                    for i in range(len(prod)):
                        #Si el caracter en la posición i es igual a la key
                        if prod[i] == var_nt:
                            # Si i es diferente a la long -1 de la producción
                            if i != (len(prod) - 1):
                                #Hallamos el adyacente (el del lado derecho.
                                #posición +1)
                                adyacente = prod[(i + 1):]
                                #Hallamos sus primeros.
                                primAdyac = self.primeros.procesoPrimeros(adyacente,product,noterm)
                                #Si b es @, entonces agregar a los Sig(x) los
                                #sig(A) exceptuando @
                                if '@' in primAdyac:
                                    siguientes_ = siguientes_ | (primAdyac - {'@'}) 
                                    #Si el x es diferente a la key que entra,
                                    #mandamos los sig(x)
                                    if(x != var_nt):
                                        siguientes_ = siguientes_ | self.procesoSiguientes(x,product,noterm) 
                                #Si b es diferente a @, se toman los primeros
                                #del adyacente.
                                else:
                                    siguientes_ = siguientes_ | primAdyac
                            #Si i es igual a la long-1 de la producción
                            else:
                                #Si el x es diferente a la key que entra,
                                #mandamos los sig(x)
                                if(x != var_nt):
                                    siguientes_ = siguientes_ | self.procesoSiguientes(x,product,noterm)
        #Se retorna el conjunto de siguientes.
        return siguientes_


