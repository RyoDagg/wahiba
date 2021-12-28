# -*- coding: utf-8 -*-
{
    'name': "Espace Wahiba",

    'summary': """Système de gestion des réservations pour Espace Wahiba""",

    'description': """
        Long description of module's purpose
    """,

    'application' : True,
    'author': "Make It Happen",
    'website': "https://mih.tn/",
	'version' : '13.0.1',

    'category': 'Clothing',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'data' : [
        'views/espace_wahiba_view.xml',
        'views/menu_views.xml',
        'views/wahiba_trees.xml'
    ],
}
