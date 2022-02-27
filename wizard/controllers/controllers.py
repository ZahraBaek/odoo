# -*- coding: utf-8 -*-
# from odoo import http


# class Wizard(http.Controller):
#     @http.route('/wizard/wizard/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wizard/wizard/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('wizard.listing', {
#             'root': '/wizard/wizard',
#             'objects': http.request.env['wizard.wizard'].search([]),
#         })

#     @http.route('/wizard/wizard/objects/<model("wizard.wizard"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wizard.object', {
#             'object': obj
#         })
