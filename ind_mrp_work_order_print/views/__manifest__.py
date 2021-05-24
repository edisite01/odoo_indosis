# -*- coding: utf-8 -*-
##############################################################################
#
#    This module uses OpenERP, Open Source Management Solution Framework.
#    Copyright (C) 2017-Today Sitaram
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

{
    'name': "Print in sales order, invoice, inventory, and purchase order reports",
    'version': "13.0.0.0",
    'summary': "Print  in sales orders, invoices, inventory, and purchase reports",
    'category': 'Extra Tools',
    'description': """
    print in all odoo reports
    inherit sales order report template
    inherit customer invoice report template
    inherit vendor bill report template
    inherit inventory report template
    inherit purchase order report template
    inherit request for quotation template

    """,
    'author': "edisite",
    'website':"http://www.sisintegrasi.co.id",
    'depends': ['base', 'sale_management', 'purchase', 'stock', 'account'],
    'data': [
        'reports/inherited_sale_order_report.xml',
        'reports/inherited_invoice_order_report.xml',
        'reports/inherited_purchase_order_report.xml',
        'reports/inherited_delivery_order_report.xml',
        'reports/inherited_expense_sheet_report.xml'
    ],
    'demo': [],
    "external_dependencies": {},
    "license": "AGPL-3",
    'installable': True,
    'auto_install': False,
    'images': ['static/description/banner.png'],

}
