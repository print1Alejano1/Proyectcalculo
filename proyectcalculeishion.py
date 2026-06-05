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
