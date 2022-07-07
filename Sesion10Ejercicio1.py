import tkinter
from tkinter import ttk 
from tkinter import *
#Creamos y le damos formato a la ventana
window = tkinter.Tk()
window.geometry('250x250')

#Variable que contendrá la opción seleccionada
seleccionado = tkinter.StringVar()

#función para limpiar la variable
def limpiar():
	seleccionado.set ('Elija una opción')

#Creación de la lista de opciones
opc1 = ttk.Radiobutton(window, text='Opción 1', value='Seleccionó opción 1', variable=seleccionado)
opc2 = ttk.Radiobutton(window, text='Opción 2', value='Seleccionó opción 2', variable=seleccionado)
opc3 = ttk.Radiobutton(window, text='Opción 3', value='Seleccionó opción 3', variable=seleccionado)
opc1.grid(column=0, row=1, pady=10, padx=40)
opc2.grid(column=0, row=2, pady=10, padx=40)
opc3.grid(column=0, row=3, pady=10, padx=40)

#Muestra el contenido de la opción seleccionada
seleccion =ttk.Label(window, textvariable = seleccionado)
seleccion.grid(column=0, row=4, sticky='E',padx=20)

#Botón de reinicio de opciones
Button(window, text='Reiniciar',command=limpiar).grid(column=0,row=5, pady=10, padx=10)

window.mainloop()
