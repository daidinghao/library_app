from odoo import models, fields, api

class Partner(models.Model):
    _inherit = 'res.partner'

    is_library_member = fields.Boolean(string="Is it a reader?")
    library_member_id = fields.Many2one('library.member', string="Related readers")

    @api.onchange('is_library_member')
    def _onchange_library_member_flag(self):
        if self.is_library_member and not self.library_member_id:
            member = self.env['library.member'].create({
                'name': self.name,
            })
            self.library_member_id = member