#components_tab.py
import csv
import pandas as pd
import numpy as np
import customtkinter as ctk
import requests
import urllib.parse
from tkinter import messagebox, ttk
from tkinter import filedialog, messagebox

class ComponentsTab(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master)
        self.configure(bg_color="white")

        # Crear la cuadrícula para la disposición de los widgets
        self.grid_columnconfigure(0, weight=1)  # Barra lateral
        self.grid_columnconfigure(1, weight=2)  # Contenedor de búsqueda
        self.grid_columnconfigure(2, weight=4)  # Contenedor de resultados
        self.grid_rowconfigure(0, weight=0)     # Espacio para la cabecera
        self.grid_rowconfigure(1, weight=1)     # Contenedor de búsqueda

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

        # Botón de descarga CSV
        self.download_button = ctk.CTkButton(self.left_sidebar_frame, text="Descargar CSV", command=self.download_csv)
        self.download_button.pack(pady=10)

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
        self.field_labels = []

        for label_text, endpoint in self.fields.items():
            field_frame = ctk.CTkFrame(self.scrollable_search_frame)
            field_frame.pack(pady=5, fill="x")

            label = ctk.CTkLabel(field_frame, text=label_text)
            label.pack(side="left", padx=5, pady=5)

            entry = ctk.CTkEntry(field_frame, width=150, placeholder_text=f"Ingrese {label_text}")
            entry.pack(side="left", padx=5, pady=5)
            self.entries[endpoint] = entry
            self.field_labels.append(label_text)

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
                self.show_results_in_popup(result)
            else:
                messagebox.showerror("Error", "Componente no encontrado")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_results_in_popup(self, data):
        # Crear el popup
        popup = ctk.CTkToplevel(self)
        popup.title("Resultados de Búsqueda")
        popup.geometry("800x600")
        
        # Asegúrate de que el popup siempre esté encima
        popup.attributes("-topmost", True)

        # Crear un frame para el Treeview y su scrollbar horizontal
        tree_frame = ctk.CTkFrame(popup)
        tree_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Configurar el Treeview
        tree = ttk.Treeview(tree_frame, show="headings")
        tree.pack(side="left", fill="both", expand=True)

        # Barra de desplazamiento horizontal
        h_scrollbar = ttk.Scrollbar(tree_frame, orient="horizontal", command=tree.xview)
        h_scrollbar.pack(side="bottom", fill="x")
        tree.configure(xscrollcommand=h_scrollbar.set)

        # Barra de desplazamiento vertical
        v_scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
        v_scrollbar.pack(side="right", fill="y")
        tree.configure(yscrollcommand=v_scrollbar.set)

        # Mostrar los resultados en una tabla horizontal
        if isinstance(data, list) and data:
            columns = list(data[0].keys())
            tree["columns"] = columns
            tree.heading("#0", text="ID")
            for col in columns:
                tree.heading(col, text=col.replace('_', ' ').title())
                tree.column(col, width=100, anchor='w')  # Ajustar el ancho y alineación

            for index, item in enumerate(data):
                values = [item.get(col, "") for col in columns]
                tree.insert("", "end", iid=index, text=index+1, values=values)
        else:
            tree["columns"] = ["No se encontraron resultados"]
            tree.heading("#0", text="")
            tree.insert("", "end", text="No se encontraron resultados")

        # Botón de descarga CSV
        download_button = ctk.CTkButton(popup, text="Descargar CSV", command=lambda: self.download_csv(popup, tree))
        download_button.pack(pady=10)

        # Configurar el popup para que siempre esté encima
        popup.lift()  # Eleva el popup sobre otras ventanas
        popup.focus_force()  # Fuerza el foco en el popup

    def download_csv(self, popup, tree):
        try:
            # Lleva el popup de resultados al frente para asegurarse de que no se minimice
            popup.lift()
            popup.attributes("-topmost", True)
            popup.attributes("-topmost", False)  # Restaurar el estado original

            # Abrir un cuadro de diálogo para elegir la ubicación y el nombre del archivo CSV
            file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                    filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
            if not file_path:
                return  # Salir si el usuario cancela el diálogo

            # Extraer los datos del Treeview
            data = []
            headers = [col for col in tree["columns"]]

            for item in tree.get_children():
                values = tree.item(item, 'values')
                # Convertir valores None a NaN
                row = [value if value is not None else pd.NA for value in values]
                data.append(row)

            # Crear un DataFrame de pandas
            df = pd.DataFrame(data, columns=headers)

            # Escribir el DataFrame en un archivo CSV
            df.to_csv(file_path, index=False, encoding='utf-8')

            # Mostrar mensaje de éxito después de que el cuadro de diálogo de descarga se cierre
            popup.after(100, lambda: messagebox.showinfo("Éxito", "Archivo CSV descargado correctamente."))
        except Exception as e:
            # Mostrar mensaje de error después de que el cuadro de diálogo de descarga se cierre
            popup.after(100, lambda: messagebox.showerror("Error", f"Error al guardar el archivo CSV: {str(e)}"))



    # Métodos dummy para los botones Insertar y Actualizar
    def insert_data(self):
        messagebox.showinfo("Insertar", "Función Insertar aún no implementada")

    def update_data(self):
        messagebox.showinfo("Actualizar", "Función Actualizar aún no implementada")
