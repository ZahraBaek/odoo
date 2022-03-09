# -*- coding: utf-8 -*-
from odoo import http

# class Ajustement3Ver12(http.Controller):
#     @http.route('/ajustement3_ver12/ajustement3_ver12/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ajustement3_ver12/ajustement3_ver12/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ajustement3_ver12.listing', {
#             'root': '/ajustement3_ver12/ajustement3_ver12',
#             'objects': http.request.env['ajustement3_ver12.ajustement3_ver12'].search([]),
#         })

#     @http.route('/ajustement3_ver12/ajustement3_ver12/objects/<model("ajustement3_ver12.ajustement3_ver12"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ajustement3_ver12.object', {
#             'object': obj
#         })