# -*- coding: utf-8 -*-
# from odoo import http


# class Ajustement45(http.Controller):
#     @http.route('/ajustement4_5/ajustement4_5/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ajustement4_5/ajustement4_5/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ajustement4_5.listing', {
#             'root': '/ajustement4_5/ajustement4_5',
#             'objects': http.request.env['ajustement4_5.ajustement4_5'].search([]),
#         })

#     @http.route('/ajustement4_5/ajustement4_5/objects/<model("ajustement4_5.ajustement4_5"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ajustement4_5.object', {
#             'object': obj
#         })
