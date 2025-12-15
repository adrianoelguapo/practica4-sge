# -*- coding: utf-8 -*-

# Se importan los módulos necesarios de Odoo para definir modelos.
from odoo import models, fields

# Definir modelo.
class BibliotecaSocio(models.Model):
    
    # Define como Odoo guardará el módulo en la base de datos.
    _name = 'biblioteca.socio'
    
    # Descripción del modelo.
    _description = 'Socio de la biblioteca'
    
    # Campo a mostrar por defecto en las vistas y menús.
    _rec_name = 'nombre'

    # Atributos del modelo.
    nombre = fields.Char('Nombre', required = True)                  # Nombre del socio.
    apellido = fields.Char('Apellido', required = True)              # Apellido del socio.
    identificador = fields.Char('Identificador', required = True)    # Identificador del socio.
