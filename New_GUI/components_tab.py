import customtkinter as ctk
import requests
import urllib.parse
from tkinter import messagebox

class ComponentsTab(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master)
        self.configure(bg_color="white")

        # Crear la cuadrícula para la disposición de los widgets
        self.grid_columnconfigure(0, weight=1)  # Barra lateral
        self.grid_columnconfigure(1, weight=2)  # Contenedor de búsqueda
        self.grid_columnconfigure(2, weight=4)  # Contenedor de resultados
        self.grid_rowconfigure(0, weight=0)     # Espacio para la cabecera
        self.grid_rowconfigure(1, weight=1)     # Área principal

        # Barra lateral de opciones
        self.left_sidebar_frame = ctk.CTkFrame(self, width=250, corner_radius=0)
        self.left_sidebar_frame.grid(row=1, column=0, sticky="nswe")
        self.left_sidebar_frame.grid_propagate(False)

        self.logo_label = ctk.CTkLabel(self.left_sidebar_frame, text="Opciones", font=("Arial", 18, "bold"))
        self.logo_label.pack(pady=(20, 10))

        self.insert_button = ctk.CTkButton(self.left_sidebar_frame, text="Insertar", command=self.insert_data)
        self.insert_button.pack(pady=10)

        self.update_button = ctk.CTkButton(self.left_sidebar_frame, text="Actualizar", command=self.update_data)
        self.update_button.pack(pady=10)

        # Botón único de búsqueda
        self.search_button = ctk.CTkButton(self.left_sidebar_frame, text="Buscar", command=self.perform_search)
        self.search_button.pack(pady=10)

        # Contenedor de búsqueda con scrollbar
        self.search_frame = ctk.CTkFrame(self, corner_radius=0)
        self.search_frame.grid(row=1, column=1, sticky="nswe")
        self.search_frame.grid_propagate(False)

        # Scrollable Frame dentro del contenedor de búsqueda
        self.scrollable_search_frame = ctk.CTkScrollableFrame(self.search_frame)
        self.scrollable_search_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Campo de búsqueda compactos
        self.fields = {
            "ID": "id",
            "CI Identification": "ci_identification",
            "PBS Acronym": "acronym",
            "PBS System": "system",
            "PBS Subsystem": "subsystem",
            "PBS Module": "module",
            "PBS Unit": "unit",
            "PBS Assembly": "assembly",
            "PBS Subassembly": "subassembly",
            "PBS Component": "component"
        }

        self.entries = {}

        for label_text, endpoint in self.fields.items():
            field_frame = ctk.CTkFrame(self.scrollable_search_frame)
            field_frame.pack(pady=5, fill="x")

            label = ctk.CTkLabel(field_frame, text=label_text)
            label.pack(side="left", padx=5, pady=5)

            entry = ctk.CTkEntry(field_frame, width=150, placeholder_text=f"Ingrese {label_text}")
            entry.pack(side="left", padx=5, pady=5)
            self.entries[endpoint] = entry

        # Contenedor de resultados
        self.results_frame = ctk.CTkFrame(self, corner_radius=0)
        self.results_frame.grid(row=1, column=2, sticky="nswe")

        self.results_label = ctk.CTkLabel(self.results_frame, text="Resultados", font=("Arial", 18, "bold"))
        self.results_label.pack(pady=(20, 10))

        self.scrollable_results_frame = ctk.CTkScrollableFrame(self.results_frame)
        self.scrollable_results_frame.pack(fill="both", expand=True, padx=20, pady=20)

    def perform_search(self):
        # Iterar a través de los campos para determinar cuál tiene valor
        for endpoint, entry in self.entries.items():
            search_term = entry.get()
            if search_term:
                self.search_component(endpoint, search_term)
                return  # Salir después de realizar la búsqueda para evitar búsquedas múltiples

        # Mostrar mensaje si ningún campo tiene valor
        messagebox.showwarning("Advertencia", "Por favor, ingrese un valor en al menos uno de los campos de búsqueda.")

    def search_component(self, endpoint, search_term):
        try:
            encoded_term = urllib.parse.quote(search_term)
            url = f'http://localhost:8000/components/search/{endpoint}/{encoded_term}'
            response = requests.get(url)
            if response.status_code == 200:
                result = response.json()
                self.update_results(result)
            else:
                messagebox.showerror("Error", "Componente no encontrado")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_results(self, data):
        # Limpiar el área de resultados
        for widget in self.scrollable_results_frame.winfo_children():
            widget.destroy()

        # Mostrar los resultados
        if isinstance(data, list) and data:
            for item in data:
                formatted_data = self.format_json_by_category(item)
                for category, text in formatted_data.items():
                    if text:  # Solo mostrar categorías no vacías
                        category_frame = ctk.CTkFrame(self.scrollable_results_frame)
                        category_frame.pack(padx=10, pady=5, fill="x")
                        
                        category_label = ctk.CTkLabel(category_frame, text=category, font=("Arial", 14, "bold"))
                        category_label.pack(padx=5, pady=5, anchor="w")
                        
                        data_label = ctk.CTkLabel(category_frame, text=text, font=("Arial", 12))
                        data_label.pack(padx=5, pady=5, anchor="w")
        else:
            empty_label = ctk.CTkLabel(self.scrollable_results_frame, text="No se encontraron resultados", font=("Arial", 14))
            empty_label.pack(padx=10, pady=10)

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

    # Métodos dummy para los botones Insertar y Actualizar
    def insert_data(self):
        messagebox.showinfo("Insertar", "Función Insertar aún no implementada")

    def update_data(self):
        messagebox.showinfo("Actualizar", "Función Actualizar aún no implementada")
