#**Ejercicio 2:** Crear una calculadora básica empleando una interfaz con botones para los números (0-9), las operaciones (+, -, *, /), y un botón de igual (=) para calcular el resultado. Conforme se van presionando botones, vamos escribiendo una expresión en un widget de tipo Entry (capturamos lo que había, lo borramos y volvemos a escribir la expresión añadiendo lo nuevo). No obstante, si el botón presionado es `=` entonces habrá que evaluar la expresión del Entry (`eval(entry.get())`... que podría arrojar excepciones), después borramos lo escrito y escribimos el resultado (o un mensaje de error si se produjo). Opcionalmente, podríamos desplegar los botones en el Frame empleando una lista de tuplas (con todos los botones) y recorriéndola con un bucle.

import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("400x500")

# Crear el campo de entrada para mostrar los números y operaciones
entrada = ttk.Entry(ventana, font=("Arial", 16), justify="right", width=20)
entrada.grid(column=0, row=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Función para agregar números y operadores
def agregar_caracter(caracter):
    entrada.insert(tk.END, caracter)

# Función para limpiar la entrada
def limpiar():
    entrada.delete(0, tk.END)

# Función para calcular el resultado
def calcular():
    try:
        expresion = entrada.get()
        if expresion:
            resultado = eval(expresion)
            entrada.delete(0, tk.END)
            entrada.insert(0, str(resultado))
    except Exception as e:
        messagebox.showerror("Error", "Expresión inválida")
        entrada.delete(0, tk.END)

# Crear los botones usando un bucle (más eficiente)
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

# Crear todos los botones usando el bucle
for (texto, fila, columna, comando) in botones:
    if texto == '=' :
        # Hacer que el botón = sea más alto
        boton = ttk.Button(ventana, text=texto, command=comando, width=10)
        boton.grid(column=columna, row=fila, rowspan=2, padx=2, pady=2, sticky="nsew")
    elif texto == '0':
        # Hacer que el botón 0 sea más ancho
        boton = ttk.Button(ventana, text=texto, command=comando, width=10)
        boton.grid(column=columna, row=fila, columnspan=2, padx=2, pady=2, sticky="ew")
    else:
        boton = ttk.Button(ventana, text=texto, command=comando, width=10)
        boton.grid(column=columna, row=fila, padx=2, pady=2, sticky="nsew")

# Configurar el redimensionamiento de columnas y filas
for i in range(4):
    ventana.grid_columnconfigure(i, weight=1)
for i in range(6):
    ventana.grid_rowconfigure(i, weight=1)

ventana.mainloop()
