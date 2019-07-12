# -*- coding: utf-8 -*-
{
    'name': "xmarts_budget",

    'summary': """
        Adecuaciones a linea presupuestos """,

    'description': """
        Adecuaciones a presupuestos
    """,

    'author': "Xmarts",
    'website': "http://xmarts.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account_budget'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}