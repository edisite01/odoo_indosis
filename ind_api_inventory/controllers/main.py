# -*- coding: utf-8 -*-
from odoo import http
import json
import werkzeug.wrappers

from odoo.http import request

from odoo.addons.restful.controllers.main import (
    validate_token,
)

from odoo.addons.restful.common import (
    extract_arguments,
    invalid_response,
    valid_response,
)

import logging
_logger = logging.getLogger(__name__)


class IndApiExpenses(http.Controller):

    @validate_token
    @http.route('/api/inventory/create_stock_picking', type="json", auth="none", methods=["POST"], csrf=False)
    def createExpense(self, **post):

        _logger.info('CONNECTION SUCCESSFUL!!')
        _logger.info(post)

        stock_picking_insert = {
            # 'name': post.get('name'),
            'partner_id': post.get('delivery_address_id'),
            'picking_type_id': post.get('picking_type_id'),
            'note': post.get('note'),
            'scheduled_date': post.get('date'),
            'origin': post.get('origin')
            # 'location_dest_id': self.partner_id.property_stock_customer.id,
            # 'location_id': self.picking_type_id.default_location_src_id.id
        }

        expenses_id = request.env['stock.picking'].create(stock_picking_insert)
        # expenses_id.action_submit_expenses()
        # expenses_id.state = 'reported'

        # move_id.post()
        return {'result':'OK'}



    @validate_token
    @http.route('/api/inventory/list_stock_picking_type', type="json", auth="none", methods=["POST"], csrf=False)
    def listExpense(self, **post):

        _logger.info('CONNECTION SUCCESSFUL!!')
        _logger.info(post)

        expenses_list = request.env['stock.picking.type'].sudo().search_read(fields=['id','name','code'])
        # return valid_response(expenses_list)
        #     return werkzeug.wrappers.Response(
        #     status=200, content_type="application/json; charset=utf-8", response=json.dumps(expenses_list)
        # )
        # move_id.post()
        return expenses_list
