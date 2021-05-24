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


class IndApiAccounting(http.Controller):
    @validate_token
    @http.route('/api/account/jurnal_entry', type="json", auth="none", methods=["POST"], csrf=False)
    def jurnalEntry(self, **post):

        _logger.info('CONNECTION SUCCESSFUL!!')
        _logger.info(post)

        move = {
            'ref': post.get('ref'),
            'journal_id': post.get('journal_id'),
            'date': post.get('date'),
        }

        _logger.info(move)
        aml_obj = request.env['account.move.line'].with_context(check_move_validity=False)
        move_id = request.env['account.move'].create(move)
        _logger.info(move_id)

        for mvlines in post.get('lines'):
            aml_obj_line = {
                    'analytic_account_id': False,
                    'analytic_line_ids': [],
                    'tax_line_id': False,
                    'currency_id': False,
                    'credit': mvlines['debit'],
                    'debit': mvlines['credit'],
                    'account_id': mvlines['account_id'],
                    'move_id': move_id.id,
                }

            aml_obj.create(aml_obj_line)

            # _logger.info(res)

        move_id.post()
        return {'result':'OK'}


