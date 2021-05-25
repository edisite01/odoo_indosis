# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.http import route
import base64


class IndDeliverynest(http.Controller):
    @http.route('/nest/', auth='user', type='http', website='True')
    def index(self, **kw):
        src = self.getpartnerid() or ''
        nests = request.env['nest.nests'].search([('vendor_id','=',src)])
        vals = {
            'n' : nests
        }
        return request.render('ind_deliverynest.display_nest',vals)

    @http.route('/nest/create/', auth='user',type='http', website='True')
    def redirect_to_form_nest_create(self, **kw):
        return request.render('ind_deliverynest.create_nest_form')

    @http.route('/nest/save/', auth='user',type='http', website='True')
    def redirect_to_form_nest_save(self, **kw):
        ufile = kw.get('ufile') or ''

        request.env['nest.nests'].create(
            {
                'product_name':kw.get('product_name'),
                'name':'New',
                'weight':kw.get('weight'),
                'date_order':kw.get('date_order'),
                'vendor_id':self.getpartnerid(),
                'image':base64.b64encode(ufile.read())
            }
        )
        return request.redirect('/nest')

    @http.route('/nest/edit/', auth='user',type='http', website='True')
    def redirect_to_form_nest_edit(self, **kw):
        vals = {}
        car_object = request.env['nest.nests'].search([('id','=',kw.get('id'))])
        vals.update({
            'nest':car_object
        })
        return request.render('ind_deliverynest.update_nest_form',vals)


    @http.route('/nest/update/', auth='user',type='http', website='True')
    def redirect_to_form_nest_update(self, **kw):
        id = int(kw.get('id'))
        request.env['nest.nests'].search([('id','=',id)]).write(
            {
                'product_name':kw.get('product_name'),
                'weight':kw.get('weight'),
                'date_order':kw.get('date_order'),
            })
        return request.redirect('/nest')

    @http.route('/nest/delete/', auth='user',type='http', website='True')
    def redirect_to_form_car_delete(self, **kw):
        car_id = int(kw.get('id'))
        request.env['nest.nests'].search([('id','=',car_id)]).unlink()
        return request.redirect('/nest')

    @http.route('/nest/views/', auth='user',type='http', website='True')
    def redirect_to_form_nest_show(self, **kw):
        vals = {}
        car_object = request.env['nest.nests'].search([('id','=',kw.get('id'))])
        vals.update({
            'nest':car_object
        })
        return request.render('ind_deliverynest.show_nest_form',vals)

    @http.route('/nest/draft_toopen/', auth='user',type='http', website='True')
    def redirect_to_form_draft_toopen(self, **kw):
        id = int(kw.get('id'))
        request.env['nest.nests'].search([('id','=',id)]).write(
            {
                'state':'open',
                'name': request.env['ir.sequence'].next_by_code('nest.nests.sequence'),
            })
        return request.redirect('/nest/views/?id=%s'%(id))

    @http.route('/nest/grading_to_approve/', auth='user',type='http', website='True')
    def redirect_to_form_grading_to_approve(self, **kw):
        id = int(kw.get('id'))
        request.env['nest.nests'].search([('id','=',id)]).write(
            {
                'state':'grading_approval',
            })
        return request.redirect('/nest/views/?id=%s'%(id))

    def getpartnerid(self):
        get_userid      = http.request.env.context.get('uid')
        get_partnerid   = request.env['res.users'].search([('id','=',get_userid)]).partner_id.id
        res_partnerid   = request.env['res.partner'].search([('id','=',get_partnerid)]).id
        return res_partnerid


