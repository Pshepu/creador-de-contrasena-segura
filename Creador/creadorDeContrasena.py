import tkinter as tk
import string
import random
from tkinter import messagebox

# Función que genera una contraseña segura
def contrasena_segura():
    try:
        longitud_de_contrasena = int(entry_longitud.get())  # Pide la longitud de la contraseña
        caracteres = string.ascii_letters + string.digits + string.punctuation  # Caracteres posibles
        contrasena = "".join(random.choice(caracteres) for i in range(longitud_de_contrasena))  # Genera la contraseña
        etiqueta_contrasena.config(text=f"La contraseña generada es: {contrasena}")  # Muestra la contraseña
        # Guarda la contraseña en una variable para usarla en copiar
        etiqueta_contrasena.password = contrasena
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido.")  # Manejo de errores

# Función para copiar la contraseña al portapapeles
def copiar_contrasena():
    try:
        root.clipboard_clear()  # Limpia el portapapeles
        root.clipboard_append(etiqueta_contrasena.password)  # Añade la contraseña al portapapeles
        messagebox.showinfo("Copiado", "Contraseña copiada al portapapeles.")  # Mensaje de confirmación
    except AttributeError:
        messagebox.showwarning("Advertencia", "Genera una contraseña primero.")  # Aviso si no se ha generado una

# Crea la ventana principal
root = tk.Tk()
root.title("Generador de Contraseñas Seguras")
root.geometry("400x400")  # Ajustado para más espacio

# Etiqueta y entrada para la longitud de la contraseña
etiqueta_longitud = tk.Label(root, text="Ingrese la longitud de la contraseña:")
etiqueta_longitud.pack(pady=10)

entry_longitud = tk.Entry(root)
entry_longitud.pack(pady=10)

# El botón para generar contraseña
boton_generar = tk.Button(root, text="Generar Contraseña", command=contrasena_segura, width=20, height=2)
boton_generar.pack(pady=10)

# Etiqueta para mostrar la contraseña generada
etiqueta_contrasena = tk.Label(root, text="")
etiqueta_contrasena.pack(pady=10)

# Botón para copiar la contraseña
boton_copiar = tk.Button(root, text="Copiar Contraseña", command=copiar_contrasena, width=20, height=2)
boton_copiar.pack(pady=10)

# Botón de salir
boton_salir = tk.Button(root, text="Salir", command=root.quit, width=20, height=2)
boton_salir.pack(pady=20)

# Iniciar el bucle principal
root.mainloop()
