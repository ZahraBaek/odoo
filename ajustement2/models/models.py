# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ajustement1(models.Model):
    _inherit = "crm.lead"

    x_rappel = fields.Datetime(string='Rappel')

