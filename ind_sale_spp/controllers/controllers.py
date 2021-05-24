# -*- coding: utf-8 -*-
# from odoo import http


# class IndSaleSpp(http.Controller):
#     @http.route('/ind_sale_spp/ind_sale_spp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ind_sale_spp/ind_sale_spp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ind_sale_spp.listing', {
#             'root': '/ind_sale_spp/ind_sale_spp',
#             'objects': http.request.env['ind_sale_spp.ind_sale_spp'].search([]),
#         })

#     @http.route('/ind_sale_spp/ind_sale_spp/objects/<model("ind_sale_spp.ind_sale_spp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ind_sale_spp.object', {
#             'object': obj
#         })
