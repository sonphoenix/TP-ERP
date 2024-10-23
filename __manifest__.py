# -*- coding: utf-8 -*-
{
    'name': 'Gestion de Bibliotheque',
    'version': '1.0',
    'category': 'Bibliotheque',
    'author': 'Ferradj Omar',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/auteur_views.xml',
        'views/livre_views.xml',
        'views/emprunteur_views.xml',
        'views/emprunt_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
}
