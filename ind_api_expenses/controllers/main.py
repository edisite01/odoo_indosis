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
    @http.route('/api/expenses/create_expenses', type="json", auth="none", methods=["POST"], csrf=False)
    def createExpense(self, **post):

        _logger.info('CONNECTION SUCCESSFUL!!')
        _logger.info(post)

        expenses_insert = {
            'name': post.get('name'),
            'product_id': post.get('product_id'),
            'unit_amount': post.get('unit_amount'),
            'quantity': post.get('quantity'),
            'employee_id': post.get('employee_id'),
            'payment_mode': post.get('paid_by'),
            'description': post.get('journal_id'),
            'date': post.get('date'),
        }

        expenses_id = request.env['hr.expense'].create(expenses_insert)
        expenses_id.action_submit_expenses()
        expenses_id.state = 'reported'

        # move_id.post()
        return {'result':'OK'}



    @validate_token
    @http.route('/api/expenses/list_expenses', type="json", auth="none", methods=["POST"], csrf=False)
    def listExpense(self, **post):

        _logger.info('CONNECTION SUCCESSFUL!!')
        _logger.info(post)

        expenses_list = request.env['hr.expense'].sudo().search_read(fields=['id','name','state','employee_id','total_amount'])
        # return valid_response(expenses_list)
        #     return werkzeug.wrappers.Response(
        #     status=200, content_type="application/json; charset=utf-8", response=json.dumps(expenses_list)
        # )
        # move_id.post()
        return json.dumps(expenses_list)


