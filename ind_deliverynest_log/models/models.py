# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class ind_deliverynest_log(models.Model):
    _name = 'nest.nests'
    _inherit = ['nest.nests','mail.thread','mail.activity.mixin']

    state = fields.Selection(track_visibility='onchange')
