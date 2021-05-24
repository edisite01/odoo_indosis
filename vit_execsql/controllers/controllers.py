# -*- coding: utf-8 -*-
from odoo import http

# class VitExecsql(http.Controller):
#     @http.route('/vit_execsql/vit_execsql/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_execsql/vit_execsql/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_execsql.listing', {
#             'root': '/vit_execsql/vit_execsql',
#             'objects': http.request.env['vit_execsql.vit_execsql'].search([]),
#         })

#     @http.route('/vit_execsql/vit_execsql/objects/<model("vit_execsql.vit_execsql"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_execsql.object', {
#             'object': obj
#         })