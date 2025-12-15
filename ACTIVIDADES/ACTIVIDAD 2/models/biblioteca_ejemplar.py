# -*- coding: utf-8 -*-

# Se importan los módulos necesarios de Odoo para definir el modelo.
from datetime import timedelta
from odoo import models, fields, api
from odoo.exceptions import ValidationError

# Definir modelo.
class BibliotecaEjemplar(models.Model):
    
    # Define como Odoo guardará el módulo en la base de datos.
    _name = 'biblioteca.ejemplar'
    
    # Define la descripción del modelo.
    _description = 'Ejemplar de Comic'
    
    # Define el campo a mostrar por defecto en las vistas y menús.
    _rec_name = 'comic_id'

    # Atributos del modelo.
    comic_id = fields.Many2one('biblioteca.comic', string = 'Comic', required = True)    # Relación con el modelo de Comic.
    socio_id = fields.Many2one('biblioteca.socio', string = 'Socio Préstamo')            # Relación con el modelo de Socio.
    fecha_inicio = fields.Date('Fecha Inicio Préstamo')                                  # Fecha de inicio del préstamo.
    fecha_fin = fields.Date('Fecha Fin Préstamo')                                        # Fecha de fin del préstamo.
    
    # Método que se encarga de validar las fechas del préstamo.
    @api.constrains('fecha_inicio', 'fecha_fin')
    def _check_fechas(self):

        # Recorre todos los registros del modelo.
        for record in self:
            
            # Si la fecha de inicio es posterior al dia actual, se lanza una error.
            if record.fecha_inicio and record.fecha_inicio > fields.Date.today():
                raise ValidationError('La fecha de inicio del prestamo no puede ser posterior al dia actual.')
            
            # Si la fecha de fin es anterior al dia actual, se lanza una error.
            if record.fecha_fin and record.fecha_fin < fields.Date.today():
                raise ValidationError('La fecha prevista de devolucion no puede ser anterior al dia actual.')
