import tkinter as tk
import sys
from  Analizador_Lexico.lexerMain  import *
from AnalizadorSintactico.sintactico_yacc import *
tokenList=[]
class Ventana:
    def __init__(self, root):

        root.geometry("500x500+400+100")
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
        self.btnActualizar = tk.Button(self.frame, text="Resultados Lexicos", fg="blue", padx=30, command=self.actualizar)
        self.btnActualizar.pack()
        self.btnSintactico = tk.Button(self.frame, text="Resultados Sintacticos", fg="blue", padx=30,command=self.sintacticosR)
        self.btnSintactico.pack()

    def sintacticosR(self):
        extra_window2 = tk.Toplevel(self.frame)
        extra_window2.geometry("300x500")
        label = tk.Label(extra_window2, text="""Resultados arrojados""")
        label.pack()
        archivo2 = open("sintactico.txt", "r")
        bop2 = tk.Label(extra_window2)
        bop2.pack()
        for linea in archivo2.readlines():
            tv = format(linea)
            b = tk.Label(bop2, text=tv)
            b.pack()
        archivo2.close()
        archivo = open("reglas.txt", "r")
        bop = tk.Label(extra_window2)
        bop.pack()

        for linea in archivo.readlines():
            tv = format(linea)
            b = tk.Label(bop, text=tv)
            b.pack()
            print(linea)
        archivo.close()

    def actualizar(self):
        extra_window = tk.Toplevel(self.frame)
        extra_window.geometry("500x500")

        archivo = open("lexico.txt", "r")
        bop = tk.Listbox(extra_window)
        bop.pack()
        label2 = tk.Label(bop, text="""Resultados arrojados""")
        label2.pack()
        scrollbar = tk.Scrollbar(extra_window)
        scrollbar.pack(side='right', fill='y')

        listbox = tk.Listbox(extra_window,width=80, height=20, yscrollcommand=scrollbar.set)
        for linea in archivo.readlines():
            listbox.insert("end",str(linea))
            print(linea)
        archivo.close()
        listbox.pack(side="left", fill="both")
        scrollbar.config(command=listbox.yview)




    def limpiar(self):
        self.txtArea.delete("1.0","end")


    def analizarLexico(self):
        crearArchivo(self.txtArea.get("1.0", "end"))
        data = self.txtArea.get("1.0","end").split("\n")
        for linea in data:
            print(">>")
            print(analizar(linea))
            if len(linea) == 0:
                break

    def analizarSintactico(self):
        crearArchivoSintactico(self.txtArea.get("1.0", "end"))
        reglas()
        cont = leerCodigo(self.txtArea.get("1.0", "end"))
        #print(cont)

# Creamos la aplicación, la ventana e iniciamos el bucle
win = tk.Tk()
win.title("Analizador Léxico-Sintáctico") #Cambiar el nombre de la ventana


window = Ventana(win)
win.mainloop()

