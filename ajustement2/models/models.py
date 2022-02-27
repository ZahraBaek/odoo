# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ajustement2(models.Model):
    _inherit = "crm.lead"

    x_rappel = fields.Datetime(string='Rappel')

