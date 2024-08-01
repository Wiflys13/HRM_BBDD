import customtkinter as ctk
import requests
import json

# Funciones para realizar búsquedas y mostrar resultados
def search_by_id():
    id = entry_id.get()
    response = requests.get(f'http://localhost:8000/components/search/id/{id}')
    if response.status_code == 200:
        result = response.json()
        formatted_result = json.dumps(result, indent=4)
        text_widget.delete(1.0, ctk.END)  # Limpiar el contenido previo
        text_widget.insert(ctk.END, formatted_result)
    else:
        ctk.CTkMessageBox.show_error("Error", "Componente no encontrado")

def search_by_ci_identification():
    ci_identification = entry_ci_identification.get()
    response = requests.get(f'http://localhost:8000/components/search/ci_identification/{ci_identification}')
    if response.status_code == 200:
        result = response.json()
        formatted_result = json.dumps(result, indent=4)
        text_widget.delete(1.0, ctk.END)  # Limpiar el contenido previo
        text_widget.insert(ctk.END, formatted_result)
    else:
        ctk.CTkMessageBox.show_error("Error", "Componente no encontrado")

# Configurar la ventana principal
app = ctk.CTk()
app.title("Interfaz de Base de Datos")
app.geometry("900x600")

# Estilo de CustomTkinter
ctk.set_appearance_mode("dark")  # Modo oscuro
ctk.set_default_color_theme("dark-blue")  # Tema oscuro predeterminado

# Función para crear botones con estilo personalizado
def create_custom_button(parent, text, command):
    return ctk.CTkButton(parent, text=text, command=command, fg_color="#2D6A4F", text_color="white")

# Widgets para buscar por ID
id_label = ctk.CTkLabel(app, text="Buscar por ID:")
id_label.pack(pady=5)
entry_id = ctk.CTkEntry(app, placeholder_text="Ingrese el ID")
entry_id.pack(pady=5)
id_button = create_custom_button(app, "Buscar", search_by_id)
id_button.pack(pady=5)

# Widgets para buscar por CI Identification
ci_label = ctk.CTkLabel(app, text="Buscar por CI Identification:")
ci_label.pack(pady=5)
entry_ci_identification = ctk.CTkEntry(app, placeholder_text="Ingrese CI Identification")
entry_ci_identification.pack(pady=5)
ci_button = create_custom_button(app, "Buscar", search_by_ci_identification)
ci_button.pack(pady=5)

# Widget de texto para mostrar los resultados
text_widget = ctk.CTkTextbox(app, width=80, height=20)
text_widget.pack(pady=10, fill="both", expand=True)

# Ejecutar la aplicación
app.mainloop()
