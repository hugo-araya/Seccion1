from tkinter import *

def funcion1():
    print('consola')

if __name__== '__main__' :
    ventana = Tk()
    ventana.geometry('200x200+100+100')
    boton = Button(ventana, text='Boton 1', command = funcion1)
    boton.grid(column=0, row=0)
    ventana.mainloop()

