# Hospital API Backend

Proyecto backend construido con **FastAPI** y **MySQL**, utilizando **SQLAlchemy** como ORM y **asyncmy** como driver de conexión asincrónica.

## Requisitos

- Python 3.11.9
- MySQL Server (local o remoto)
- Entorno virtual (`.venv`)

## Estructura del proyecto
```
hospital_api_backend/
│
├── app/
│   ├── api/                  # Rutas y versiones de la API
│   ├── crud/                 # Operaciones CRUD con SQLAlchemy
│   ├── db/                   # Configuración de la base de datos
│   ├── models/               # Modelos ORM
│   ├── schemas/              # Esquemas Pydantic
│   ├── services/             # Lógica de negocio
│   └── main.py               # Punto de entrada de la app FastAPI
│
├── .env                      # Variables de entorno
├── requirements.txt
└── README.md
```
## Instalación

1. Crear y activar el entorno virtual:

```bash
- En Windows
py -3.11 -m venv .venv
.venv\Scripts\activate

- En macOS
python3.11 -m venv .venv
source .venv/bin/activate
```
2. Instalar dependencias
```bash
pip install -r requirements.txt
```
3. Crear el .env en la raiz del proyecto especificando las variables de entorno:
```bash
    DATABASE_URL=mysql+asyncmy://usuario:contraseña@localhost:3306/hospital_db
    DEBUG=true #para desarrollo
    APP_NAME=Nombre del proyecto
    APP_VERSION=Version
    ALLOWED_ORIGINS=["*"]
```
4. Ejecutar el servidor
```bash
    uvicorn app.main:app --reload
```