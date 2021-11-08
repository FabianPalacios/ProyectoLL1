# ProyectoLL1
Proyecto Terminado

La empresa de desarrollo “ACME” esta creando un nuevo lenguaje de programación “el calamar” y 
para ello requiere con suma urgencia la sistematización del analizador LL1 con sus componentes:
• Primeros
• Siguientes
• Conjunto Predicción

Requerimientos 

RNFI01 ->  El sistema debe recibir por medio de un json la parametrización lo que es el 
            conjunto de producciones como mínimo.
            
RNFI02 ->  Una vez cargado el json el sistema debe tener en su interfaz grafica, un botón 
            para que permita la verificación de la gramática si es LL1, si no aplica recursión izquierda.
            
RNFI03 ->  Una vez realizada la verificación, el sistema debe mostrar por interfaz grafica 
            cada uno de los procesos realizados es decir, Primero ,Siguientes y por ultimo 
            conjunto predicción.
            
RNFI04 ->  El sistema debe informar si la gramática ingresada pertenece a lenguaje. 

RNFI05 ->  El sistema debe permitir el ingreso de nuevo de una gramática y llevar el 
            control de cuantas gramáticas se han realizado.

RNFI06 ->  Las gramáticas que cumplan deben guardarse en una base de datos. Y en 
            cualquier momento estas se pueden listar.
            
RNFA04 La base de datos usamos SQLite

RNFA06 Lenguaje de programación  Python
            
Los documentos que deben entregar son:
• Diagrama de casos de uso.
• Diagrama ER
• Diagrama de Clases.
• Sistema funcionando
