import tkinter as tk
from semantico import traductor, traductor2


def interfazTraductor(texto):

    ventanaTraductor = tk.Tk()
    ventanaTraductor.title("Traductor")
    ventanaTraductor.geometry("770x600")
    ventanaTraductor.config(background="#D5E6DD")
    ventanaTraductor.resizable(0, 0)

    listas = traductor(texto)
    listas2 = traductor2(texto)

    print('\n', listas, '\n')
    print(listas2)

    palabra1 = listas[0] + ' ' + listas[1] + ' () ' + ' : '
    palabra2 = listas[2] + '  ' + listas[3]
    palabra3 = listas[4] + '  ' + listas[5] + '   ' + listas[6]
    palabra4 = listas[7] + '  ( ' + listas[8] + listas[9] + ' '+listas[10] + ') '
    palabra5 = listas[11] + ' ' + listas[12]

    palabra6 = listas2[0] + '  ' + listas2[1] + ' ' + listas2[2]
    palabra7 = listas2[3]
    palabra8 = listas2[4]
    palabra9 = listas2[5] +' ' + listas2[8] +' ' + '=' + listas2[10]
    palabra10 = listas2[11] + listas2[12] + listas2[13] + listas2[14] + listas2[15]
    palabra11 =listas2[16] + ' ' + listas2[17]
    palabra12 = listas2[18]
    

    labelTitulo = tk.Label(ventanaTraductor, text="Traductor Python", width=50, height=2,background="#4C5CA6", foreground="#FCF9F9", font=("Tahoma", 22,)).place(x=0, y=15)
    cuadro2 = tk.Label(ventanaTraductor, background="#F2F3F4",highlightbackground="#4C5CA6",highlightthickness=1, bd=0).place(x=60, y=129, width=640, height=460)
    labelReservada = tk.Label(ventanaTraductor, background="#F2F3F4", text=palabra1, font=("Arial", 13)).place(x=80, y=160, width=200)
    labelReservada = tk.Label(ventanaTraductor, background="#F2F3F4", text=palabra3, font=("Arial", 13)).place(x=110, y=195, width=200)
    labelReservada = tk.Label(ventanaTraductor, background="#F2F3F4", text=palabra4, font=("Arial", 13)).place(x=110, y=225, width=250)
    labelReservada = tk.Label(ventanaTraductor, background="#F2F3F4", text=palabra5, font=("Arial", 13)).place(x=110, y=250, width=200)

    label5 = tk.Label(ventanaTraductor, background="white", text='----------------', font=('Arial',13)).place(x=200, y=300)

    label5 = tk.Label(ventanaTraductor, background="white", text=palabra6, font=('Arial',13)).place(x=200, y=340)
    label6 = tk.Label(ventanaTraductor, background='white', text=palabra7, font=('Arial',13)).place(x=200, y=380)
    label7 = tk.Label(ventanaTraductor, background='white', text=palabra8, font=('Arial',13)).place(x=200, y=400)
    label8 = tk.Label(ventanaTraductor, background='white', text=palabra9, font=('Arial',13)).place(x=200, y=440)
    label9 = tk.Label(ventanaTraductor, background="white", text=palabra10, font=('Arial',13)).place(x=200, y=480)
    label10 = tk.Label(ventanaTraductor, background='white', text=palabra11, font=('Arial',13)).place(x=200, y=500)
    label11 = tk.Label(ventanaTraductor, background='white', text=palabra12, font=('Arial',13)).place(x=200, y=540)
    
    ventanaTraductor.mainloop()
