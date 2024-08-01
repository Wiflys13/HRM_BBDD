import customtkinter as ctk

class AdministrationTab(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        # Aquí puedes agregar elementos específicos para la pestaña de Administración
        self.label = ctk.CTkLabel(self, text="Administración", font=("Arial", 16, "bold"))
        self.label.pack(pady=10)
        # Añadir más widgets y funcionalidades según sea necesario