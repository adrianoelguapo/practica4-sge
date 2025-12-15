# -*- coding: utf-8 -*-

# Se importan las los modulos necesarios para definir el modelo
from odoo import models, fields

class Consulta(models.Model):

    # Define como Odoo guardará el módulo en la base de datos.
    _name = 'hospital.consulta'

    # Define la descripción del modelo.
    _description = 'Consulta Médica del Hospital'
    
    # Relación con paciente: Many2one (muchas consultas pueden ser de un paciente).
    paciente_id = fields.Many2one(comodel_name = 'hospital.paciente', string = 'Paciente', required = True, help = 'Paciente atendido en la consulta')
    
    # Relación con médico: Many2one (muchas consultas pueden ser de un médico)
    medico_id = fields.Many2one(comodel_name = 'hospital.medico', string = 'Médico', required = True, help = 'Médico que atendió la consulta')
    
    # Diagnóstico de la consulta.
    diagnostico = fields.Text(string = 'Diagnóstico', required = True, help = 'Diagnóstico realizado por el médico')
    
    # Fecha y hora de la consulta (por defecto, fecha/hora actual).
    fecha_hora = fields.Datetime(string = 'Fecha y Hora', default = fields.Datetime.now, help = 'Fecha y hora de la consulta')