import tkinter as tk
from  Analizador_Lexico.lexerMain  import analizar
from AnalizadorSintactico.sintactico_yacc import leerCodigo

class Ventana:
    # Le pasamos el componente raíz al constructor
    def __init__(self, root):

        # Establecemos el tamaño de la raíz
        root.geometry("500x550+400+100")
        self.title = tk.Label(root, text="Analiza la Sintaxis de tu código")
        self.title.pack()

        self.txtArea=tk.Text(root,width=400 , height=20)
        self.txtArea.pack()


        self.frame = tk.LabelFrame(root,text="Selecciona el tipo de análisis")
        self.frame.pack( ipadx=30, ipady=10)


        self.lexerButton = tk.Button(self.frame, text="Léxico", fg="red",padx=40,command=self.analizarLexico)
        self.lexerButton.pack()

        self.sintButton = tk.Button(self.frame, text="Sintáctico", fg="red",padx=30,command=self.analizarSintactico)
        self.sintButton.pack()
        self.btnLimpiar = tk.Button(self.frame, text="Limpiar", fg="blue", padx=30, command=self.limpiar)
        self.btnLimpiar.pack()

    def limpiar(self):
        self.txtArea.delete("1.0","end")

    def analizarLexico(self):
        data = self.txtArea.get("1.0","end").split("\n")
        for linea in data:
            print(">>")
            print(analizar(linea))
            if len(linea) == 0:
                break


    def analizarSintactico(self):
        cont=leerCodigo(self.txtArea.get("1.0", "end"))
        print(cont)


# Creamos la aplicación, la ventana e iniciamos el bucle
win = tk.Tk()
#win.config(bg="gray")
win.title("Analizador Léxico-Sintáctico") #Cambiar el nombre de la ventana

window = Ventana(win)
win.mainloop()
