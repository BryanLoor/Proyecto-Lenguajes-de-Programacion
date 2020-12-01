import tkinter as tk
from  Analizador_Lexico.lexerMain  import analizar
from AnalizadorSintactico.sintactico_yacc import leerCodigo

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
        self.btnActualizar = tk.Button(self.frame, text="Actualizar Resultados", fg="blue", padx=30, command=self.actualizar)
        self.btnActualizar.pack()


    def actualizar(self):
        self.extra_window =tk.Toplevel(self.frame)
        self.extra_window.geometry("500x500+400+100")
        label2 = tk.Label(self.extra_window, text="""Resultados arrojados""")
        label2.grid(row=0,column=0,ipadx=30, ipady=10)
        resultados= tk.LabelFrame(self.extra_window,text="Tokens reconocidos")
        resultados.grid(row=1,column=0,ipadx=50, ipady=20)

        scrollbar = tk.Scrollbar(resultados)
        scrollbar.grid(row=2,column=0,ipadx=150, ipady=10, columnspan=3)

        mylist = tk.Listbox(resultados, yscrollcommand=scrollbar.set)

        for val in tokenList:
            for tok in val:
                mylist.insert(tk.END, "Token:   " + tok.value+"Regla:   "+tok.type)
        mylist.grid(row=2,column=2,ipadx=150, ipady=20, sticky='e')
        scrollbar.config(command=mylist.yview)



    def limpiar(self):
        self.txtArea.delete("1.0","end")
        tokenList.clear()

    def analizarLexico(self):
        data = self.txtArea.get("1.0","end").split("\n")
        for linea in data:
            tokens= analizar(linea)
            tokenList.append(tokens)
            if len(linea) == 0:
                break

    def analizarSintactico(self):
        cont = leerCodigo(self.txtArea.get("1.0", "end"))
        print(cont)

# Creamos la aplicación, la ventana e iniciamos el bucle
win = tk.Tk()
win.title("Analizador Léxico-Sintáctico") #Cambiar el nombre de la ventana


window = Ventana(win)
win.mainloop()
