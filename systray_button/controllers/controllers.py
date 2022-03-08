# -*- coding: utf-8 -*-
# from odoo import http


# class SystrayButton(http.Controller):
#     @http.route('/systray_button/systray_button/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/systray_button/systray_button/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('systray_button.listing', {
#             'root': '/systray_button/systray_button',
#             'objects': http.request.env['systray_button.systray_button'].search([]),
#         })

#     @http.route('/systray_button/systray_button/objects/<model("systray_button.systray_button"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('systray_button.object', {
#             'object': obj
#         })
