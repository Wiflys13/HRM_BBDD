import customtkinter as ctk
import requests
import urllib.parse
from tkinter import messagebox  # Importar messagebox de tkinter

class ComponentsTab(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master)
        self.configure(bg_color="white")  # Establecer el color de fondo si es necesario

        # Crear la barra lateral para Insertar y Actualizar a la izquierda
        self.left_sidebar_frame = ctk.CTkFrame(self, width=250, corner_radius=0)  # Ampliar la barra lateral
        self.left_sidebar_frame.pack(side="left", fill="y")

        self.logo_label = ctk.CTkLabel(self.left_sidebar_frame, text="Opciones", font=("Arial", 18, "bold"))  # Aumentar el tamaño de fuente
        self.logo_label.pack(pady=(20, 10))

        self.insert_button = ctk.CTkButton(self.left_sidebar_frame, text="Insertar", command=self.insert_data)
        self.insert_button.pack(pady=10)

        self.update_button = ctk.CTkButton(self.left_sidebar_frame, text="Actualizar", command=self.update_data)
        self.update_button.pack(pady=10)

        # Área principal en el centro
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(side="left", fill="both", expand=True)

        # Contenedor de datos
        self.scrollable_frame = ctk.CTkScrollableFrame(self.main_frame)
        self.scrollable_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Barra lateral para Buscar y Aplicar Filtros a la derecha
        self.right_sidebar_frame = ctk.CTkFrame(self, width=250, corner_radius=0)  # Ampliar el marco de filtro
        self.right_sidebar_frame.pack(side="right", fill="y")

        self.filter_label = ctk.CTkLabel(self.right_sidebar_frame, text="Filtrar Datos", font=("Arial", 18, "bold"))  # Aumentar el tamaño de fuente
        self.filter_label.pack(pady=(20, 10))

        self.filter_entry = ctk.CTkEntry(self.right_sidebar_frame, placeholder_text="Ingrese criterio")
        self.filter_entry.pack(pady=10)

        self.apply_filter_button = ctk.CTkButton(self.right_sidebar_frame, text="Aplicar Filtro", command=self.apply_filter)
        self.apply_filter_button.pack(pady=10)

        self.clear_filter_button = ctk.CTkButton(self.right_sidebar_frame, text="Limpiar Filtro", command=self.clear_filter)
        self.clear_filter_button.pack(pady=10)

        self.search_button = ctk.CTkButton(self.right_sidebar_frame, text="Buscar", command=self.open_search_dialog)
        self.search_button.pack(pady=10)

    def open_search_dialog(self):
        # Implementar el diálogo de búsqueda
        search_term = ctk.CTkInputDialog(text="Ingrese la identificación del componente", title="Buscar Componente").get_input()
        if search_term:
            self.search_component_by_ci_identification(search_term)

    def search_component_by_ci_identification(self, ci_identification):
        try:
            # Codificar el término de búsqueda para la URL
            encoded_ci_identification = urllib.parse.quote(ci_identification)
            response = requests.get(f'http://localhost:8000/components/search/ci_identification/{encoded_ci_identification}')
            if response.status_code == 200:
                result = response.json()
                self.update_gui(result)
            else:
                messagebox.showerror("Error", "Componente no encontrado")  # Cambiar a messagebox.showerror
        except Exception as e:
            messagebox.showerror("Error", str(e))  # Cambiar a messagebox.showerror

    def insert_data(self):
        # Implementar la función de inserción de datos
        messagebox.showinfo("Insertar", "Funcionalidad de inserción no implementada")  # Cambiar a messagebox.showinfo

    def update_data(self):
        # Implementar la función de actualización de datos
        messagebox.showinfo("Actualizar", "Funcionalidad de actualización no implementada")  # Cambiar a messagebox.showinfo

    def apply_filter(self):
        # Implementar la aplicación del filtro
        filter_criteria = self.filter_entry.get()
        messagebox.showinfo("Filtrar", f"Aplicar filtro: {filter_criteria}")  # Cambiar a messagebox.showinfo

    def clear_filter(self):
        # Implementar la limpieza del filtro
        self.filter_entry.delete(0, ctk.END)
        messagebox.showinfo("Filtrar", "Filtro limpiado")  # Cambiar a messagebox.showinfo

    def format_json_by_category(self, data):
        categories = {
            "PBS": [
                "ci_identification", "pbs_name", "pbs_acronym", "pbs_level",
                "pbs_system", "pbs_subsystem", "pbs_module", "pbs_unit",
                "pbs_assembly", "pbs_subassembly", "pbs_component", "notes_and_comments"
            ],
            "Component": [
                "pbs_is_component", "component_status", "component_description",
                "component_type", "component_field"
            ],
            "Procurement": [
                "procurement_supplier", "procurement_manufacturer",
                "manufacturer_part_number", "procurement_catalog_reference",
                "procurement_cost_unit", "procurement_cost_status", "procurement_quantity"
            ],
            "Mechanical": [
                "mechanical_mass", "mechanical_material", "mechanical_treatment",
                "mechanical_coating", "mechanical_step_link"
            ],
            "Electrical": [
                "electrical_power_budget", "electrical_current_ps_only", "electrical_voltage_dc",
                "electrical_voltage_ac", "electrical_initialization_power",
                "electrical_initialization_current", "electrical_standby_power",
                "electrical_standby_current", "electrical_calibration_power",
                "electrical_calibration_current", "electrical_observation_power",
                "electrical_observation_current", "electrical_maintenance_power",
                "electrical_maintenance_current", "electrical_ups_power_required",
                "electrical_ups_power_time_required_ups"
            ],
            "Thermical": [
                "thermical_heat_dissipated", "thermical_heat_load_to_air",
                "thermical_heat_load_to_coolant", "thermical_skin_temperature_above_ambient",
                "thermical_requires_cooling"
            ],
            "Cables": [
                "cables_function", "cables_max_length", "cables_length",
                "cables_outer_diameter", "cables_min_bending_radius_dynamic",
                "cables_min_bending_radius_static", "cables_mass_density"
            ]
        }

        formatted_text = {}
        for category, fields in categories.items():
            formatted_text[category] = ""
            for field in fields:
                if field in data:
                    formatted_text[category] += f"{field.replace('_', ' ').title()}: {data[field]}\n"

        return formatted_text

    def update_gui(self, data):
        # Limpiar el área principal
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Formatear los datos
        formatted_data = self.format_json_by_category(data)

        # Agregar datos formateados a la interfaz gráfica
        for category, text in formatted_data.items():
            if text:  # Solo agregar categorías no vacías
                category_frame = ctk.CTkFrame(self.scrollable_frame)
                category_frame.pack(padx=10, pady=5, fill="x")
                
                category_label = ctk.CTkLabel(category_frame, text=category, font=("Arial", 14, "bold"))
                category_label.pack(padx=5, pady=5, anchor="w")
                
                data_label = ctk.CTkLabel(category_frame, text=text, font=("Arial", 12))
                data_label.pack(padx=5, pady=5, anchor="w")
