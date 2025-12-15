# -*- coding: utf-8 -*-

# Se importan los módulos necesarios para definir el modelo.
from odoo import models, fields, api

class Paciente(models.Model):

    # Define como Odoo guardará el módulo en la base de datos.
    _name = 'hospital.paciente'

    # Define la descripción del modelo.
    _description = 'Paciente del Hospital'
    
    # Campo obligatorio para nombre completo.
    name = fields.Char(string = 'Nombre y Apellidos', required = True, help = 'Nombre completo del paciente')
    
    # Síntomas del paciente
    symptoms = fields.Text(string = 'Síntomas', help = 'Descripción de los síntomas del paciente')
    
    # Relación con consultas: un paciente puede tener muchas consultas.
    consulta_ids = fields.One2many(comodel_name = 'hospital.consulta', inverse_name = 'paciente_id', string = 'Consultas', help = 'Lista de consultas')