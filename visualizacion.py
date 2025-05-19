# Librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Seaborn para visualizaciones más estilizadas
import seaborn as sns
import os
from analisis import DataAnalyzer
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox , simpledialog , filedialog
from PIL import ImageTk

data = pd.read_csv("adult.csv")
analizar = DataAnalyzer(data)


def informacion():
    try:
        info = analizar.summary()
        text_area.insert(tk.END , info)
    except:
        messagebox.showerror("Error" , "No se puede")

def mostrar_imagenes(pill_img):
    image_tk = ImageTk.PhotoImage(pill_img)
    image_label.configure(image = image_tk)
    image_label.image = image_tk
    
def mostrar_correlacion():
    img = analizar.correlation_matrix()
    mostrar_imagenes(img)
    
def mostrar_categorico():
    cols = analizar.df.select_dtypes(include= 'object').columns.tolist()
    if not cols:
        messagebox.showwarning("Atencion" , "El df no tiene col. categoricas")
    else:
        sel = simpledialog.askstring("Columna" , f"Elige una: \n{cols}")
        if sel in cols:
            img = analizar.categorical_analisis_col(sel)
            mostrar_imagenes(img)

    
ventana = tk.Tk()
ventana.title("Análisis de datos")

boton_summary = tk.Button(ventana , text = "Estadisticas" , command = informacion)
boton_summary.grid(row=0 , column=0)

boton_numerico = tk.Button(ventana , text = "Analisis Númerico" , command = mostrar_correlacion)
boton_numerico.grid(row=0 , column=1)

boton_categorico = tk.Button(ventana , text = "Analisis Categórico" , command = mostrar_categorico)
boton_categorico.grid(row=0 , column=2)

text_area = ScrolledText(ventana , width = 70 , height = 30)
text_area.grid(row=1 , column=1)



content_frame = tk.Frame(ventana)
content_frame.grid(row=1 , column =2 )
image_label = tk.Label(content_frame , text = "Resultado")
image_label.grid(row=0 , column=0 )
ventana.mainloop()
