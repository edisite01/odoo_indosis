from odoo import models, fields, api

class saleAddNote(models.Model):
    _inherit = 'sale.order'

    additional_note = fields.Text(string='Additional Notes')
