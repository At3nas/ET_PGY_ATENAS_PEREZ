# Setup
## Instalación
**Creación de entorno virtual**
```
virtualenv venv
```

**Activación del entorno virtual**
```
.\venv\Scripts\activate
```

**Instalación de dependencias**
```
pip install -r requirements.txt
```

## Base de datos
1. Entrar en SQL Developer

2. Click derecho en 'Oracle conexiones' en la sección de conexiones en la barra lateral izquierda

3. Click sobre 'Importar conexiones'

4. Seleccionar el archivo 'verdinosDB.json' en la carpeta 'sql' ubicada en los archivos del proyecto

5. Ingresar clave de cifrado: verdinos

6. Ejecutar el script 'SCRIPT_CREAR_TABLAS.sql' dentro de la carpeta 'sql'

# Proyecto
## Estructura
- **Proyecto principal**: losVerdinos

- **Aplicaciones**:
    - **website**: página web de la tienda comunitaria Los Verdinos, la cual es accesible a los clientes. Tiene por objetivo facilitar la promoción y venta de productos, así como permitir a los clientes realizar seguimiento de sus compras.

    - **dataManager**: dashboard para la gestión de los datos que serán visualizados por los clientes en el sitio web, tales como productos, descuentos, entre otros. Su objetivo es facilitar a los administradores la tarea de añadir, modificar y eliminar datos en cualquier momento.

- **Otros archivos y carpetas**:
    - **sql**: carpeta que contiene todos los archivos necesarios para configurar la base de datos del proyecto.

    - **requirements.txt**: archivo que contiene las dependencias y paquetes necesarios para el correcto funcionamiento del proyecto.

    - **readme.md**: documentación del proyecto que explica todo lo necesario para su comprensión y correcta configuración.