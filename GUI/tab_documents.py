import customtkinter as ctk

class DocumentsTab(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        # Aquí puedes agregar elementos específicos para la pestaña de Documentos
        self.label = ctk.CTkLabel(self, text="Documentos", font=("Arial", 16, "bold"))
        self.label.pack(pady=10)
        # Añadir más widgets y funcionalidades según sea necesario