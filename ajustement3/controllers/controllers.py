# -*- coding: utf-8 -*-
from odoo import http


class Ajustement3(http.Controller):
     @http.route('/ajustement3/ajustement3/', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/ajustement3/ajustement3/objects/', auth='public')
     def list(self, **kw):
         return http.request.render('ajustement3.listing', {
             'root': '/ajustement3/ajustement3',
             'objects': http.request.env['ajustement3.ajustement3'].search([]),
         })

     @http.route('/ajustement3/ajustement3/objects/<model("ajustement3.ajustement3"):obj>/', auth='public')
     def object(self, obj, **kw):
         return http.request.render('ajustement3.object', {
             'object': obj
         })
