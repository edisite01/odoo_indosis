from odoo import models, fields, api, _
from odoo.exceptions import UserError


class grt_equipment_part_kapal(models.Model):
    # _name = 'grt_equipment_part_kapal.grt_equipment_part_kapal'
    _inherit = 'maintenance.equipment'

    tipe_part           = fields.Selection([
            ('fastmoving', 'Fast Moving'),
            ('slowmoving', 'Slow Moving'),
        ], string='Tipe Part', default='fastmoving')

    fast_moving           = fields.Selection([
            ('rekondisi', 'Rekondisi'),
            ('baru', 'Baru'),
            ('best_condition', 'Best Condition'),
        ], string='Fast Moving', default='rekondisi')

    slow_moving           = fields.Selection([
            ('rekondisi', 'Rekondisi'),
            ('baru', 'Tidak Rekondisi / Baru'),
        ], string='Slow Moving', default='rekondisi')
    catatan = fields.Text(string='Catatan')

    running_hour = fields.Char(string='Running Hours')
    max_pemakaian   = fields.Char(string='Max. Pemakaian')
    expired_date = fields.Date(string='Expird Date')


class grt_maintenance_part_kapal(models.Model):
    _inherit = ['maintenance.request']

    estimate_expense = fields.Float(string='Estimate Expense')
