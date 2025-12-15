# -*- coding: utf-8 -*-
{
    'name': "actividad2_comics",  # Titulo del módulo
    'summary': "Gestionar comics :) (Version simple)",  # Resumen de la funcionaliadad
    'description': """
Gestor de bibliotecas (Version Simple)
==============
    """,  
    'application': True,
    'installable': True,
    'author': "Adriano",
    'website': "https://staytuned.com.es",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],

    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/biblioteca_comic.xml',
        'views/biblioteca_socio.xml',
        'views/biblioteca_ejemplar.xml'
    ]
}
