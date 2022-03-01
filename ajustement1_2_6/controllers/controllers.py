# -*- coding: utf-8 -*-
from odoo import http


class Ajustement1(http.Controller):
     @http.route('/ajustement1_2_6/ajustement1_2_6/', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/ajustement1_2_6/ajustement1_2_6/objects/', auth='public')
     def list(self, **kw):
         return http.request.render('ajustement1_2_6.listing', {
             'root': '/ajustement1_2_6/ajustement1_2_6',
             'objects': http.request.env['ajustement1_2_6.ajustement1_2_6'].search([]),
         })

     @http.route('/ajustement1_2_6/ajustement1_2_6/objects/<model("ajustement1_2_6.ajustement1_2_6"):obj>/', auth='public')
     def object(self, obj, **kw):
         return http.request.render('ajustement1_2_6.object', {
             'object': obj
         })
