from tkinter import filedialog
import json

class CargarArchivo:
    #Metodo para abrir el archivo, capturamos la ruta de solo archivos json y hacemos la lectura del archivo json
    #Return data
    def abrirArchivo(self):
        archivo = filedialog.askopenfilename(title = "abrir", initialdir="C:/", filetypes=[("Documentos de texto", "*.Json")])
        
        data = json.loads(open(archivo).read())
        return data


