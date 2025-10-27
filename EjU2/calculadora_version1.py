import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("600x400")

# Crear la entrada primero
entrada = ttk.Entry(ventana, font=("Arial", 14), width=20)
entrada.grid(column=1, row=0, columnspan=3, padx=5, pady=5)

# Función que recibe el texto del botón como parámetro
def obtener_texto(caracter):
    if caracter == "=":
        # Calcular el resultado
        try:
            expresion = entrada.get()
            if expresion:
                resultado = eval(expresion)
                entrada.delete(0, tk.END)
                entrada.insert(0, str(resultado))
        except Exception:
            messagebox.showerror("Error", "Expresión inválida")
            entrada.delete(0, tk.END)
    elif caracter == "C":
        # Limpiar
        entrada.delete(0, tk.END)
    else:
        # Agregar el caracter
        entrada.insert(tk.END, caracter)

# Botón para limpiar
botonClear = ttk.Button(ventana, text="C", command=lambda: obtener_texto("C"))
botonClear.grid(column=1, row=1)

# Botones numéricos
boton0 = ttk.Button(ventana, text="0", command=lambda: obtener_texto("0"))
boton0.grid(column=1, row=3)

boton1 = ttk.Button(ventana, text="1", command=lambda: obtener_texto("1"))
boton1.grid(column=2, row=3)

boton2 = ttk.Button(ventana, text="2", command=lambda: obtener_texto("2"))
boton2.grid(column=3, row=3)

boton3 = ttk.Button(ventana, text="3", command=lambda: obtener_texto("3"))
boton3.grid(column=1, row=4)

boton4 = ttk.Button(ventana, text="4", command=lambda: obtener_texto("4"))
boton4.grid(column=2, row=4)

boton5 = ttk.Button(ventana, text="5", command=lambda: obtener_texto("5"))
boton5.grid(column=3, row=4)

boton6 = ttk.Button(ventana, text="6", command=lambda: obtener_texto("6"))
boton6.grid(column=1, row=5)

boton7 = ttk.Button(ventana, text="7", command=lambda: obtener_texto("7"))
boton7.grid(column=2, row=5)

boton8 = ttk.Button(ventana, text="8", command=lambda: obtener_texto("8"))
boton8.grid(column=3, row=5)

boton9 = ttk.Button(ventana, text="9", command=lambda: obtener_texto("9"))
boton9.grid(column=1, row=6)

# Botones de operaciones
botonSuma = ttk.Button(ventana, text="+", command=lambda: obtener_texto("+"))
botonSuma.grid(column=2, row=6)

botonResta = ttk.Button(ventana, text="-", command=lambda: obtener_texto("-"))
botonResta.grid(column=3, row=6)

botonMul = ttk.Button(ventana, text="*", command=lambda: obtener_texto("*"))
botonMul.grid(column=1, row=7)

botonDiv = ttk.Button(ventana, text="/", command=lambda: obtener_texto("/"))
botonDiv.grid(column=2, row=7)

botonIgual = ttk.Button(ventana, text="=", command=lambda: obtener_texto("="))
botonIgual.grid(column=3, row=7)

# Botón para punto decimal
botonPunto = ttk.Button(ventana, text=".", command=lambda: obtener_texto("."))
botonPunto.grid(column=2, row=8)

ventana.mainloop()