#importamos las librerias necesarias
import customtkinter as ctk #aqui tambien estamos dejando abreviado a ctk, y eso vamos a suar cuando queramos usar algo con el custom 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
import sympy as sp

#creamos la ventana principal
ctk.set_appearance_mode("System") #aqui nos saldra del color del modo k este el equipo, claro, oscuro
ctk.set_default_color_theme("blue") #y usamos 


programa_calculo = ctk.CTk()    
programa_calculo.title("EID-CALCULO-LIMITES")
programa_calculo.geometry("1080x720")

#crear la funcion que sera llamada cuando el bton se llegue a presionar
def calculowe():
    print("el ingeniero aun esta cocinando esperen")


#crear el boton, 
button = ctk.CTkButton(master=programa_calculo, text="Calcular", command=calculowe)
button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)



#para que no se cierre el programa
programa_calculo.mainloop()
