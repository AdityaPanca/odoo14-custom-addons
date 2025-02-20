{
    'name': 'Material Registration',
    'version': '14.1.0',
    'summary': 'Module for registering materials with REST API support',
    'description': 'Allows CRUD operations for materials with REST API and validation.',
    'category': 'Inventory',
    'author': 'Aditya Panca Putra',
    'depends': [
        'base',
        'contacts'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/material_views.xml',
        'views/material_templates.xml',
        'views/material_menu.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}