# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResUser(models.Model):
    _inherit = 'res.users'

    def get_user_address(self):
        user = self.env.user
        address = ""
        if user:
            address = user.partner_id.street + "," + user.partner_id.city + "," + user.partner_id.state_id.name
        return address

# class systray_button(models.Model):
#     _name = 'systray_button.systray_button'
#     _description = 'systray_button.systray_button'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
