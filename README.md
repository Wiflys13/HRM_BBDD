# HRM_BBDD

La gestión y organización de la base de datos sigue la siguiente estructura:

my_project/
├── app/
│ ├── init.py
│ ├── main.py
│ ├── config.py/
│ │ ├── init.py
│ │ └── config.py
│ ├── models/
│ ├── schemas/
│ ├── repositories/
│ ├── services/
│ ├── routers/
│ ├── dependencies/
│ └── utils/
│ └── logger.py
├── data/
├── notebooks/
├── GUI/
├── scripts/
└── requirements.txt

### Descripción de los Directorios

#### 'config/'
Se introduce la configuración de la base de datos, los directorios con los datos... 

#### `app/`
Contiene el código principal de la aplicación FastAPI.

##### `app/models/`
Define los modelos de datos de la aplicación.

- `component.py`: Define el modelo de datos para un componente mecánico.
- 

##### `app/schemas/`
Define los esquemas para la validación y serialización de datos con Pydantic.

- `component.py`: Define los esquemas Pydantic para crear, actualizar y ver componentes.


##### `app/repositories/`
Gestiona las operaciones de acceso a datos (CRUD) con la base de datos. Implementa el patrón Repository.

- `component_repository.py`: Implementa las operaciones CRUD para los componentes.


##### `app/services/`
Contiene la lógica de negocio y utiliza los repositorios para acceder a los datos.

- `component_service.py`: Contiene la lógica de negocio para los componentes.


##### `app/routers/`
Define los endpoints de la API. Cada recurso o grupo de recursos tiene su propio router.

- `component_router.py`: Define las rutas para los componentes mecánicos.


##### `app/dependencies/`
Define las dependencias de la aplicación que pueden ser inyectadas en los endpoints de FastAPI.

- `database.py`: Define la dependencia del repositorio que se inyectará en los endpoints.


##### `app/utils/`
Contiene funciones y clases auxiliares que se utilizan en diferentes partes de la aplicación.

- `logger.py`: Define una función para configurar y obtener un logger.


#### `data/`
Aquí se incluyen los imports a la base de datos.

#### `notebooks/`
Se realiza análisis exploratorio y preprocesamiento de los datos previo a introducirlos en la base de datos.

#### `GUI/`
Interfaz gráfica de la base de datos.

#### `scripts/`
Scripts varios de Python.