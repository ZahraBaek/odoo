# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class CreateLeadWizard(models.TransientModel):
    _name = "create.lead.wizard"
    _description = "Create Lead Wizard"

    name = fields.Char(string='name', required=True)
