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
        'views/ciclo_formativo_views.xml',
        'views/modulo_views.xml',
        'views/alumno_views.xml',
        'views/profesor_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
}