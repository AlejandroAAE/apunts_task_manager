# Apunts Task Manager

Un módulo sencillo y funcional para Odoo 17 que permite gestionar tareas internas dentro de una organización.  
Incluye creación de tareas, fechas límite, prioridad, estado y filtrado avanzado desde la vista de búsqueda.

## Características principales

- Creación y edición de tareas internas.
- Campos esenciales:
  - **Título**
  - **Responsable**
  - **Fecha límite**
  - **Estado** (`pendiente`, `en_progreso`, `completada`)
  - **Prioridad** (`baja`, `media`, `alta`)
  - **Descripción**
- Vistas incluidas:
  - Lista (tree)
  - Formulario
  - Búsqueda avanzada
- Filtros prácticos:
  - Por prioridad
  - Por estado
  - Por fechas (hoy, atrasadas, próximas)
  - Mis tareas (usuario actual)
- Agrupación por estado, responsable o prioridad.

---

## Instalación

 1. Copiar el módulo
Clona este repositorio dentro de la carpeta `addons` de tu instancia de Odoo:

```bash
git clone https://github.com/AlejandroAAE/apunts_task_manager.git

2. Ejecutar Odoo con Docker (opcional)

Ejemplo básico de docker-compose.yml:

services:
  web:
    image: odoo:17
    depends_on:
      - db
    ports:
      - "8069:8069"
    volumes:
      - ./addons:/mnt/extra-addons
      - ./odoo-web-data:/var/lib/odoo

  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=odoo
      - POSTGRES_PASSWORD=odoo
    volumes:
      - ./pg-data:/var/lib/postgresql/data


Levantar contenedores:

docker compose up -d


3. Activar el módulo en Odoo

Ir a Apps.

Activar el Modo Desarrollador.

Pulsar “Actualizar lista de módulos”.

Buscar Apunts Task Manager e instalarlo.




Estructura del módulo
apunts_task_manager/
│
├── __manifest__.py
├── models/
│   └── task.py
├── views/
│   └── task_views.xml
├── imagenes/
└── __init__.py


### Aspecto Base
<img src="imagenes/tareas1.png" width="1000">

### Filtros
<img src="imagenes/tareas2.png" width="1000">

### Filtros 2
<img src="imagenes/tareas3.png" width="1000">


