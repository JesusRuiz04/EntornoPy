import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Calculadora Avanzada")
ventana.geometry("400x500")

# Crear el campo de entrada
entrada = ttk.Entry(ventana, font=("Arial", 16), justify="right", width=20)
entrada.grid(column=0, row=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Función para agregar caracteres
def agregar_caracter(caracter):
    entrada.insert(tk.END, caracter)

# Función para limpiar
def limpiar():
    entrada.delete(0, tk.END)

# Función para calcular
def calcular():
    try:
        expresion = entrada.get()
        if expresion:
            resultado = eval(expresion)
            entrada.delete(0, tk.END)
            entrada.insert(0, str(resultado))
    except Exception:
        messagebox.showerror("Error", "Expresión inválida")
        entrada.delete(0, tk.END)

# Lista de botones: (texto, fila, columna, comando)
botones = [
    ('C', 1, 0, limpiar),
    ('/', 1, 1, lambda: agregar_caracter('/')),
    ('*', 1, 2, lambda: agregar_caracter('*')),
    ('-', 1, 3, lambda: agregar_caracter('-')),
    
    ('7', 2, 0, lambda: agregar_caracter('7')),
    ('8', 2, 1, lambda: agregar_caracter('8')),
    ('9', 2, 2, lambda: agregar_caracter('9')),
    ('+', 2, 3, lambda: agregar_caracter('+')),
    
    ('4', 3, 0, lambda: agregar_caracter('4')),
    ('5', 3, 1, lambda: agregar_caracter('5')),
    ('6', 3, 2, lambda: agregar_caracter('6')),
    ('=', 3, 3, calcular),
    
    ('1', 4, 0, lambda: agregar_caracter('1')),
    ('2', 4, 1, lambda: agregar_caracter('2')),
    ('3', 4, 2, lambda: agregar_caracter('3')),
    
    ('0', 5, 0, lambda: agregar_caracter('0')),
    ('.', 5, 1, lambda: agregar_caracter('.')),
]

# Crear todos los botones usando un bucle
for (texto, fila, columna, comando) in botones:
    if texto == '=':
        # Botón = más alto
        boton = ttk.Button(ventana, text=texto, command=comando, width=8)
        boton.grid(column=columna, row=fila, rowspan=2, padx=2, pady=2, sticky="nsew")
    elif texto == '0':
        # Botón 0 más ancho
        boton = ttk.Button(ventana, text=texto, command=comando, width=8)
        boton.grid(column=columna, row=fila, columnspan=2, padx=2, pady=2, sticky="ew")
    else:
        boton = ttk.Button(ventana, text=texto, command=comando, width=8)
        boton.grid(column=columna, row=fila, padx=2, pady=2, sticky="nsew")

# Configurar redimensionamiento
for i in range(4):
    ventana.grid_columnconfigure(i, weight=1)
for i in range(6):
    ventana.grid_rowconfigure(i, weight=1)

ventana.mainloop()