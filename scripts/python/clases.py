#Para llamar a los atributos: print(bom_instance.pbs.name)  # Output: Component Name
# print(bom_instance.procurement.supplier)  # Output: Supplier A
from typing import Optional

#Orden para las Clases
"""
Componentes: 
    ci_identificación
    item_name
    acronym
    notes

PartNumber(Components)
    ci_identification
    level
    system
    subsystem
    module
    unit
    assembly
    subassembly
    component
    
BoM(PartNumber)
    ci_identification
    is_component
    status
    description
    type
    field

Procurement
    
"""



class PartNumber:
    """Clase para los datos provenientes de Product Number Tracking"""
    def __init__(self, ci_identification: str, item_name: str, acronym: str, level: int, system: int, 
                 subsystem: int, module: int, unit: int, assembly: int, subassembly: int, 
                 component: int, notes_and_comments: str):
        self.__ci_identification = ci_identification
        self.__item_name = item_name
        self.__acronym = acronym
        self.__level = level
        self.__system = system
        self.__subsystem = subsystem
        self.__module = module
        self.__unit = unit
        self.__assembly = assembly
        self.__subassembly = subassembly
        self.__component = component
        self.__notes_and_comments = notes_and_comments
        
    def __str__(self):
        return f'Componente:{self.__item_name}'    

    # Getters
    @property
    def ci_identification(self):
        return self.__ci_identification
    @property
    def item_name(self):
        return self.__item_name
    @property
    def acronym(self):
        return self.__acronym
    @property
    def level(self):
        return self.__level
    @property
    def system(self):
        return self.__system
    @property
    def subsystem(self):
        return self.__subsystem
    @property
    def module(self):
        return self.__module
    @property
    def unit(self):
        return self.__unit
    @property
    def assembly(self):
        return self.__assembly
    @property
    def subassembly(self):
        return self.__subassembly
    @property
    def component(self):
        return self.__component
    @property
    def notes(self):
        return self.__notes_and_comments

    # Setters
    @ci_identification.setter
    def ci_identification(self, value):
        self.__ci_identification = value
    @item_name.setter
    def item_name(self, value):
        self.__item_name = value
    @acronym.setter
    def acronym(self, value):
        self.__acronym = value
    @level.setter
    def level(self, value):
        self.__level = value
    @system.setter
    def system(self, value):
        self.__system = value
    @subsystem.setter
    def subsystem(self, value):
        self.__subsystem = value
    @module.setter
    def module(self, value):
        self.__module = value
    @unit.setter
    def unit(self, value):
        self.__unit = value
    @assembly.setter
    def assembly(self, value):
        self.__assembly = value
    @subassembly.setter
    def subassembly(self, value):
        self.__subassembly = value
    @component.setter
    def component(self, value):
        self.__component = value
    @notes.setter
    def notes(self, value):
        self.__notes_and_comments = value
        
    #Convertir a diccionario
    def to_dict(self):
        """Convertir la instancia a un diccionario"""
        return {
            'ci_identification': self.ci_identification,
            'item_name': self.item_name,
            'acronym': self.acronym,
            'level': self.level,
            'system': self.system,
            'subsystem': self.subsystem,
            'module': self.module,
            'unit': self.unit,
            'assembly': self.assembly,
            'subassembly': self.subassembly,
            'component': self.component,
            'notes_and_comments': self.notes_and_comments
        }

class ComponentStatus:
    def __init__(self, ci_identification: str, is_component: bool, status: str, description: str, type: str, field: str):
        self.__ci_identification = ci_identification
        self.__is_component = is_component
        self.__status = status
        self.__description = description
        self.__type = type
        self.__field = field
    
    # Getters
    @property
    def ci_identification(self):
        return self.__ci_identification    
    @property
    def is_component(self):
        return self.__is_component
    @property
    def status(self):
        return self.__status
    @property
    def description(self):
        return self.__description
    @property
    def type(self):
        return self.__type
    @property
    def field(self):
        return self.__field
    
    # Setters
    @ci_identification.setter
    def ci_identification(self, value):
        self.__ci_identification = value
    @is_component.setter
    def ci_identification(self, value):
        self.__ci_identification = value
    @is_component.setter
    def is_component(self, value):
        self.__is_component = value
    @status.setter
    def status(self, value):
        self.__status = value
    @description.setter
    def description(self, value):
        self.__description = value
    @type.setter
    def type(self, value):
        self.__type = value
    @field.setter
    def field(self, value):
        self.__field = value
        
    
    # Convert to dictionary
    def to_dict(self):
        return {
            "ci_identification": self.ci_identification,
            "is_component": self.is_component,
            "status": self.status,
            "description": self.description,
            "type": self.type,
            "field": self.field
        }

class Procurement:
    def __init__(self, ci_identification: str, supplier: str, manufacturer: str, part_number: str, catalog_reference: str, cost_unit: float, 
                 cost_status: str, quantity: int):
        self.__ci_identification = ci_identification
        self.__supplier = supplier
        self.__manufacturer = manufacturer
        self.__part_number = part_number
        self.__catalog_reference = catalog_reference
        self.__cost_unit = cost_unit
        self.__cost_status = cost_status
        self.__quantity = quantity
    
    # Getters
    @property
    def ci_identification(self):
        return self.__ci_identification    
    @property
    def supplier(self):
        return self.__supplier
    @property
    def manufacturer(self):
        return self.__manufacturer
    @property
    def part_number(self):
        return self.__part_number
    @property
    def catalog_reference(self):
        return self.__catalog_reference
    @property
    def cost_unit(self):
        return self.__cost_unit
    @property
    def cost_status(self):
        return self.__cost_status
    @property
    def quantity(self):
        return self.__quantity
    
    # Setters
    @ci_identification.setter
    def ci_identification(self, value):
        self.__ci_identification = value    
    @supplier.setter
    def supplier(self, value):
        self.__supplier = value
    @manufacturer.setter
    def manufacturer(self, value):
        self.__manufacturer = value
    @part_number.setter
    def part_number(self, value):
        self.__part_number = value
    @catalog_reference.setter
    def catalog_reference(self, value):
        self.__catalog_reference = value
    @cost_unit.setter
    def cost_unit(self, value):
        self.__cost_unit = value
    @cost_status.setter
    def cost_status(self, value):
        self.__cost_status = value
    @quantity.setter
    def quantity(self, value):
        self.__quantity = value


class Electrical:
    def __init__(self, ci_identification: str, power_budget: float, current_ps_only: str, voltage_dc: float, voltage_ac: float, 
                 init_power: float, init_current: float, standby_power: float, standby_current: float, 
                 calib_power: float, calib_current: float, obs_power: float, obs_current: float, 
                 maint_power: float, maint_current: float, ups_power_required: str, ups_power_time: str):
        self.__ci_identification = ci_identification
        self.__power_budget = power_budget
        self.__current_ps_only = current_ps_only
        self.__voltage_dc = voltage_dc
        self.__voltage_ac = voltage_ac
        self.__init_power = init_power
        self.__init_current = init_current
        self.__standby_power = standby_power
        self.__standby_current = standby_current
        self.__calib_power = calib_power
        self.__calib_current = calib_current
        self.__obs_power = obs_power
        self.__obs_current = obs_current
        self.__maint_power = maint_power
        self.__maint_current = maint_current
        self.__ups_power_required = ups_power_required
        self.__ups_power_time = ups_power_time
    
    # Getters
    @property
    def ci_identification(self):
        return self.__ci_identification    
    @property
    def power_budget(self):
        return self.__power_budget
    @property
    def current_ps_only(self):
        return self.__current_ps_only
    @property
    def voltage_dc(self):
        return self.__voltage_dc
    @property
    def voltage_ac(self):
        return self.__voltage_ac
    @property
    def init_power(self):
        return self.__init_power
    @property
    def init_current(self):
        return self.__init_current
    @property
    def standby_power(self):
        return self.__standby_power
    @property
    def standby_current(self):
        return self.__standby_current
    @property
    def calib_power(self):
        return self.__calib_power
    @property
    def calib_current(self):
        return self.__calib_current
    @property
    def obs_power(self):
        return self.__obs_power
    @property
    def obs_current(self):
        return self.__obs_current
    @property
    def maint_power(self):
        return self.__maint_power
    @property
    def maint_current(self):
        return self.__maint_current
    @property
    def ups_power_required(self):
        return self.__ups_power_required
    @property
    def ups_power_time(self):
        return self.__ups_power_time
    
    # Setters
    @ci_identification.setter
    def ci_identification(self, value):
        self.__ci_identification = value
    @power_budget.setter
    def power_budget(self, value):
        self.__power_budget = value
    @current_ps_only.setter
    def current_ps_only(self, value):
        self.__current_ps_only = value
    @voltage_dc.setter
    def voltage_dc(self, value):
        self.__voltage_dc = value
    @voltage_ac.setter
    def voltage_ac(self, value):
        self.__voltage_ac = value
    @init_power.setter
    def init_power(self, value):
        self.__init_power = value
    @init_current.setter
    def init_current(self, value):
        self.__init_current = value
    @standby_power.setter
    def standby_power(self, value):
        self.__standby_power = value
    @standby_current.setter
    def standby_current(self, value):
        self.__standby_current = value
    @calib_power.setter
    def calib_power(self, value):
        self.__calib_power = value
    @calib_current.setter
    def calib_current(self, value):
        self.__calib_current = value
    @obs_power.setter
    def obs_power(self, value):
        self.__obs_power = value
    @obs_current.setter
    def obs_current(self, value):
        self.__obs_current = value    
    @maint_power.setter
    def maint_power(self, value):
        self.__maint_power = value
    @maint_current.setter
    def maint_current(self, value):
        self.__maint_current = value
    @ups_power_required.setter
    def ups_power_required(self, value):
        self.__ups_power_required = value
    @ups_power_time.setter
    def ups_power_time(self, value):
        self.__ups_power_time = value


class BoM:
    def __init__(self, id: Optional[str] = None, pbs: PBS, component_status: ComponentStatus, procurement: Procurement, electrical: Electrical):
        self.id = id
        self.pbs = pbs
        self.component_status = component_status
        self.procurement = procurement
        self.electrical = electrical

    def __str__(self):
        return f'BoM(PBS: {self.pbs}, Component Status: {self.component_status}, Procurement: {self.procurement}, Electrical: {self.electrical})'
    
    # Methods to update individual modules can be added here

# Función para leer archivos .csv
def leer_csv(ruta_archivo):
    return pd.read_csv(ruta_archivo)

# Funciones para crear instancias de los módulos
def crear_instancia_pbs(df):
    # Crear y devolver una instancia de PBS
    pass

def crear_instancia_component_status(df):
    # Crear y devolver una instancia de ComponentStatus
    pass

def crear_instancia_procurement(df):
    # Crear y devolver una instancia de Procurement
    pass

def crear_instancia_electrical(df):
    # Crear y devolver una instancia de Electrical
    pass
    
## Leer los archivos .csv
# df_pbs = leer_csv('ruta_al_archivo_pbs.csv')
# df_component_status = leer_csv('ruta_al_archivo_component_status.csv')
# df_procurement = leer_csv('ruta_al_archivo_procurement.csv')
# df_electrical = leer_csv('ruta_al_archivo_electrical.csv')

# # Crear instancias de los módulos
# pbs = crear_instancia_pbs(df_pbs)
# component_status = crear_instancia_component_status(df_component_status)
# procurement = crear_instancia_procurement(df_procurement)
# electrical = crear_instancia_electrical(df_electrical)

# # Crear una instancia de BoM
# bom = BoM(pbs, component_status, procurement, electrical)

# # Imprimir la instancia de BoM
# print(bom)