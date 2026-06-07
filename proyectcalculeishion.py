#Importamos las librerias necesarias
import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
import sympy as sp

#creamos la ventana principal y su aspecto en general (dependiendo del tema del computador, 
#es decir si esta en modo claro o modo oscuro)
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
programa_calculo = ctk.CTk()
programa_calculo.title("EID-CALCULO-LIMITES")
programa_calculo.geometry("1080x720")




#_____________________________________creación de las funciones del programa______________________________________________
#función limpiar texto
def limpiar():
    ingresar_datos.delete("1.0", "end")
    ingresar_tendencia.delete("1.0", "end")

#funcion coseno
def coseno():
    ingresar_datos.insert("end","cos(x)") 

#funcion seno
def seno():
    ingresar_datos.insert("end","sen(x)")

#funcion tangente
def tangente():
    ingresar_datos.insert("end","tan(x)")

def calcular():
    print("NO TOI NI AHI CON EL LIMITE")


#______________________________________creación de "contenedores" para ingresar datos______________________________________
#crear el "contenedor dónde se escriben los datos"
ingresar_datos = ctk.CTkTextbox(programa_calculo, width=200, height=30)
ingresar_datos.place(relx=0.01, rely=0.18)

#crear el "contenedor al número que tiende x"
ingresar_tendencia = ctk.CTkTextbox(programa_calculo, width=200, height=30)
ingresar_tendencia.place(relx=0.01, rely=0.32)

#______________________________________instrucciones de los "contenedores"_________________________________________________
efe_de_x = ctk.CTkLabel(programa_calculo, text="ingrese la funcion de su limite", font=("Calibri", 16))
efe_de_x.place(relx=0.01, rely=0.12)

tendencia_x = ctk.CTkLabel(programa_calculo, text="ingrese la tendencia a 'x'", font=("Calibri", 16))
tendencia_x.place(relx=0.01, rely=0.26)

funciones_rapidas = ctk.CTkLabel(programa_calculo, text="funciones rapidas", font=("Calibri", 16))
funciones_rapidas.place(relx=0.01, rely=0.40)

#_______________________________________creación de botones del programa___________________________________________________
#crear botón coseno
cos_button = ctk.CTkButton(master=programa_calculo, text="cos(x)", command=coseno)
cos_button.place(relx=0.01, rely=0.46)

#crear botón seno
sen_button = ctk.CTkButton(master=programa_calculo, text="sen(x)", command=seno)
sen_button.place(relx=0.15, rely=0.46)

#crear botón tangente
tan_button = ctk.CTkButton(master=programa_calculo, text="tan(x)", command=tangente)
tan_button.place(relx=0.01, rely=0.54)

#crear botón para limpiar los datos
limpiar_button = ctk.CTkButton(master=programa_calculo, text="Limpiar", command=limpiar)
limpiar_button.place(relx=0.15, rely=0.54)


# --- BOTÓN PARA ACCIÓN DE CÁLCULO ---
#crear botón para calcular
calcular_button = ctk.CTkButton(master=programa_calculo, text="Calcular el limite", command=calcular)
calcular_button.place(relx=0.01, rely=0.68)


#para que no se cierre el programa
programa_calculo.mainloop()
