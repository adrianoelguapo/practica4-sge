# -*- coding: utf-8 -*-

{
    'name': 'Gestión de Ciclos Formativos',
    'version': '1.0',
    'summary': 'Gestión de ciclos formativos, módulos, alumnos y profesores',
    'category': 'Education',
    'author': 'Adriano',
    'website': 'https://staytuned.com.es',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/ciclo_formativo_views.xml',  # Vistas de los ciclos
        'views/modulo_views.xml',           # Vistas de los módulos
        'views/alumno_views.xml',           # Vistas de los alumnos
        'views/profesor_views.xml',         # Vistas de los profesores
        'views/menu_views.xml',             # Vistas de los menús
    ],
    'installable': True,
    'application': True,
}