import tkinter as tk
import tkcalendar
from datetime import timedelta
from tkinter import ttk
import pandas as pd
class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()

        self.frame_principal=ttk.Frame(self)
        self.boton_ejecutar=ttk.Button(self.frame_principal,text="Ejecutar",command=self.obtener_ejecutar
)
        self.boton_salir=ttk.Button(self.frame_principal,text="Salir",command=self.salir_click)
        self.label_ejecutar=ttk.Label(self.frame_principal,text="FechaInicial")
        self.label_ejecutar2=ttk.Label(self.frame_principal,text="FechaFinal")

        #empaquetar todo
        self.frame_principal.pack(fill=tk.BOTH,expand=True)
        self.boton_ejecutar.pack()

        self.boton_salir.pack()
        self.label_ejecutar.pack()
        self.label_ejecutar2.pack()

    def salir_click(self):
        self.destroy()

    def obtener_ejecutar(self):
        IngresoUsuario=UserInput()
        global Ruta
        global fechaInicialUsuario
        global fechaFinalUsuario
        fechaInicialUsuario=IngresoUsuario.fechita1
        fechaFinalUsuario=IngresoUsuario.fechita2
        self.label_ejecutar.configure(text=pd.to_datetime(fechaInicialUsuario))
        self.label_ejecutar2.configure(text=pd.to_datetime(fechaFinalUsuario))#Coge de la ventana UserInput la variable usuario

        Ruta="1.xlsx"
        operacion()
        imprimir_valor()

class UserInput(tk.Toplevel,list): #SELF HACE REFERENCIA A LA VENTANA TOP LEVEL
    def __init__(self):
        super().__init__()
        self.usuario=None #inicializa el usuario con anda
        self.fechita1=None
        self.fechita2=None
        self.frame_secundario=ttk.Frame(self)
        #self.entrada_usuario=ttk.Entry(self.frame_secundario)
        self.boton_guardar=ttk.Button(self.frame_secundario,text="Guardar",command=lambda: self.date_range())
        self.fecha1=tkcalendar.DateEntry(self.frame_secundario)
        self.fecha2=tkcalendar.DateEntry(self.frame_secundario)


        self.frame_secundario.pack(fill=tk.BOTH,expand=True)
        #self.entrada_usuario.pack()
        self.boton_guardar.pack()
        self.fecha1.pack()
        self.fecha2.pack()
        self.transient(self.master)
        self.grab_set()
        self.wait_window(self)
    def guardar_valor(self):
        #self.usuario=self.entrada_usuario.get()
        self.destroy()

    def date_range(self):
        self.fechita1=self.fecha1.get_date()
        self.fechita2=self.fecha2.get_date()
        self.destroy()


if __name__=="__main__":
    ventana_principal=MainWindow()
    def operacion():
        Datos= pd.read_excel(Ruta)
    # loop over the list of csv files
    # for f in RutaExcel:
    #     try:
    #         Datos = pd.read_excel(f,usecols="A:G,J:L,R")
    #     except:
    #         print("Obtencion de datos fallida")
        Datos.to_excel("Resultado.xlsx")
    def imprimir_valor():
        print(Ruta)
        print(fechaInicialUsuario)
        print(fechaFinalUsuario)
    ventana_principal.mainloop()

