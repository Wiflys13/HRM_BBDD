#main_gui.py
import customtkinter as ctk
from components_tab import ComponentsTab
from documents_tab import DocumentsTab
from administration_tab import AdministrationTab

# Crear la aplicación principal
if __name__ == "__main__":
    class App(ctk.CTk):
        def __init__(self):
            super().__init__()
            self.title("Base de Datos de Harmoni - CAB")
            self.geometry("1600x800")

            # Configuración de la cuadrícula
            self.grid_columnconfigure(0, weight=1)
            self.grid_columnconfigure(1, weight=3)
            self.grid_columnconfigure(2, weight=1)
            self.grid_rowconfigure(0, weight=0)
            self.grid_rowconfigure(1, weight=1)

            # Crear la cabecera
            self.header_frame = ctk.CTkFrame(self, height=60, corner_radius=0)
            self.header_frame.grid(row=0, column=0, columnspan=3, sticky="ew")
            self.header_frame.grid_propagate(False)

            self.header_label = ctk.CTkLabel(self.header_frame, text="Base de Datos de Harmoni - CAB", font=("Arial", 24, "bold"))
            self.header_label.pack(pady=15)

            # Crear las pestañas
            self.tabview = ctk.CTkTabview(self, width=1600, height=800)
            self.tabview.grid(row=1, column=0, columnspan=3, sticky="nsew")
            self.tabview.add("Componentes")
            self.tabview.add("Documentos")
            self.tabview.add("Administración")

            # Agregar el contenido a las pestañas
            self.componentes_tab = ComponentsTab(self.tabview.tab("Componentes"))
            self.componentes_tab.pack(fill="both", expand=True)

            # Asumiendo que también quieres agregar contenido a las otras pestañas:
            self.documentos_tab = DocumentsTab(self.tabview.tab("Documentos"))
            self.documentos_tab.pack(fill="both", expand=True)

            self.administracion_tab = AdministrationTab(self.tabview.tab("Administración"))
            self.administracion_tab.pack(fill="both", expand=True)

    app = App()
    app.mainloop()
