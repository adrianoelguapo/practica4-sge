# -*- coding: utf-8 -*-

# Se importan los módulos necesarios para definir el model
from odoo import models, fields

class Alumno(models.Model):

    # Define como Odoo guardará el módulo en la base de datos.
    _name = 'ciclos.alumno'
    
    # Define la descripción del modelo.
    _description = 'Alumno'
    
    # Campos obligatorios para nombre y DNI.
    name = fields.Char('Nombre', required = True)
    dni = fields.Char('DNI', required = True)
    
    # Relación con módulos: muchos alumnos pueden estar en muchos módulos
    modulo_ids = fields.Many2many('ciclos.modulo', string = 'Módulos')