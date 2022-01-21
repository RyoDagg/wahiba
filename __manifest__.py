# -*- coding: utf-8 -*-
{
    'name': "Texitile Production and Stock Mangement",

    'summary': "Système de gestion Textile",

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
        'views/actions_view.xml',
        'views/menu_views.xml',
        'views/forms/prototype_form.xml',
        'views/trees/prototype_tree.xml',
        'views/trees/matiere_tree.xml'
    ],
}
