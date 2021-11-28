# -*- coding: utf-8 -*-
# from odoo import http


# class GrtEquipmentPartKapal(http.Controller):
#     @http.route('/grt_equipment_part_kapal/grt_equipment_part_kapal/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/grt_equipment_part_kapal/grt_equipment_part_kapal/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('grt_equipment_part_kapal.listing', {
#             'root': '/grt_equipment_part_kapal/grt_equipment_part_kapal',
#             'objects': http.request.env['grt_equipment_part_kapal.grt_equipment_part_kapal'].search([]),
#         })

#     @http.route('/grt_equipment_part_kapal/grt_equipment_part_kapal/objects/<model("grt_equipment_part_kapal.grt_equipment_part_kapal"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('grt_equipment_part_kapal.object', {
#             'object': obj
#         })
