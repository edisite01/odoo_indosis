# -*- coding: utf-8 -*-
{
    'name': "ind_deliverynest",

    'summary': """
        ind_deliverynest""",

    'description': """
        ind_deliverynest
    """,

    'author': "edisite",
    'website': "http://www.sisintegrasi.co.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/dn.xml',
        'views/w_menu_website.xml',
        'views/w_display_nest.xml',
        'views/w_nest_create_form.xml',
        'views/w_nest_update_form.xml',
        'views/w_nest_show_form.xml',
        'views/sequence.xml',
        'wizard/sent_product_wizard.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
