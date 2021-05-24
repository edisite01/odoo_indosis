# -*- coding: utf-8 -*-
{
    'name': "ind_sale_spp",

    'summary': """
        Sale Order Surat Perintah Produksi""",

    'description': """
        Sale Order Surat Perintah Produksi
    """,

    'author': "edisite",
    'website': "http://sisintegrasi.co.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/print.xml',
        'views/product.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'images': ['static/description/banner.png'],
}
