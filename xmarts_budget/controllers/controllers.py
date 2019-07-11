# -*- coding: utf-8 -*-
from odoo import http

# class XmartsBudget(http.Controller):
#     @http.route('/xmarts_budget/xmarts_budget/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xmarts_budget/xmarts_budget/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xmarts_budget.listing', {
#             'root': '/xmarts_budget/xmarts_budget',
#             'objects': http.request.env['xmarts_budget.xmarts_budget'].search([]),
#         })

#     @http.route('/xmarts_budget/xmarts_budget/objects/<model("xmarts_budget.xmarts_budget"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xmarts_budget.object', {
#             'object': obj
#         })