import tkinter as tk
import string
import random
from tkinter import messagebox

# Función que genera una contraseña segura
# La función nos pide que ingresemos una longitud de la contraseña a usar (el largo)
# esta contraseña incluye letras, dígitos, puntuaciones y símbolos varios

def contrasena_segura():
    try:
        longitud_de_contrasena = int(entry_longitud.get()) #pide la longitud de la contraseña, cuantos caracteres tendra
        caracteres = string.ascii_letters + string.digits + string.punctuation #guarda en un string anidado todo lo que esta de acuerdo a ASCII
        contrasena = "".join(random.choice(caracteres) for i in range(longitud_de_contrasena)) #lo que hace es tomar un char aleatorio del string acorde a la longitud
        etiqueta_contrasena.config(text=f"La contraseña generada es: {contrasena}") #imprime en pantalla la contraseña
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido.") # esto es para que no se ingrese un caracter u otra cosa

# Crea la ventana principal
root = tk.Tk()
root.title("Generador de Contraseñas Seguras")

#se ajusta la pantalla a 400 pixeles x 400 pixeles
root.geometry("400x400")  # Ajustado para más espacio

# Etiqueta y entrada para la longitud de la contraseña
etiqueta_longitud = tk.Label(root, text="Ingrese la longitud de la contraseña:")
etiqueta_longitud.pack(pady=10)

entry_longitud = tk.Entry(root)
entry_longitud.pack(pady=10)

# El boton para generar contraseña
boton_generar = tk.Button(root, text="Generar Contraseña", command=contrasena_segura, width=20, height=2)
boton_generar.pack(pady=10)

# Etiqueta para mostrar la contraseña generada
etiqueta_contrasena = tk.Label(root, text="")
etiqueta_contrasena.pack(pady=10)

# Botón de salir
boton_salir = tk.Button(root, text="Salir", command=root.quit, width=20, height=2)
boton_salir.pack(pady=20)

# Iniciar el bucle principal
root.mainloop()
