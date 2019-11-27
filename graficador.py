from tkinter import *
import matplotlib.pyplot as plt


def generar_grafica():
    for llave, valor in diccionario_de_datos.items():
        plt.plot(valor, label=llave)

    plt.legend()
    plt.show()


def agregar_datos():
    nombre_datos = nombre_entrada.get()
    datos = datos_entrada.get()

    # crear lista con los datos
    datos = datos.split(',')

    if datos[-1] == '':
        del datos[-1]

    datos_int = []
    for dato in datos:
        dato = int(dato)
        datos_int.append(dato)

    diccionario_de_datos[nombre_datos] = datos_int

    estado_label.configure(text='Datos "' + nombre_datos + '" agregados.')
    nombre_entrada.delete(0, END)
    datos_entrada.delete(0, END)


def reiniciar_datos():
    global diccionario_de_datos
    diccionario_de_datos = {}
    estado_label.configure(text='Se han reiniciado todos los datos.')


diccionario_de_datos = {}

color1 = 'lemon chiffon'
color2 = 'goldenrod4'


tk = Tk()
tk.geometry('520x670')
tk.wm_title('Graficador Sencillo de Datos')
tk.configure(bg=color1)

titulo_programa = Label(tk, text='Graficador Sencillo')
titulo_programa.configure(font=('Arial', 42), bg=color1, fg=color2)
titulo_programa.grid(row=0, column=0, padx=20, pady=20)

nombre_label = Label(tk, text='Nombre de los datos:')
nombre_label.configure(bg=color1, font=('Arial', 20))
nombre_label.grid(row=1, column=0)

nombre_entrada = Entry(tk)
nombre_entrada.configure(font=('Arial', 20), fg='dark green')
nombre_entrada.grid(row=2, column=0, padx=10,sticky='ew')

datos_label = Label(tk, text='Datos separados por comas:')
datos_label.configure(bg=color1, font=('Arial', 20))
datos_label.grid(row=3, column=0)

datos_entrada = Entry(tk)
datos_entrada.configure(font=('Arial', 20), fg='blue')
datos_entrada.grid(row=4, column=0, padx=10,sticky='ew')

boton_agregar = Button(tk, text='Agregar datos', command=agregar_datos)
boton_agregar.configure(font=('Arial', 20), bg='goldenrod')
boton_agregar.grid(row=5, column=0, sticky='ew', pady=(10,100))

estado_titulo_label = Label(tk, text='Estado:')
estado_titulo_label.configure(bg=color1, font=('Arial', 20), fg='lime green')
estado_titulo_label.grid(row=6, column=0)

estado_label = Label(tk, text='Sin datos agregados...')
estado_label.configure(bg=color1, font=('Arial', 14), fg='navy')
estado_label.grid(row=7, column=0)

boton_graficar = Button(tk, text='Generar grafica', command=generar_grafica)
boton_graficar.configure(font=('Arial', 20), bg='medium sea green')
boton_graficar.grid(row=8, column=0, sticky='ew', pady=(100,0))

boton_reiniciar = Button(tk, text='Reiniciar todos los datos', command=reiniciar_datos)
boton_reiniciar.configure(font=('Arial', 20), bg='red3')
boton_reiniciar.grid(row=9, column=0, sticky='ew', pady=(0,30))

tk.mainloop()
