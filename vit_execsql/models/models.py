# -*- coding: utf-8 -*-

from odoo import models, fields, api

class vit_execsql(models.Model):
    _name = 'vit_execsql.vit_execsql'

    name = fields.Char("Name")
    sql = fields.Text("SQL Commands", required=True)

    def action_execute(self):
        self.env.cr.execute(self.sql)