import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cambio de Color")
ventana.geometry("300x200")

indice_color = 0

# Función que se ejecuta cuando el botón es presionado
def cambio_color():
    global indice_color
    colores = ["red", "blue", "green"]
    ventana.config(bg=colores[indice_color]) 
    indice_color += 1
    if indice_color >= len(colores):
        indice_color = 0

# Crear un botón
boton = ttk.Button(ventana, text="Cambiar Color", command=cambio_color)
boton.pack(pady=20)  # Empaquetamos el botón en la ventana

ventana.mainloop()