#Ejercicio 3: Crear un formulario que valide la entrada de datos del usuario. Si la entrada es incorrecta, muestra un mensaje de error. Crea un formulario con campos para el nombre y el correo electrónico. Validemos que el nombre no esté vacío y que el correo electrónico contenga un @. Si la entrada no es válida, muestra un mensaje de error. Puedes emplear messagebox.showerror("Tu mensaje de error"). No olvides importar el componente: from tkinter import messagebox.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Validación")
ventana.geometry("400x300")

# Crear un frame para organizar el formulario
frame = ttk.Frame(ventana, padding="20")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Título del formulario
titulo = ttk.Label(frame, text="Formulario de Registro", font=("Arial", 16, "bold"))
titulo.grid(column=0, row=0, columnspan=2, pady=(0, 20))

# Etiqueta y entrada para el nombre
etiqueta_nombre = ttk.Label(frame, text="Nombre:")
etiqueta_nombre.grid(column=0, row=1, sticky=tk.W, pady=5)

entrada_nombre = ttk.Entry(frame, width=30)
entrada_nombre.grid(column=1, row=1, padx=(10, 0), pady=5)

# Etiqueta y entrada para el correo
etiqueta_correo = ttk.Label(frame, text="Correo electrónico:")
etiqueta_correo.grid(column=0, row=2, sticky=tk.W, pady=5)

entrada_correo = ttk.Entry(frame, width=30)
entrada_correo.grid(column=1, row=2, padx=(10, 0), pady=5)

# Función para validar los datos
def validar_formulario():
    nombre = entrada_nombre.get().strip()
    correo = entrada_correo.get().strip()
    
    # Validar que el nombre no esté vacío
    if not nombre:
        messagebox.showerror("Error de validación", "El nombre no puede estar vacío")
        entrada_nombre.focus()
        return
    
    # Validar que el correo no esté vacío
    if not correo:
        messagebox.showerror("Error de validación", "El correo electrónico no puede estar vacío")
        entrada_correo.focus()
        return
    
    # Validar que el correo contenga @
    if "@" not in correo:
        messagebox.showerror("Error de validación", "El correo electrónico debe contener el símbolo @")
        entrada_correo.focus()
        return
    
    # Validación adicional: verificar formato básico del correo
    if correo.count("@") != 1:
        messagebox.showerror("Error de validación", "El correo electrónico debe contener exactamente un símbolo @")
        entrada_correo.focus()
        return
    
    partes = correo.split("@")
    if len(partes[0]) == 0 or len(partes[1]) == 0:
        messagebox.showerror("Error de validación", "El formato del correo electrónico no es válido")
        entrada_correo.focus()
        return
    
    if "." not in partes[1]:
        messagebox.showerror("Error de validación", "El correo electrónico debe tener un dominio válido (ej: .com, .es)")
        entrada_correo.focus()
        return
    
    # Si todas las validaciones pasan, mostrar mensaje de éxito
    messagebox.showinfo("Registro exitoso", f"¡Bienvenido/a {nombre}!\nCorreo: {correo}")
    
    # Limpiar los campos después del registro exitoso
    entrada_nombre.delete(0, tk.END)
    entrada_correo.delete(0, tk.END)
    entrada_nombre.focus()

# Función para limpiar el formulario
def limpiar_formulario():
    entrada_nombre.delete(0, tk.END)
    entrada_correo.delete(0, tk.END)
    entrada_nombre.focus()

# Botones del formulario
frame_botones = ttk.Frame(frame)
frame_botones.grid(column=0, row=3, columnspan=2, pady=20)

boton_validar = ttk.Button(frame_botones, text="Validar y Registrar", command=validar_formulario)
boton_validar.grid(column=0, row=0, padx=5)

boton_limpiar = ttk.Button(frame_botones, text="Limpiar", command=limpiar_formulario)
boton_limpiar.grid(column=1, row=0, padx=5)

# Configurar el redimensionamiento
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

# Establecer el foco inicial en el campo nombre
entrada_nombre.focus()

# Permitir validar con Enter
def validar_con_enter(event):
    validar_formulario()

entrada_nombre.bind('<Return>', validar_con_enter)
entrada_correo.bind('<Return>', validar_con_enter)

ventana.mainloop()