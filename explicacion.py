# importar todos los elementos de la libreria tkinter
from tkinter import *

# importar el elemento "pyplot" de la libreria  matplotlib,
# este elemento es el que nos permite generar graficas.
# En este caso tambien le damos la abreviacion "plt"
# solo para no tener que esribir todo el nombre de "matplotlib.pyplot" dentro
# de nuestro programa.
import matplotlib.pyplot as plt


# INICIO de la funcion "agregar_datos"
# Esta funcion se encarga de sacar el texto que el usuario
# nos dio dentro del programa.
# En nuestro programa esta funcion se llama cuando picamos el boton
# de "Agregar Datos". Que se encuentra en la linea 151.
def agregar_datos():
    # sacar el texto dentro de la Entrada "nombre_entrada"
    nombre_datos = nombre_entrada.get()
    # sacar el texto dentro de la Entrada "datos_entrada"
    datos = datos_entrada.get()

    # crear lista con los datos. El metodo .split() nos
    # sirve para separar cada dato por cada "," encontrada
    # e insertar el dato automaticamente dentro de la lista.
    datos = datos.split(',')

    datos_int = []  # Inicializamos otra lista para guardar
    # los mismos datos pero ahora convertidos
    # a tipo "int", osea tipo numeros.

    for dato in datos:  # ciclar sobre cada dato de la lista "datos" uno por uno
        # tomamos cada dato y lo convertimos a int con el metodo "int()"
        dato = int(dato)
        # agragamos el dato a la lista "datos_int" con el metodo .append()
        datos_int.append(dato)

    # Agregar a nuestro diccionario
    diccionario_de_datos[nombre_datos] = datos_int

    # Actualizar nuestro estado_label en la interfaz grafica.
    estado_label.configure(text='Datos "' + nombre_datos + '" agregados.')

    # Borrar el texto que se encuentran en nuestras 2 Entradas en la interfaz grafica.
    nombre_entrada.delete(0, END)
    datos_entrada.delete(0, END)
# FIN de la funcion agregar_datos



# INICIO  de la funcion generar_grafica
# funcion para generar grafica, esta seccion de codigo
# no va a correr hasta que nuestro programa lo "llame".
# En nuestro programa esta funcion se llama cuando picamos el boton
# de "Generar Grafica". Que se encuentra en la linea 127.
def generar_grafica():

    # sacar las claves y datos de nuestro diccionario uno por uno
    for nombre, datos in diccionario_de_datos.items():
        # plt.plot se encarga de agregar datos a la grafica
        # este metodo viene de matplotlib. Para que funcione le 
        # tenemos que dar 2 argumentos, una lista de datos y
        # un nombre.
        # Nosotros estamos sacando la lista de datos y el nombre desde nuestro diccionario
        # y pasandoselo a plt.plot.
        plt.plot(datos, label=nombre)
        # la estructura(por ejemplo) es asi:
        # plt.plot( [1, 1, 2, 3, 5, 8] , label="fibonacci")

    plt.legend() # aqui le decimos a matplotlib que cargue todos los nombres que le dimos en plt.plot()
    plt.show() # aqui le decimos a matplotlib que cargue y muestre todas las listas de datos que 
               # le dimos en plt.plot()

# FIN de la funcion "generar_grafica"


# INICIO funcion reiniciar_datos
def reiniciar_datos():
    global diccionario_de_datos # tomar el diccionario de datos de nuestro programa
    diccionario_de_datos = {} # nuesto diccionario_de_datos ahora es un diccionario vacio
    estado_label.configure(text='Se han reiniciado todos los datos.') # Actualizar estado_label
# FIN funcion reiniciar_datos

# **COMIENZO DEL PROGRAMA**

diccionario_de_datos = {} # inicializar un diccionario vacio

# poner colores en variables para no tener que escribirlos
# cada vez que los queramos usar
color1 = 'lemon chiffon' 
color2 = 'goldenrod4'


tk = Tk() # inicializar Tkinter
tk.geometry('520x670') # dimensiones de la ventana
tk.wm_title('Graficador Sencillo de Datos') # titulo de la ventana
tk.configure(bg=color1) # configurar color principal de la ventana


# Primer LABEL con el titulo
titulo_programa = Label(tk, text='Graficador Sencillo')
titulo_programa.configure(font=('Arial', 42), bg=color1, fg=color2)
titulo_programa.grid(row=0, column=0, padx=20, pady=20)

# Segundo LABEL con el texto "Nombre de los datos"
nombre_label = Label(tk, text='Nombre de los datos:')
nombre_label.configure(bg=color1, font=('Arial', 20))
nombre_label.grid(row=1, column=0)

# Primer ENTRADA/Entry de texto para que nos den el nombre de los datos
nombre_entrada = Entry(tk)
nombre_entrada.configure(font=('Arial', 20), fg='dark green')
nombre_entrada.grid(row=2, column=0, padx=10, sticky='ew')


# Tercer LABEL con el texto "Datos separados por comas:"
datos_label = Label(tk, text='Datos separados por comas:')
datos_label.configure(bg=color1, font=('Arial', 20))
datos_label.grid(row=3, column=0)

# Segunda ENTRADA  de datos, donde nos deben de poner numeros separados por comas
datos_entrada = Entry(tk)
datos_entrada.configure(font=('Arial', 20), fg='blue')
datos_entrada.grid(row=4, column=0, padx=10, sticky='ew')


# PRIMER BOTON
# Aqui vemos la palabra "command" que se refiera a que funcion debemos de llamar
# cuando se pique este boton.
# En este caso cuando piquemos este boton nuestro programa va a 
# correr la funcion agregar_datos
boton_agregar = Button(tk, text='Agregar datos', command=agregar_datos)
boton_agregar.configure(font=('Arial', 20), bg='goldenrod')
boton_agregar.grid(row=5, column=0, sticky='ew', pady=(10, 100))


# Cuarto LABEL con el texto "Estado:"
estado_titulo_label = Label(tk, text='Estado:')
estado_titulo_label.configure(bg=color1, font=('Arial', 20), fg='lime green')
estado_titulo_label.grid(row=6, column=0)

# Quinto LABEL con el texto "Sin datos agregados..."
# este es el LABEL que se actualiza cuando llamamos
# la funcion agregar_datos o reiniciar_datos como se muestra en 
# la linea 44 y 81
estado_label = Label(tk, text='Sin datos agregados...')
estado_label.configure(bg=color1, font=('Arial', 14), fg='navy')
estado_label.grid(row=7, column=0)


# SEGUNDO BOTON
# Este boton le llama a nuesta funcion "generar_grafica" cuando le picamos.
boton_graficar = Button(tk, text='Generar grafica', command=generar_grafica)
boton_graficar.configure(font=('Arial', 20), bg='medium sea green')
boton_graficar.grid(row=8, column=0, sticky='ew', pady=(100, 0))


# TERCER BOTON
# Este boton le llama a nuestra funcion "reiniciar_datos"
boton_reiniciar = Button(
    tk, text='Reiniciar todos los datos', command=reiniciar_datos)
boton_reiniciar.configure(font=('Arial', 20), bg='red3')
boton_reiniciar.grid(row=9, column=0, sticky='ew', pady=(0, 30))

# Este codigo va al final de todos los programas que utlizan tkinter
# sirve para que comienze a correr.
tk.mainloop()
