# -*- coding: utf-8 -*-
{
    'name': 'Actividad 3 - Hospital',
    'version': '1.0',
    'summary': 'Gestión básica de pacientes, médicos y consultas',
    'category': 'Healthcare',
    'author': 'Adriano',
    'website': 'https://staytuned.com.es',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/paciente_views.xml',      # Vistas de pacientes
        'views/medico_views.xml',        # Vistas de médicos
        'views/consulta_views.xml',      # Vistas de consultas
        'views/menu_views.xml',          # Menús
    ],
    'installable': True,
    'application': True,
}