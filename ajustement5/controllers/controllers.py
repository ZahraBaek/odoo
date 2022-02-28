# -*- coding: utf-8 -*-
# from odoo import http


# class Ajustement5(http.Controller):
#     @http.route('/ajustement5/ajustement5/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ajustement5/ajustement5/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ajustement5.listing', {
#             'root': '/ajustement5/ajustement5',
#             'objects': http.request.env['ajustement5.ajustement5'].search([]),
#         })

#     @http.route('/ajustement5/ajustement5/objects/<model("ajustement5.ajustement5"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ajustement5.object', {
#             'object': obj
#         })
