#importamos las librerias necesarias
import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
import sympy as sp

#creamos la ventana principal
programa_calculo = ctk.CTk()    
programa_calculo.title("EID-CALCULO-LIMITES")
programa_calculo.geometry("1080x720")
