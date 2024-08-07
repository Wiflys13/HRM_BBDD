import customtkinter as ctk
import requests
import urllib.parse

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurar la ventana
        self.title("Base de Datos de Harmoni - CAB")
        self.geometry("1600x800")  # Tamaño de ventana aumentado

        # Configurar la cuadrícula
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

        # Contenido de la pestaña "Componentes"
        self.componentes_frame = ctk.CTkFrame(self.tabview.tab("Componentes"))
        self.componentes_frame.pack(fill="both", expand=True)

        # Contenido de la pestaña "Documentos"
        self.documentos_frame = ctk.CTkFrame(self.tabview.tab("Documentos"))
        self.documentos_frame.pack(fill="both", expand=True)

        # Contenido de la pestaña "Administración"
        self.administracion_frame = ctk.CTkFrame(self.tabview.tab("Administración"))
        self.administracion_frame.pack(fill="both", expand=True)

        # Crear la barra lateral
        self.sidebar_frame = ctk.CTkFrame(self.componentes_frame, width=250, corner_radius=0)  # Ampliar la barra lateral
        self.sidebar_frame.grid(row=0, column=0, sticky="ns")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Opciones", font=("Arial", 18, "bold"))  # Aumentar el tamaño de fuente
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.insert_button = ctk.CTkButton(self.sidebar_frame, text="Insertar", command=self.insert_data)
        self.insert_button.grid(row=1, column=0, padx=20, pady=10)

        self.search_button = ctk.CTkButton(self.sidebar_frame, text="Buscar", command=self.open_search_dialog)
        self.search_button.grid(row=2, column=0, padx=20, pady=10)

        self.update_button = ctk.CTkButton(self.sidebar_frame, text="Actualizar", command=self.update_data)
        self.update_button.grid(row=3, column=0, padx=20, pady=10)

        # Área principal
        self.main_frame = ctk.CTkFrame(self.componentes_frame)
        self.main_frame.grid(row=0, column=1, sticky="nsew")

        # Configurar la expansión de la cuadrícula
        self.componentes_frame.grid_columnconfigure(1, weight=3)
        self.componentes_frame.grid_columnconfigure(2, weight=1)
        self.componentes_frame.grid_rowconfigure(0, weight=1)

        # Contenedor de datos
        self.scrollable_frame = ctk.CTkScrollableFrame(self.main_frame)
        self.scrollable_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Filtro
        self.filter_frame = ctk.CTkFrame(self.componentes_frame, width=250, corner_radius=0)  # Ampliar el marco de filtro
        self.filter_frame.grid(row=0, column=2, sticky="ns")
        self.filter_frame.grid_rowconfigure(4, weight=1)

        self.filter_label = ctk.CTkLabel(self.filter_frame, text="Filtrar Datos", font=("Arial", 18, "bold"))  # Aumentar el tamaño de fuente
        self.filter_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.filter_entry = ctk.CTkEntry(self.filter_frame, placeholder_text="Ingrese criterio")
        self.filter_entry.grid(row=1, column=0, padx=20, pady=10)

        self.apply_filter_button = ctk.CTkButton(self.filter_frame, text="Aplicar Filtro", command=self.apply_filter)
        self.apply_filter_button.grid(row=2, column=0, padx=20, pady=10)

        self.clear_filter_button = ctk.CTkButton(self.filter_frame, text="Limpiar Filtro", command=self.clear_filter)
        self.clear_filter_button.grid(row=3, column=0, padx=20, pady=10)

        # Configuración inicial
        self.update_gui({})  # Inicializa con datos vacíos

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
                ctk.CTkMessageBox.show_error("Error", "Componente no encontrado")
        except Exception as e:
            ctk.CTkMessageBox.show_error("Error", str(e))

    def insert_data(self):
        # Implementar la función de inserción de datos
        ctk.CTkMessageBox.show_info("Insertar", "Funcionalidad de inserción no implementada")

    def update_data(self):
        # Implementar la función de actualización de datos
        ctk.CTkMessageBox.show_info("Actualizar", "Funcionalidad de actualización no implementada")

    def apply_filter(self):
        # Implementar la aplicación del filtro
        filter_criteria = self.filter_entry.get()
        ctk.CTkMessageBox.show_info("Filtrar", f"Aplicar filtro: {filter_criteria}")

    def clear_filter(self):
        # Implementar la limpieza del filtro
        self.filter_entry.delete(0, ctk.END)
        ctk.CTkMessageBox.show_info("Filtrar", "Filtro limpiado")

    def format_json_by_category(self, data):
        categories = {
            "PBS": [
                "id", "pbs_number", "pbs_name", "pbs_acronym", "pbs_level",
                "pbs_system", "pbs_subsystem", "pbs_module", "pbs_unit",
                "pbs_assembly", "pbs_subassembly", "pbs_component"
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
                "electrical_power_budget", "electrical_current_ps_only", "electrical_voltaje_dc",
                "electrical_voltaje_ac", "electrical_initialization_power",
                "electrical_initialization_current", "electrical_standby_power",
                "electrical_standby_current", "electrical_calibration_power",
                "electrical_calibration_current", "electrical_observation_power",
                "electrical_observation_current", "electrical_maintenance_power",
                "electrical_maintenance_current", "electrical_ups_power_required",
                "electrical_ups_power_time_required_ups"
            ],
            "Thermical": [
                "thermical_heat_dissipated", "thermical_head_load_to_air",
                "thermical_head_load_to_coolant", "thermical_skin_temperature_above_ambient",
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

if __name__ == "__main__":
    app = App()
    app.mainloop()
