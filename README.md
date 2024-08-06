# HRM_BBDD

La gestión y organización de la base de datos sigue la siguiente estructura:

```plaintext
my_project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── db/
│   │   ├── session.py
│   │   ├── base.py
│   │   └── init_db.py
│   ├── models/
│   │   ├── partnumber.py
│   │   ├── components.py
│   │   ├── electrical.py
│   │   ├── mechanical.py
│   │   └── procurement.py
│   ├── schemas/
│   │   ├── partnumber.py
│   │   ├── components.py
│   │   ├── electrical.py
│   │   ├── mechanical.py
│   │   └── procurement.py
│   ├── repositories/
│   │   └── component_repository.py
│   ├── services/
│   │   └── component_service.py
│   ├── routers/
│   │   └── component_router.py
│   ├── dependencies/
│   │   └── database.py
│   └── utils/
│       └── logger.py
├── data/
├── notebooks/
├── GUI/
├── scripts/
└── requirements.txt

### Descripción de los Directorios

#### 'config/'

#### `app/`
Contiene el código principal de la aplicación FastAPI.

##### `app/db/`
Contine lo relativo a la configuración y la gestión de la base de datos. Esto incluye la conexión a la base de datos, la inicializaciomn de la base de datos, migraciones en caso de que existan y otras utilidades relacionadas con la base de datos.


##### `app/models/`
Define los modelos de datos de la aplicación. Los modelos representan las estructuras de datos que se almacenan en la **base de datos**.
Su proposito principal es definir como se ven los datos y como se almacenan.
Pueden incluir configuraciones especificas de la base de datos como las claves primarias, índices y relaciones.

- `partnumber.py`: Define el modelo de datos para ...
- `components.py`: Define el modelo de datos para ...
- `electrical.py`: Define el modelo de datos para ...
- `mecanical.py`: Define el modelo de datos para ...
- `procuerement.py`: Define el modelo de datos para ....

##### `app/routers/`
Define los endpoints de la API. Cada recurso o grupo de recursos tiene su propio router.

- `component_router.py`: Define las rutas para los componentes mecánicos.

##### `app/schemas/`
Define los esquemas para la validación y serialización de datos en la API. Se utiliza pydantic para definir las estructuras de datos que se esperan recibir y enviar en las solicitudes
y respuestas de la **API**. Esto incluye validacion de datos de entrada y salida y garantiza que los datos sean correctos y completos.
Pueden incluir validadores personalizados y transformaciones de datos.
- `partnumber.py`: Define el modelo de datos para ...
- `components.py`: Define el modelo de datos para ...
- `electrical.py`: Define el modelo de datos para ...
- `mecanical.py`: Define el modelo de datos para ...
- `procuerement.py`: Define el modelo de datos para ....

##### `app/repositories/`
Los repositorios son responsables de interactuar directamente con la base de datos. Encapsulan las operaciones CRUD (Create, Read, Update, Delete) y proporcionan una abstraccion sobre la base de datos.

- `component_repository.py`: Implementa las operaciones CRUD para los componentes.

##### `app/services/`
Encapsulan la lógica de negocio de la aplicación. En lugar de manejar la lógica de negocio en los controladores (routers), se delega a los servicios para mantener los controladores ligeros y centrados en manejar las solicitudes HTTP.

- `component_service.py`: Contiene la lógica de negocio para los componentes.

##### `app/dependencies/`
Las dependencias se usan para inyectar dependencias en tus rutas de manera sencilla y eficiente. Esto incluye cosas como la conexión a la base de datos, servicios...
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