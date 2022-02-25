# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ajustement3(models.Model):
     _inherit = "res.partner"

     x_partner_id = fields.One2many("crm.lead", "partner_id", string="Tests")

