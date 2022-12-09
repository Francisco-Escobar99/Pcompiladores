import tkinter as tk
from lexico2 import lexico as lex
from sintactico import sintaxis as sin
from interfazTraductor import interfazTraductor

class interfaz():
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Compiladores e Interpretes")
        self.ventana.geometry("1000x700")
        self.ventana.config(background="#D5E6DD")
        self.ventana.resizable(0,0)
        
        self.labelTitulo=tk.Label(self.ventana, text="Analizador de pseudocodigo", width=68, height=2, background="#4C5CA6" ,foreground="#FCF9F9", font=("Tahoma", 22,)).place(x=0,y=45)
        self.labelSubTitulo=tk.Label(self.ventana, text="Pseudocodigo a evaluar:", background="#D5E6DD", foreground="#596186", font=("Arial", 17)).place(x=125,y=171)

        self.CajaTexto=tk.Text(self.ventana, highlightbackground="#4C5CA6", foreground="#596186", highlightthickness = 1, bd=0, font=("Arial", 12))
        self.CajaTexto.place(x=60,y=219,width=375, height=386)


        
        self.cuadro2=tk.Label(self.ventana, background="#FFFFFF", highlightbackground="#4C5CA6",highlightthickness =1, bd=0).place(x=460,y=219, width=469, height=386)
        self.labelTituloMetodo=tk.Label(self.ventana, text="Token", width=64, height=1,  background="#4C5CA6", foreground="#FCF9F9", font=("Arial", 14)).place(x=460,y=219, width=469)
        self.labelError=tk.Label(self.ventana, text="Error", width=64, height=1,  background="#4C5CA6", foreground="#FCF9F9", font=("Arial", 14,)).place(x=460,y=495, width=469)
        self.labelReservada=tk.Label(self.ventana, background="#FFFFFF",text="Palabras Reservadas:", font=("Arial", 14)).place(x=473,y=250, width=190)
        self.labelDelimitadores=tk.Label(self.ventana, background="#FFFFFF",text="Delimitadores:", font=("Arial", 14)).place(x=469,y=300, width=140)
        self.labelParentesis=tk.Label(self.ventana, background="#FFFFFF",text="Operadores:", font=("Arial", 14)).place(x=477,y=350, width=100)
        self.labelPalabras=tk.Label(self.ventana, background="#FFFFFF",text="Variables:", font=("Arial", 14)).place(x=470,y=400, width=100)
        self.labelEntero=tk.Label(self.ventana, background="#FFFFFF",text="Digitos:", font=("Arial", 14)).place(x=475,y=450, width=80)
        self.btnAnalizar=tk.Button(self.ventana, text="Analizar y Tradurcir",  background="#4C5CA6", foreground="#FCF9F9", font=("Arial", 14,),command= lambda:self.ResultadoLexico(self.CajaTexto.get('1.0','end')))
        self.btnAnalizar.place(x=460,y=615, width=190, height=35)
        self.ventana.mainloop()

    def ResultadoLexico(self, texto_Codigo):

        n_Texto, p_Reservadas, tt_Reservadas = lex.busqueda_Reservadas(texto_Codigo)
        n_Texto2, p_Delimitadores, tt_Delimitadores = lex.busqueda_Delimitadores(n_Texto)
        n_Texto3, p_Operadores, tt_Operadores = lex.busqueda_Operadores(n_Texto2)
        n_Texto4, p_Variables, tt_Variables = lex.busqueda_Variables(n_Texto3)
        n_Texto5, p_Digitos, tt_Digitos = lex.busqueda_Decimales(n_Texto4)
        n_Texto6, p_Digitos2, tt_Digitos2 = lex.busqueda_Enteros(n_Texto5)
        tt_Errores, p_Errores = lex.busqueda_Errores(n_Texto6)

        suma_Digitos = tt_Digitos + tt_Digitos2

        print('----------------')
        print('Reservadas: ', tt_Reservadas ,' = ', p_Reservadas)
        print('Delimitador: ', tt_Delimitadores, ' = ' , p_Delimitadores)
        print('Operadores: ', tt_Operadores, ' =  ', p_Operadores)
        print('Variables: ', tt_Variables, '= ', p_Variables)
        print('Digitos: ', suma_Digitos, ' = ', p_Digitos + p_Digitos2)
        print('Errores: ', tt_Errores, ' = ', p_Errores)
        print('----------------')

        tk.Label(self.ventana, background="#FFFFFF",text= tt_Reservadas, font=("Arial", 13)).place(x=662,y=253)
        tk.Label(self.ventana, background="#FFFFFF",text= tt_Delimitadores, font=("Arial", 13)).place(x=600,y=303)
        tk.Label(self.ventana, background="#FFFFFF",text=tt_Operadores, font=("Arial", 13)).place(x=578,y=353)
        tk.Label(self.ventana, background="#FFFFFF",text=tt_Variables, font=("Arial", 13)).place(x=560,y=403)
        tk.Label(self.ventana, background="#FFFFFF",text=suma_Digitos, font=("Arial", 13)).place(x=554,y=453)

        opcion = sin(texto_Codigo)
        print(opcion)

        if opcion == True:
            print('Son Errores')
        else:
            interfazTraductor(texto_Codigo)

        # tk.Label(self.ventana, background="#FFFFFF",text=tablaReservadas, font=("Arial", 13)).place(x=675,y=253)
        # tk.Label(self.ventana, background="#FFFFFF",text=delimitador, font=("Arial", 13)).place(x=615,y=303)
        # tk.Label(self.ventana, background="#FFFFFF",text=parentesis, font=("Arial", 13)).place(x=598,y=353)
        # tk.Label(self.ventana, background="#FFFFFF",text=Variables, font=("Arial", 13)).place(x=576,y=403)
        # tk.Label(self.ventana, background="#FFFFFF",text=Digitos, font=("Arial", 13)).place(x=576,y=453)
        tk.Label(self.ventana, background="#FFFFFF",text= p_Errores, font=("Arial", 13)).place(x=526,y=543)
    
VentanaPrincipal = interfaz()