
from odoo import _, api, exceptions, fields, models, modules
from odoo.addons.base.models.res_users import is_selection_groups


class Users(models.Model):
    _inherit = 'res.users'


    @api.model
    def systray_get_leads(self):
        """Get leads with states"""
        query = """SELECT m.id, m.x_rappel,
                    CASE
                        WHEN %(today)s::date - x_rappel::date = 0 Then 'today'
                        WHEN %(today)s::date - x_rappel::date > 0 Then 'overdue'
                        WHEN %(today)s::date - x_rappel::date < 0 Then 'planned'
                    END AS states
                    FROM crm_lead AS m
                    WHERE m.type='lead' and m.x_rappel IS NOT NULL
                    GROUP BY m.id, states;
                    """

        self.env.cr.execute(query, {
            'today': fields.Date.context_today(self),
        })
        lead_data = self.env.cr.dictfetchall()
        """Count number of leads according to states"""
        overdue_count = 0
        today_count = 0
        planned_count = 0

        for l in lead_data:
            if l['states'] == 'today':
                today_count +=1
            if l['states'] == 'overdue':
                overdue_count +=1
            if l['states'] == 'planned':
                planned_count +=1

        leads = {'name': 'CRM Qualifications',
                 'icon': modules.module.get_module_icon(self.env['crm.lead']._original_module),
                 'model': 'crm.lead',
                 'total_count': len(lead_data),
                 'today_count':  today_count,
                 'overdue_count': overdue_count,
                 'planned_count': planned_count,
                }
        return leads
