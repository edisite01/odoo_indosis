from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError

class SentProductWizard(models.TransientModel):

    _name = 'nest.nests.wizard'

    nomor_resi      = fields.Char(string='Nomor Resi')
    sender_date     = fields.Date(string='Sender Date ', default=fields.Date.today())
    shipper         = fields.Selection([("jnt","J&T"),("jne","JNE"),("cod","COD / Manually")], string='Shipper / Carrier')

    nest_id = fields.Many2one(
        string='Nest',
        comodel_name='nest.nests',
        ondelete='restrict',
    )


    def process_wizard(self):
        ids_to_change   = self._context.get('active_ids')
        active_model    = self._context.get('active_model')
        doc_ids         = self.env[active_model].browse(ids_to_change)
        self.nest_id    = doc_ids.id
        doc_ids.state   = 'sent'

        line_obj        =self.env['nest.nests.sent']
        line_vals       ={
            'nomor_resi':self.nomor_resi,
            'sender_date':self.sender_date,
            'shipper' : self.shipper,
            'sent_id' : doc_ids.id
        }
        line_obj.create(line_vals)

