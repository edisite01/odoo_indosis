# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ind_sale_order_line_spp(models.Model):
    _inherit = 'sale.order.line'

    slump           = fields.Float(string='Slump')
    metode_curah    = fields.Char(string='Metode Curah')
    waktu_loading   = fields.Integer(string='Waktu Loading')

class ind_sale_order_spp(models.Model):
    _inherit = ['sale.order']

    kontraktor = fields.Many2one(
        comodel_name='res.partner',
        string='Kontraktor'
        )
    name_proyek         = fields.Char(string='Nama Proyek')
    contact_person      = fields.Char(string='Contact Person')
    hp                  = fields.Char(string='No. HP')
    alamat_proyek       = fields.Char(string='Alamat Proyek')


class ind_product_margin(models.Model):
    _inherit = ['product.template']

    ind_margin = fields.Float(compute='_compute_total', string='Margin', store=False)

    @api.depends('list_price','standard_price')
    def _compute_total(self):
        for order_doc in self:
            list_price = order_doc.list_price
            standard_price  = order_doc.standard_price
            order_doc.ind_margin = list_price - standard_price

