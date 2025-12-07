from odoo import models, fields

class Task(models.Model):
    _name = 'task.task'
    _description = 'Tarea interna'

    name = fields.Char("Título", required=True)
    user_id = fields.Many2one('res.users', string="Responsable")
    deadline = fields.Date("Fecha límite")
    status = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En progreso'),
        ('completada', 'Completada'),
    ], default='pendiente', string="Estado")
    priority = fields.Selection([
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    ], default ='baja', string="Prioridad")
    description = fields.Text("Descripción")
