# -*- coding: utf-8 -*-

# Se importan los módulos necesarios para definir el model
from odoo import models, fields

class CicloFormativo(models.Model):

    # Define como Odoo guardará el módulo en la base de datos.
    _name = 'ciclos.ciclo'
    
    # Define la descripción del modelo.
    _description = 'Ciclo Formativo'
    
    # Campos obligatorios para nombre y código del ciclo,
    name = fields.Char('Nombre', required = True)
    codigo = fields.Char('Código', required = True)
    
    # Relación con módulos: un ciclo puede tener varios módulos.
    modulo_ids = fields.One2many('ciclos.modulo', 'ciclo_id', 'Módulos')