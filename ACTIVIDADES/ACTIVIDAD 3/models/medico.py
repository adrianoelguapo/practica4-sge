# -*- coding: utf-8 -*-

from odoo import models, fields

class Medico(models.Model):

    # Define como Odoo guardará el módulo en la base de datos.
    _name = 'hospital.medico'

    # Define la descripción del modelo.
    _description = 'Médico del Hospital'
    
    # Campo obligatorio para nombre completo
    name = fields.Char(string = 'Nombre y Apellidos', required = True, help = 'Nombre completo del médico')
    
    # Número de colegiado, campo obligatorio y único
    numero_colegiado = fields.Char(string = 'Número de Colegiado', required = True, help = 'Número de colegiado del médico')
    
    # Relación con consultas: un médico puede tener muchas consultas
    consulta_ids = fields.One2many(comodel_name = 'hospital.consulta', inverse_name = 'medico_id', string = 'Consultas', help = 'Lista de consultas realizadas por este médico' )