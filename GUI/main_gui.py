import customtkinter as ctk
from tab_components import ComponentsTab
from tab_documents import DocumentsTab
from tab_administration import AdministrationTab

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Base de Datos de Harmoni - CAB")
        self.geometry("1600x800")  # Tamaño de ventana aumentado

        # Configuración de la cuadrícula
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)

        # Crear la cabecera
        self.header_frame = ctk.CTkFrame(self, height=60, corner_radius=0)  # Aumentar la altura de la cabecera
        self.header_frame.grid(row=0, column=0, columnspan=3, sticky="ew")
        self.header_frame.grid_propagate(False)

        self.header_label = ctk.CTkLabel(self.header_frame, text="Base de Datos de Harmoni - CAB", font=("Arial", 24, "bold"))
        self.header_label.pack(pady=15)

        # Crear las pestañas
        self.tabview = ctk.CTkTabview(self, width=1600, height=60)  # Aumentar el ancho de las pestañas
        self.tabview.grid(row=1, column=0, columnspan=3, sticky="ew")
        self.tabview.add("Componentes")
        self.tabview.add("Documentos")
        self.tabview.add("Administración")

        # Agregar el contenido a las pestañas
        self.componentes_tab = ComponentsTab(self.tabview.tab("Componentes"))
        self.componentes_tab.pack(fill="both", expand=True)

        # Configuración inicial
        self.update_gui({})  # Inicializa con datos vacíos

    def update_gui(self, data):
        # Llama a la función update_gui en la pestaña "Componentes"
        self.componentes_tab.update_gui(data)

if __name__ == "__main__":
    app = App()
    app.mainloop()