import sqlite3

class GramaticaBD:
    
   def sql_conexion(self):
       try:
            # Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
            con = sqlite3.connect('gramaticaBD.db')
            return con
       except Error:
           return Error
      

   # Crear tabla
   def sql_table(self,con):
       try :
           cursorObj = con.cursor()

           cursorObj.execute("CREATE TABLE gramaticas(noterminales text, terminales text, gramatica text, RecursionIzq text, primeros text, siguientes text, prediccion text)")

           con.commit()
       except sqlite3.OperationalError:
           return sqlite3.OperationalError

   # Insertar en la tabla
   def sql_insert(self,con, entities):

        cursorObj = con.cursor()
    
        cursorObj.execute('INSERT INTO gramaticas (noterminales, terminales, gramatica, RecursionIzq, primeros, siguientes, prediccion) VALUES(?, ?, ?, ?, ?, ?, ?)', entities)
    
        con.commit()

    # Listar Datos
   def sql_fetch(self,con):

        cursorObj = con.cursor()

        cursorObj.execute('SELECT * FROM gramaticas')

        rows = cursorObj.fetchall()

        return rows
