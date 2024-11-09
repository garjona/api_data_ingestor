# api_data_ingestor

## Descripción

`api_data_ingestor` es una API desarrollada en Python, diseñada para insertar o actualizar datos en una base de datos, con un enfoque particular en la ingesta de noticias. La API permite la creación de nuevas entradas o la actualización de entradas existentes, manteniendo la información de manera organizada y accesible para su posterior uso.

## Características

- **Ingesta de Datos**: Inserción de nuevos datos en la base de datos.
- **Actualización de Datos**: Actualización de registros existentes si la entrada ya se encuentra en la base de datos.
- **Validación de Datos**: Verificación de la estructura de los datos antes de ser insertados o actualizados.
- **Soporte para MongoDB**: Almacenamiento de datos en una base de datos MongoDB, facilitando la escalabilidad y flexibilidad.

## Requisitos

- **Python** 3.11+
- **MongoDB**
- **FastAPI** para la gestión de la API
## Instalación

1. Clonar este repositorio:

   ```bash
   git clone https://github.com/usuario/001_api_data_ingestor.git
   cd 001_api_data_ingestor

2. Crear un entorno virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows, usar `venv\Scripts\activate`
   
3. Instalar las dependencias::

   ```bash
   pip install -r requirements.txt
   
4. Configurar las variables de entorno creando un archivo .env en el directorio principal:

   ```bash
   DB_HOST=<tu_host_de_mongodb>
   DB_PORT=<tu_puerto_de_mongodb>
   DB_CLIENT=<nombre_de_la_base_de_datos>
   API_HOST=<tu_host_api>
   API_PORT=<puerto_api>