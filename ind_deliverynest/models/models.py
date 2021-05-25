from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class DeliveryNestModel(models.Model):
    _name = 'nest.nests'

    name            = fields.Char(string='Nomor', default="New", readonly="1")
    product_name    = fields.Char(string='Product Name')
    weight          = fields.Integer(string='Weight')
    state           = fields.Selection([
            ('draft', 'Draft'),
            ('open', 'Open'),
            ('approve', 'Approve'),
            # ('done', 'Done'),
            ('sent', 'Sent'),
            ('receive', 'Received'),
            ('cleanrinse', 'Clean and Rinse'),
            ('grading', 'Grading'),
            ('grading_approval', 'Grading Approval'),
            ('purchase', 'Purchase'),
            ('billing', 'Billing'),
            ('done', 'Done'),
            ('cancel', 'Canceled'),
        ], string='Status', default='draft')

    image = fields.Binary(string='Image')
    vendor_id = fields.Many2one(
        string='Vendor',
        comodel_name='res.partner',
        ondelete='restrict',
    )
    date_order          = fields.Date(string='Schedule Delivery ', default=fields.Date.today())
    sent_ids            = fields.One2many('nest.nests.sent', 'sent_id', string='Lines Sent')
    receive_ids         = fields.One2many('nest.nests.receive', 'receive_id', string='Lines')
    cleanandrinse_ids   = fields.One2many('nest.nests.cleanandrinse', 'cleanandrinse_id', string='Lines')
    grading_ids         = fields.One2many('nest.nests.grading', 'grading_id', string='Lines')
    purchase_ids        = fields.One2many('nest.nests.purchase', 'purchase_id', string='Lines')
    billing_ids         = fields.One2many('nest.nests.billing', 'billing_id', string='Lines')


    def set_open(self):
        for doc in self:
            seqnest = self.env['ir.sequence'].next_by_code('nest.nests.sequence')
            doc.name = seqnest
            doc.state = 'open'

    def set_approve(self):
        for doc in self:
            doc.state = 'approve'
    def set_cancel(self):
        for doc in self:
            doc.state = 'cancel'
            doc.name = '/'
    def set_receive(self):
        for doc in self:
            doc.state = 'receive'
    def set_cleanandrinse(self):
        for doc in self:
            doc.state = 'cleanrinse'
    def set_grading(self):
        for doc in self:
            doc.state = 'grading'
    def set_grading_approval(self):
        for doc in self:
            doc.state = 'grading_approval'
    def set_purchase(self):
        for doc in self:
            doc.state = 'purchase'
    def set_billing(self):
        for doc in self:
            doc.state = 'billing'
    def set_done(self):
        for doc in self:
            doc.state = 'done'
    def set_sent_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Popup',
            'res_model': 'nest.nests.wizard',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
        }
    # def unlink(self):
    #     for container in self:
    #         if container.state not in ('draft', 'cancel'):
    #             raise UserError(_('You cannot delete a Container which is not draft or cancelled. You should cancel it first.'))
    #     return super(DeliveryNestModel, self).unlink()


class DeliveryNestSent(models.Model):
    _name = 'nest.nests.sent'

    sent_id         = fields.Many2one('nest.nests', string='Return',ondelete='cascade')
    nomor_resi      = fields.Char(string='Nomor Resi')
    sender_date     = fields.Date(string='Sender Date ', default=fields.Date.today())
    shipper         = fields.Selection([("jnt","J&T"),("jne","JNE"),("cod","COD / Manually")], string='Shipper / Carrier')

class DeliveryNestSent(models.Model):
    _name = 'nest.nests.receive'

    receive_id          = fields.Many2one('nest.nests', string='Return',ondelete='cascade')
    receive_date        = fields.Date(string='Received Date ', default=fields.Date.today())
    pic_id              = fields.Many2one(comodel_name='res.partner',string='PIC')

class DeliveryNestCleanandrinse(models.Model):
    _name = 'nest.nests.cleanandrinse'

    cleanandrinse_id        = fields.Many2one('nest.nests', string='Return',ondelete='cascade')
    cleanandrinse_date      = fields.Date(string='Clean and Rinse Date ', default=fields.Date.today())
    pic_id                  = fields.Many2one(comodel_name='res.partner',string='PIC')
    weight_cleanandrinse    = fields.Integer(string='Weight Clean')

class DeliveryNestGrading(models.Model):
    _name = 'nest.nests.grading'

    grading_id              = fields.Many2one('nest.nests', string='Return',ondelete='cascade')
    grading_date            = fields.Date(string='Grading Date ', default=fields.Date.today())
    pic_id                  = fields.Many2one(comodel_name='res.partner',string='PIC')
    weight_grading          = fields.Integer(string='Weight grading')
    price                   = fields.Integer(string='Price')

class DeliveryNestPurchase(models.Model):
    _name = 'nest.nests.purchase'

    purchase_id              = fields.Many2one('nest.nests', string='Return',ondelete='cascade')
    purchase_date            = fields.Date(string='Purchase Date ', default=fields.Date.today())
    pic_id                  = fields.Many2one(comodel_name='res.partner',string='PIC')
    weight_grading          = fields.Integer(string='Weight grading')
    price                   = fields.Integer(string='Price')

class DeliveryNestBilling(models.Model):
    _name = 'nest.nests.billing'

    billing_id              = fields.Many2one('nest.nests', string='Return',ondelete='cascade')
    # billing_date            = fields.Date(string='Billing Date ', default=fields.Date.today())
    # pic_id                  = fields.Many2one(comodel_name='res.partner',string='PIC')
    # weight_grading          = fields.Integer(string='Weight grading')
    payment                 = fields.Integer(string='Payemnt')

