import tkinter as tk
from tkinter import messagebox
import requests

def search_by_id():
    id = entry_id.get()
    response = requests.get(f'http://localhost:8000/components/search/id/{id}')
    if response.status_code == 200:
        result = response.json()
        messagebox.showinfo("Resultado", str(result))
    else:
        messagebox.showerror("Error", "Componente no encontrado")

def search_by_ci_identification():
    ci_identification = entry_ci_identification.get()
    response = requests.get(f'http://localhost:8000/components/search/ci_identification/{ci_identification}')
    if response.status_code == 200:
        result = response.json()
        messagebox.showinfo("Resultado", str(result))
    else:
        messagebox.showerror("Error", "Componente no encontrado")

app = tk.Tk()
app.title("Interfaz de Base de Datos")

# Widgets para buscar por ID
tk.Label(app, text="Buscar por ID:").pack()
entry_id = tk.Entry(app)
entry_id.pack()
tk.Button(app, text="Buscar", command=search_by_id).pack()

# Widgets para buscar por CI Identification
tk.Label(app, text="Buscar por CI Identification:").pack()
entry_ci_identification = tk.Entry(app)
entry_ci_identification.pack()
tk.Button(app, text="Buscar", command=search_by_ci_identification).pack()

app.mainloop()