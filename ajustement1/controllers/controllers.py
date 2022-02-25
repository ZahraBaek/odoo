# -*- coding: utf-8 -*-
from odoo import http


class Ajustement1(http.Controller):
     @http.route('/ajustement1/ajustement1/', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/ajustement1/ajustement1/objects/', auth='public')
     def list(self, **kw):
         return http.request.render('ajustement1.listing', {
             'root': '/ajustement1/ajustement1',
             'objects': http.request.env['ajustement1.ajustement1'].search([]),
         })

     @http.route('/ajustement1/ajustement1/objects/<model("ajustement1.ajustement1"):obj>/', auth='public')
     def object(self, obj, **kw):
         return http.request.render('ajustement1.object', {
             'object': obj
         })
