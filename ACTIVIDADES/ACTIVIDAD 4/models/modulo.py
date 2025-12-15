# -*- coding: utf-8 -*-

# Se importan los módulos necesarios para definir el model
from odoo import models, fields

class Modulo(models.Model):

    # Define como Odoo guardará el módulo en la base de datos.
    _name = 'ciclos.modulo'
    
    # Define la descripción del modelo.
    _description = 'Módulo'
    
    # Campos obligatorios para nombre y código del módulo.
    name = fields.Char('Nombre', required = True)
    codigo = fields.Char('Código', required = True)
    
    # Relaciones

    # Un módulo pertenece a un solo ciclo
    ciclo_id = fields.Many2one('ciclos.ciclo', 'Ciclo', required = True)
    
    # Un módulo puede tener un solo profesor
    profesor_id = fields.Many2one('ciclos.profesor', 'Profesor')
    
    # Un módulo puede tener muchos alumnos
    alumno_ids = fields.Many2many('ciclos.alumno', string = 'Alumnos')