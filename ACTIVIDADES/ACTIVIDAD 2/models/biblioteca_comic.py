# -*- coding: utf-8 -*-

# Se importan los módulos necesarios para definir el modelo.
from datetime import timedelta
from odoo import models, fields, api
from odoo.exceptions import ValidationError

# Se define el modelo abstracto BaseArchive
class BaseArchive(models.AbstractModel):

    # Define como Odoo guardará el módulo en la base de datos.
    _name = 'base.archive'
    
    # Define la descripción del modelo.
    _description = 'Fichero abstracto'

    # Atributo del modelo que define si el cómic está archivado o no.
    activo = fields.Boolean(default = True)

    # Método que se encarga de archivar el cómic.
    def archivar(self):
        for record in self:
            record.activo = not record.activo


# Definimos modelo Biblioteca comic
class BibliotecaComic(models.Model):

    # Define como Odoo guardará el módulo en la base de datos.
    _name = 'biblioteca.comic'
    
    # Define la descripción del modelo.
    _description = 'Comic de biblioteca'
    
    # Define el campo a mostrar por defecto en las vistas y menús.
    _rec_name = 'nombre'

    # Herencia de la clase BaseArchive.
    _inherit = ['base.archive']

    # Atributos del modelo.
    nombre = fields.Char('Titulo', required = True, index = True)                   # Título del cómic.
    estado = fields.Selection(
        [('borrador', 'No disponible'),
         ('disponible', 'Disponible'),
         ('perdido', 'Perdido')],
        'Estado', default = "borrador")                                              # Estado del cómic (selección entre las opciones definidas).
    descripcion = fields.Html('Descripción', sanitize = True, strip_style = False)   # Descripción del cómic.
    portada = fields.Binary('Portada Comic')                                         # Portada del cómic.
    fecha_publicacion = fields.Date('Fecha publicación')                             # Fecha de publicación del cómic.
    precio = fields.Float('Precio')                                                  # Precio del cómic.
    paginas = fields.Integer('Numero de páginas',
        groups = 'base.group_user',
        states = {'perdido': [('readonly', True)]},
        help = 'Total numero de paginas',
        company_dependent = False
    )                                                                                 # Número de páginas del cómic.
    valoracion_lector = fields.Float(
        'Valoración media lectores',
        digits = (14, 4),
    )                                                                                 # Valoración media de los lectores.
    autor_ids = fields.Many2many('res.partner', string = 'Autores')                   # Autores del cómic.
    
    # Define las restricciones SQL del modelo.
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (nombre)', 'El título del cómic debe ser único.'),
        ('positive_page', 'CHECK(paginas>0)', 'El cómic debe tener al menos una página')
    ]

    # Método que se encarga de validar la fecha de publicación del cómic.
    @api.constrains('fecha_publicacion')
    def _check_release_date(self):
        
        # Recorre todos los registros del modelo.
        for record in self:
            
            # Si la fecha de publicación es posterior al dia actual, se lanza una error.
            if record.fecha_publicacion and record.fecha_publicacion > fields.Date.today():
                raise models.ValidationError('La fecha de lanzamiento debe ser anterior a la actual')