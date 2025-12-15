# -*- coding: utf-8 -*-

# Se importan los módulos necesarios para definir el modelo.
from odoo import models, fields

class Profesor(models.Model):

    # Define como Odoo guardará el módulo en la base de datos.
    _name = 'ciclos.profesor'
    
    # Define la descripción del modelo.
    _description = 'Profesor'
    
    # Campos obligatorios para nombre y DNI.
    name = fields.Char('Nombre', required = True)
    dni = fields.Char('DNI', required = True)
    
    # Relación con módulos: un profesor imparte varios módulos.
    modulo_ids = fields.One2many('ciclos.modulo', 'profesor_id', 'Módulos')