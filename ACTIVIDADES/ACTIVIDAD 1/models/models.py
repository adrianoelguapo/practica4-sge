# -*- coding: utf-8 -*-

# Se importan los módulos necesarios de Odoo para definir modelos.
from odoo import models, fields, api

# Definir modelo.
class ListaTareas(models.Model):
    
    _name = 'lista_tareas.lista' # Define como como Odoo guardará el módulo en la base de datos. 
    _description = 'Modelo de la lista de tareas' # Descripción del modelo.
    _rec_name = "tarea" # Campo a mostrar por defecto en las vistas y menús.

    # Atributos del modelo.
    tarea = fields.Char(string = "Tarea") # Nombre de la tarea (String).
    prioridad = fields.Integer(string = "Prioridad") # Prioridad de la tarea (Integer).
    fecha = fields.Date(string = "Fecha") # Fecha límite de la tarea (Date).
    urgente = fields.Boolean(string = "Urgente", compute = "_value_urgente", store = True) # Atributo computado de tipo booleano. Será True si la prioridad es mayor a 10
    realizada = fields.Boolean(string = "Realizada") # Define si la tarea ha sido realizada o no (Booleano).

    # Método que se encarga de calcular el valor del atributo 'urgente' en función del valor del atributo 'prioridad'.
    @api.depends('prioridad')
    def _value_urgente(self):
        for record in self:
            # Si la prioridad es mayor que 10, se considera urgente
            record.urgente = record.prioridad > 10