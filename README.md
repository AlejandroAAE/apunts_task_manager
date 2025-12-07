# Apunts Task Manager (Odoo)

Módulo personalizado para gestionar tareas internas dentro de Odoo.

## Funcionalidades

- Modelo `task.task`
- Campos:
  - Título
  - Responsable
  - Fecha límite
  - Estado
  - Prioridad
  - Descripción
- Vistas:
  - Lista
  - Formulario
  - Búsqueda avanzada
- Filtros útiles:
  - Por prioridad
  - Por estado
  - Por fecha límite (vencidas, hoy, próximas)
- Menú propio dentro del panel de Odoo

## Instalación

1. Copiar la carpeta `apunts_task_manager` dentro de la ruta `addons` de tu instalación Odoo.
2. Activar el modo desarrollador en Odoo.
3. Instalar el módulo desde Ajustes → Aplicaciones.
